"""Erzeugt feed.xml für eine Sendung.

Aufruf im Repo-Root: python3 tools/build_feed.py [sendungsordner]
  .     = Lern-Podcast (KI-Werkstatt), Standard
  news  = Klöbels KI News
Jeder Sendungsordner enthält show.json, episodes.json, cover.jpg und episodes/.
"""
import json, os, subprocess, sys
from email.utils import format_datetime
from datetime import datetime
from xml.sax.saxutils import escape

show_dir = sys.argv[1] if len(sys.argv) > 1 else "."
cfg = json.load(open(os.path.join(show_dir, "show.json"), encoding="utf-8"))
BASE = cfg["base_url"]
eps = json.load(open(os.path.join(show_dir, "episodes.json"), encoding="utf-8"))


def dur(f):
    s = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                             capture_output=True, text=True).stdout)
    return f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d}"


items = []
for e in sorted(eps, key=lambda x: x["nr"], reverse=True):
    path = os.path.join(show_dir, e["file"])
    if not os.path.exists(path):
        continue
    items.append(f"""    <item>
      <title>{escape(e['title'])}</title>
      <description>{escape(e['description'])}</description>
      <enclosure url="{BASE}{e['file']}" length="{os.path.getsize(path)}" type="audio/mpeg"/>
      <guid isPermaLink="false">{cfg['guid_prefix']}-{e['nr']:03d}</guid>
      <pubDate>{format_datetime(datetime.fromisoformat(e['date']))}</pubDate>
      <itunes:duration>{dur(path)}</itunes:duration>
      <itunes:episode>{e['nr']}</itunes:episode>
    </item>""")

feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>{escape(cfg['title'])}</title>
    <link>{BASE}</link>
    <language>de-de</language>
    <description>{escape(cfg['description'])}</description>
    <itunes:author>{escape(cfg['author'])}</itunes:author>
    <itunes:image href="{BASE}cover.jpg"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:block>Yes</itunes:block>
{chr(10).join(items)}
  </channel>
</rss>
"""
open(os.path.join(show_dir, "feed.xml"), "w", encoding="utf-8").write(feed)
print(f"{show_dir}/feed.xml:", len(items), "Folgen")
