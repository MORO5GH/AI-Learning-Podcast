"""Folge in den Feed einer Sendung aufnehmen.

Aufruf im Repo-Root:
  python3 tools/publish.py [--show news] <nr> <roh-mp3> "<Titel>" "<Beschreibung>"

- wandelt die MP3 in 64 kbit/s Mono um und legt sie unter <sendung>/episodes/<präfix>-NNN.mp3 ab
- trägt die Folge in <sendung>/episodes.json ein (Datum = jetzt)
- hält nur die letzten 30 Folgen als MP3 vor (ältere MP3s werden gelöscht, Skripte bleiben)
- baut <sendung>/feed.xml neu
Ohne --show: Lern-Podcast (Repo-Root).
"""
import json, os, subprocess, sys
from datetime import datetime
from zoneinfo import ZoneInfo

KEEP = 30
args = sys.argv[1:]
show_dir = "."
if args and args[0] == "--show":
    show_dir, args = args[1], args[2:]
nr, raw, title, desc = int(args[0]), args[1], args[2], args[3]
cfg = json.load(open(os.path.join(show_dir, "show.json"), encoding="utf-8"))
rel = f"episodes/{cfg['file_prefix']}-{nr:03d}.mp3"
out = os.path.join(show_dir, rel)
os.makedirs(os.path.dirname(out), exist_ok=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-ac", "1", "-b:a", "64k",
                "-id3v2_version", "3", "-metadata", f"title={title}", "-metadata", f"artist={cfg['author']}", out],
               check=True)

ep_file = os.path.join(show_dir, "episodes.json")
eps = json.load(open(ep_file, encoding="utf-8"))
eps = [e for e in eps if e["nr"] != nr]
eps.append({"nr": nr, "title": title, "description": desc, "file": rel,
            "date": datetime.now(ZoneInfo("Europe/Berlin")).replace(microsecond=0).isoformat()})
eps.sort(key=lambda e: e["nr"])
for e in eps[:-KEEP]:
    p = os.path.join(show_dir, e["file"])
    if os.path.exists(p):
        os.remove(p)
eps = eps[-KEEP:]
json.dump(eps, open(ep_file, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
subprocess.run([sys.executable, "tools/build_feed.py", show_dir], check=True)
print("veröffentlicht:", out)
