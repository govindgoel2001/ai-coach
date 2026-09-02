#!/usr/bin/env python3
import argparse, tempfile
from pathlib import Path
import yt_dlp
from _common import save_raw, clean_slug

p=argparse.ArgumentParser(description='Collect public metadata and available subtitles/transcript files with yt-dlp. Respect rights and platform terms.')
p.add_argument('--coach', required=True)
p.add_argument('url')
a=p.parse_args()
slug=clean_slug(a.coach)
with tempfile.TemporaryDirectory() as td:
    outtmpl=str(Path(td)/'%(id)s.%(ext)s')
    opts={
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en','en-US','en-GB'],
        'subtitlesformat': 'vtt',
        'outtmpl': outtmpl,
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info=ydl.extract_info(a.url, download=True)
    vid=info.get('id','video')
    pieces=[
        f"# {info.get('title','')}\n",
        f"URL: {a.url}\n",
        f"Channel: {info.get('channel') or info.get('uploader') or ''}\n",
        f"Description:\n{info.get('description') or ''}\n"
    ]
    for pth in sorted(Path(td).glob(f'{vid}*.vtt')):
        pieces.append(f"\n## Subtitle file: {pth.name}\n"+pth.read_text(encoding='utf-8', errors='ignore'))
    save_raw(slug, f'{vid}.youtube.txt', '\n'.join(pieces), {
        'source': a.url, 'type':'youtube', 'id':vid, 'title':info.get('title'), 'channel':info.get('channel') or info.get('uploader')
    })
    print('saved', info.get('title', vid))
