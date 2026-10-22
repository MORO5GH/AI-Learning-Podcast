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
MODEL = os.environ.get("TTS_MODEL", "gemini-3.8-flash-tts")
SPEAKERS = dict(p.split(":") for p in os.environ.get("SPEAKERS", "MIRA:Aoede,JAN:Charon").split(","))
NAMES = {k.upper(): k.capitalize() for k in SPEAKERS}  # MIRA -> Mira


def tts(dialog, out_wav):
    parts = []
    for l in dialog.splitlines():
        sp, t = l.split(":", 1)
        parts.append({"text": t.strip(), "speechMetadata": {"speaker": sp}})
    voices = [{"speaker": NAMES[k.upper()], "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": v}}}
              for k, v in SPEAKERS.items()]
    body = {"contents": [{"role": "user", "parts": parts}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"multiSpeakerVoiceConfig": {"speakerVoiceConfigs": voices}}}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
    for attempt in range(8):
        try:
            d = json.load(urllib.request.urlopen(req, timeout=600))
            break
        except Exception as e:
            err = e.read().decode()[:500] if hasattr(e, "read") else str(e)
            print("retry", attempt, err, file=sys.stderr)
            if "400" in str(e):
                raise SystemExit("TTS bad request")
            time.sleep(min(60 * (attempt + 1), 300))
    else:
        raise SystemExit("TTS failed")
    pcm = b"".join(base64.b64decode(p["inlineData"]["data"])
                   for p in d["candidates"][0]["content"]["parts"] if "inlineData" in p)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", "-", out_wav],
                   input=pcm, check=True)
    return d.get("usageMetadata", {})


def chunks(script, max_chars=4000):
    pat = re.compile(r"^(" + "|".join(NAMES) + r"):")
    lines = [l for l in open(script, encoding="utf-8").read().splitlines() if pat.match(l)]
    lines = [NAMES[l.split(":", 1)[0]] + ":" + l.split(":", 1)[1] for l in lines]
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
        parts.append(f)
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
