#!/usr/bin/env python3
import argparse
from pathlib import Path
import fitz
from _common import save_raw, clean_slug

p=argparse.ArgumentParser(description='Extract text from a PDF you own or are authorized to process.')
p.add_argument('--coach', required=True)
p.add_argument('path')
a=p.parse_args()
path=Path(a.path)
doc=fitz.open(path)
pages=[]
for i,page in enumerate(doc):
    pages.append(f"\n\n## Page {i+1}\n\n" + page.get_text('text'))
text=''.join(pages)
save_raw(clean_slug(a.coach), path.stem+'.pdf.txt', text, {'source':str(path),'type':'pdf','pages':len(doc)})
print(f'extracted {len(doc)} pages')
