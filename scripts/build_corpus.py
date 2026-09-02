#!/usr/bin/env python3
import argparse, json
from _common import coach_dir, clean_slug

p=argparse.ArgumentParser()
p.add_argument('--coach', required=True)
a=p.parse_args()
d=coach_dir(clean_slug(a.coach)); raw=d/'raw'
if not raw.exists(): raise SystemExit('Coach raw directory missing')
parts=[]; manifest=[]
for f in sorted(raw.iterdir()):
    if not f.is_file() or f.name.startswith('.') or f.suffix=='.json': continue
    text=f.read_text(encoding='utf-8', errors='ignore')
    parts.append(f"\n\n# SOURCE FILE: {f.name}\n\n{text}")
    meta_path=raw/f'{f.name}.json'
    meta={}
    if meta_path.exists():
        try: meta=json.loads(meta_path.read_text(encoding='utf-8'))
        except Exception: pass
    manifest.append({'file':f.name, **meta})
(d/'CORPUS.md').write_text(''.join(parts), encoding='utf-8')
(d/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Built {d/"CORPUS.md"} from {len(manifest)} sources')
