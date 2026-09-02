#!/usr/bin/env bash
set -euo pipefail
python -m pip install --upgrade pip
pip install -r requirements.txt
cp -n .env.example .env 2>/dev/null || true
python scripts/new_coach.py --slug my-coach --name "My Coach" --domain general --force
mkdir -p .claude/skills/icon-coach
cp -R skills/icon-coach/. .claude/skills/icon-coach/
echo "Universal AI Coach workspace ready."
echo "Next: add FIRECRAWL_API_KEY to .env if needed, ingest sources, then build the corpus."
