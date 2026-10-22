"""Folge in den Feed aufnehmen.

Aufruf im Repo-Root:
  python3 tools/publish.py <nr> <roh-mp3> "<Titel>" "<Beschreibung>"

- wandelt die MP3 in 64 kbit/s Mono um und legt sie unter episodes/folge-NNN.mp3 ab
- trägt die Folge in episodes.json ein (Datum = jetzt)
- hält nur die letzten 30 Folgen als MP3 vor (ältere MP3s werden gelöscht, Skripte bleiben)
- baut feed.xml neu
"""
import json, os, subprocess, sys
from datetime import datetime
from zoneinfo import ZoneInfo

KEEP = 30
nr, raw, title, desc = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
out = f"episodes/folge-{nr:03d}.mp3"
os.makedirs("episodes", exist_ok=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-ac", "1", "-b:a", "64k",
                "-id3v2_version", "3", "-metadata", f"title={title}", "-metadata", "artist=Klöbels KI Podcast", out], check=True)

eps = json.load(open("episodes.json", encoding="utf-8"))
eps = [e for e in eps if e["nr"] != nr]
eps.append({"nr": nr, "title": title, "description": desc, "file": out,
            "date": datetime.now(ZoneInfo("Europe/Berlin")).replace(microsecond=0).isoformat()})
eps.sort(key=lambda e: e["nr"])
for e in eps[:-KEEP]:
    if os.path.exists(e["file"]):
        os.remove(e["file"])
eps = eps[-KEEP:]
json.dump(eps, open("episodes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
subprocess.run([sys.executable, "tools/build_feed.py"], check=True)
print("veröffentlicht:", out)
