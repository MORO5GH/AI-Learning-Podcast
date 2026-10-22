"""Erzeugt feed.xml aus episodes.json. Aufruf: python3 tools/build_feed.py (im Repo-Root)."""
import json, os, subprocess
from email.utils import format_datetime
from datetime import datetime
from xml.sax.saxutils import escape
BASE="https://moro5gh.github.io/AI-Learning-Podcast/"
eps=json.load(open("episodes.json",encoding="utf-8"))
def dur(f):
    s=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)
    return f"{int(s//3600):02d}:{int(s%3600//60):02d}:{int(s%60):02d}"
items=[]
for e in sorted(eps,key=lambda x:x["nr"],reverse=True):
    if not os.path.exists(e["file"]): continue
    items.append(f"""    <item>
      <title>{escape(e['title'])}</title>
      <description>{escape(e['description'])}</description>
      <enclosure url="{BASE}{e['file']}" length="{os.path.getsize(e['file'])}" type="audio/mpeg"/>
      <guid isPermaLink="false">ki-werkstatt-{e['nr']:03d}</guid>
      <pubDate>{format_datetime(datetime.fromisoformat(e['date']))}</pubDate>
      <itunes:duration>{dur(e['file'])}</itunes:duration>
      <itunes:episode>{e['nr']}</itunes:episode>
    </item>""")
feed=f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>KI-Werkstatt</title>
    <link>{BASE}</link>
    <language>de-de</language>
    <description>Persönlicher Lern-Podcast: jeden Tag eine Folge zu Prompting, KI-Tools und Agenten.</description>
    <itunes:author>KI-Werkstatt</itunes:author>
    <itunes:image href="{BASE}cover.jpg"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:block>Yes</itunes:block>
{chr(10).join(items)}
  </channel>
</rss>
"""
open("feed.xml","w",encoding="utf-8").write(feed); print("feed.xml:",len(items),"Folgen")
