#!/usr/bin/env python3
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'dist'
out.mkdir(exist_ok=True)
base=out/'icon-coach-skill'
zip_path=shutil.make_archive(str(base), 'zip', root_dir=ROOT/'skills', base_dir='icon-coach')
print(zip_path)
