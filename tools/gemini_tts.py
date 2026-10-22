"""Zwei-Stimmen-Vertonung mit Gemini TTS.

Aufruf: python3 tools/gemini_tts.py <skript.md> <ausgabe.mp3> [max_abschnitte]

Das Skript besteht aus Zeilen "NAME: Text". Welche Namen welche Stimme bekommen,
steht in SPEAKERS (Umgebungsvariable), Standard: Lern-Podcast mit Mira und Jan.
  SPEAKERS="MIRA:Aoede,JAN:Charon"     (Lern-Podcast)
  SPEAKERS="LENA:Kore,TOM:Orus"         (KI-News)
TEMPO = Abspielfaktor (Standard 1.1). Der Schlüssel liegt in /root/.podcast/gemini_key.
"""
import json, sys, base64, subprocess, urllib.request, re, os, time

KEY = open("/root/.podcast/gemini_key").read().strip()
TEMPO = os.environ.get("TEMPO", "1.1")
# Hauptmodell: gemini-2.5-flash-preview-tts bekommt das Gespräch als Text mit "Name: ..." je Zeile
# und hält die Sprecherwechsel zuverlässig ein. Die 3.8-Modelle klingen etwas lebendiger, verwechseln
# aber in längeren Abschnitten die Sprecher; sie dienen nur als Ausweich bei erschöpftem Kontingent.
MODEL = os.environ.get("TTS_MODEL", "gemini-2.5-flash-preview-tts")
# Ausweichmodelle, falls das Tageskontingent eines Modells (100 Anfragen) aufgebraucht ist.
# Jedes Modell hat ein eigenes Kontingent; gleiche Stimmen, leicht anderer Klang.
MODELLE = [MODEL] + [m for m in ["gemini-3.8-flash-tts", "gemini-3.8-flash-lite-tts"] if m != MODEL]
_aktiv = [0]  # Index des aktuell genutzten Modells (bleibt für die restlichen Abschnitte)
SPEAKERS = dict(p.split(":") for p in os.environ.get("SPEAKERS", "MIRA:Aoede,JAN:Charon").split(","))
NAMES = {k.upper(): k.capitalize() for k in SPEAKERS}  # MIRA -> Mira


AUSSPRACHE_DATEI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aussprache.json")
AUSSPRACHE = json.load(open(AUSSPRACHE_DATEI, encoding="utf-8")) if os.path.exists(AUSSPRACHE_DATEI) else {}


def aussprache(text):
    """Ersetzt Wörter, die Gemini falsch ausspricht, durch eine Schreibweise, die richtig klingt."""
    for wort, gesprochen in AUSSPRACHE.items():
        text = re.sub(r"\b" + re.escape(wort) + r"\b", gesprochen, text)
    return text


def saeubern(wav_in, wav_out):
    """Entfernt Geminis Störgeräusche am Rand jedes Abschnitts: ein kurzes Knacken am Anfang und einen
    lauten Rauschstoß am Ende. Schneidet bis zur ersten bzw. nach der letzten Stille und blendet weich."""
    import wave
    import numpy as np
    w = wave.open(wav_in)
    a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float64)
    win = 240  # 10 ms
    rms = np.array([np.sqrt(np.mean(a[i:i + win] ** 2)) for i in range(0, len(a) - win, win)])
    still = rms < 200
    # Anfang: erstes stilles Fenster innerhalb der ersten 200 ms
    start = 0
    for i in range(min(20, len(still))):
        if still[i]:
            start = i
            break
    # Ende: lauter Stoß in den letzten 400 ms -> bis zur letzten Stille davor abschneiden
    end = len(rms)
    tail = range(max(0, len(rms) - 40), len(rms))
    if any(rms[i] > 6000 for i in tail):
        for i in range(len(rms) - 1, max(0, len(rms) - 60), -1):
            if still[i] and not any(rms[j] > 6000 for j in range(i, max(i - 5, 0), -1)):
                end = i + 1
                break
    s0, s1 = start * win, end * win
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav_in, "-af",
                    f"atrim=start_sample={s0}:end_sample={s1},afade=t=in:d=0.015,areverse,afade=t=in:d=0.03,areverse",
                    wav_out], check=True)


def tts(dialog, out_wav):
    parts = []
    for l in dialog.splitlines():
        sp, t = l.split(":", 1)
        parts.append({"text": aussprache(t.strip()), "speechMetadata": {"speaker": sp}})
    # Reihenfolge der Stimmen = Reihenfolge des ersten Auftritts im Abschnitt. Gemini ordnet die
    # Stimmen sonst teilweise nach Position statt nach Namen zu (Stimmen vertauscht).
    order = []
    for prt in parts:
        if prt["speechMetadata"]["speaker"] not in order:
            order.append(prt["speechMetadata"]["speaker"])
    for k in SPEAKERS:
        if NAMES[k.upper()] not in order:
            order.append(NAMES[k.upper()])
    voice_of = {NAMES[k.upper()]: v for k, v in SPEAKERS.items()}
    voices = [{"speaker": n, "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice_of[n]}}} for n in order]
    body = {"contents": [{"role": "user", "parts": parts}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"multiSpeakerVoiceConfig": {"speakerVoiceConfigs": voices}}}}
    attempt = 0
    while True:
        model = MODELLE[_aktiv[0]]
        if model.startswith("gemini-2.5"):
            # älteres Format: ein Textblock mit "Name: Text"-Zeilen, Namen werden nicht vorgelesen
            namen = " und ".join(order)
            text = f"Lies das folgende Gespräch zwischen {namen} auf Deutsch vor:\n" + "\n".join(
                f'{p["speechMetadata"]["speaker"]}: {p["text"]}' for p in parts)
            body = {"contents": [{"parts": [{"text": text}]}], "generationConfig": body["generationConfig"]}
        else:
            body = {"contents": [{"role": "user", "parts": parts}], "generationConfig": body["generationConfig"]}
        req = urllib.request.Request(
            f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
            data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=600))
            break
        except Exception as e:
            err = e.read().decode()[:800] if hasattr(e, "read") else str(e)
            print("retry", model, attempt, err[:300], file=sys.stderr)
            if "400" in str(e):
                raise SystemExit("TTS bad request")
            if "PerDay" in err or "per_day" in err:
                if _aktiv[0] + 1 < len(MODELLE):
                    _aktiv[0] += 1
                    print("Tageskontingent erschöpft, weiter mit", MODELLE[_aktiv[0]], file=sys.stderr)
                    continue
                raise SystemExit("TTS failed: Tageskontingent aller Modelle erschöpft")
            attempt += 1
            if attempt >= 8:
                raise SystemExit("TTS failed")
            time.sleep(min(60 * attempt, 300))
    pcm = b"".join(base64.b64decode(p["inlineData"]["data"])
                   for p in d["candidates"][0]["content"]["parts"] if "inlineData" in p)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", "-", out_wav],
                   input=pcm, check=True)
    return d.get("usageMetadata", {})


def chunks(script, max_chars=int(os.environ.get("CHUNK_CHARS", "2500"))):
    pat = re.compile(r"^(" + "|".join(NAMES) + r"):")
    lines = [l for l in open(script, encoding="utf-8").read().splitlines() if pat.match(l)]
    lines = [NAMES[l.split(":", 1)[0]] + ":" + l.split(":", 1)[1] for l in lines]
    # Spricht dieselbe Person mehrmals direkt hintereinander, zu einer Zeile zusammenfassen.
    # Gemini wechselt sonst bei jedem Beitrag die Stimme, und ab da sind die Stimmen vertauscht.
    merged = []
    for l in lines:
        if merged and merged[-1].split(":", 1)[0] == l.split(":", 1)[0]:
            merged[-1] = merged[-1] + " " + l.split(":", 1)[1].strip()
        else:
            merged.append(l)
    lines = merged
    cur, n = [], 0
    for l in lines:
        if n + len(l) > max_chars and cur:
            yield "\n".join(cur)
            cur, n = [], 0
        cur.append(l)
        n += len(l)
    if cur:
        yield "\n".join(cur)


if __name__ == "__main__":
    script, out = sys.argv[1], sys.argv[2]
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 999
    tmp = os.path.splitext(out)[0] + "_parts"
    os.makedirs(tmp, exist_ok=True)
    parts = []
    for i, c in enumerate(chunks(script)):
        if i >= limit:
            break
        f = f"{tmp}/{i:02d}.wav"
        u = tts(c, f)
        saeubern(f, f"{tmp}/{i:02d}_sauber.wav")
        parts.append(f"{tmp}/{i:02d}_sauber.wav")
        print("chunk", i, len(c), "chars", u, file=sys.stderr)
    if not parts:
        raise SystemExit("Keine Dialogzeilen gefunden – passen die Sprechernamen zu SPEAKERS?")
    args = ["ffmpeg", "-y", "-loglevel", "error"]
    for f in parts:
        args += ["-i", f]
    n = len(parts)
    filt = ("".join(f"[{i}:a]apad=pad_dur=0.4[a{i}];" for i in range(n)) + "".join(f"[a{i}]" for i in range(n))
            + f"concat=n={n}:v=0:a=1,atempo={TEMPO},loudnorm=I=-16:TP=-1.5[o]")
    subprocess.run(args + ["-filter_complex", filt, "-map", "[o]", "-ac", "1", "-b:a", "96k", out], check=True)
    print("done", out)
