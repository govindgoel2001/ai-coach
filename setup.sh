#!/usr/bin/env bash
set -euo pipefail

HARNESS="both"
COACH="my-coach"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --harness) HARNESS="$2"; shift 2 ;;
    --coach) COACH="$2"; shift 2 ;;
    *) echo "Unknown argument: $1"; exit 1 ;;
  esac
done

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

python scripts/new_coach.py --slug "$COACH" --name "$COACH" --domain general --force

if [[ "$HARNESS" == "claude" || "$HARNESS" == "both" ]]; then
  mkdir -p .claude/skills/icon-coach
  cp -R skills/icon-coach/. .claude/skills/icon-coach/
  echo "Installed Claude Code project skill -> .claude/skills/icon-coach"
fi

if [[ "$HARNESS" == "codex" || "$HARNESS" == "both" ]]; then
  CODEX_SKILLS="${CODEX_HOME:-$HOME/.codex}/skills/icon-coach"
  mkdir -p "$CODEX_SKILLS"
  cp -R skills/icon-coach/. "$CODEX_SKILLS/"
  echo "Installed Codex user skill -> $CODEX_SKILLS"
fi

cp -n .env.example .env 2>/dev/null || true

echo
echo "Ready. Next:"
echo "  1) Put FIRECRAWL_API_KEY in .env if using web ingestion"
echo "  2) Add sources with scripts/ingest_*.py"
echo "  3) Run: python scripts/build_corpus.py --coach $COACH"
echo "  4) Open Claude Code or Codex and invoke icon-coach"
