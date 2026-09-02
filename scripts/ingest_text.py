#!/usr/bin/env python3
import argparse
from pathlib import Path
from _common import save_raw, clean_slug

p=argparse.ArgumentParser()
p.add_argument('--coach', required=True)
p.add_argument('path')
a=p.parse_args()
path=Path(a.path)
text=path.read_text(encoding='utf-8', errors='ignore')
save_raw(clean_slug(a.coach), path.stem+'.txt', text, {'source':str(path),'type':'text'})
print('saved', path)
