#!/usr/bin/env python3
import argparse
from _common import ROOT, coach_dir, clean_slug

p = argparse.ArgumentParser()
p.add_argument('--slug', required=True)
p.add_argument('--name', required=True)
p.add_argument('--domain', default='general')
p.add_argument('--inspired-by', default='Publicly available source material')
p.add_argument('--force', action='store_true')
a = p.parse_args()
slug = clean_slug(a.slug)
d = coach_dir(slug)
if d.exists() and not a.force:
    raise SystemExit(f"Coach exists: {d}. Use --force to overwrite templates only.")
d.mkdir(parents=True, exist_ok=True)
(d/'raw').mkdir(exist_ok=True)
(d/'data').mkdir(exist_ok=True)
(d/'raw'/'.gitkeep').touch()
(d/'data'/'.gitkeep').touch()

repls = {
    '{{NAME}}': a.name,
    '{{INSPIRED_BY}}': a.inspired_by,
    '{{DOMAIN}}': a.domain,
    '{{MISSION}}': f'Help me make better {a.domain} decisions using documented frameworks and my current context.'
}
for name in ['PROFILE.md','FRAMEWORKS.md','EVIDENCE.md','TOOL_MAP.md']:
    src = ROOT/'templates'/name
    text = src.read_text(encoding='utf-8')
    for k,v in repls.items(): text = text.replace(k,v)
    dst = d/name
    if not dst.exists() or a.force:
        dst.write_text(text, encoding='utf-8')
print(d)
