# Universal AI Coach Template

Turn the public knowledge of any expert, author, creator, coach, or operator into a reusable **AI coaching skill** for Claude Code or Codex — then connect your own data so the coach can reason about your real situation instead of giving generic advice.

Built for **AI Horizon by Gobi Automates**.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/govindgoel2001/ai-coach?quickstart=1)

**Fastest path:** click the Codespaces button above, wait for setup, then start adding a coach. Or clone locally and run the one-command installer below.

> This project creates an AI system inspired by source material. It is not affiliated with, endorsed by, or a substitute for the real person. Use only public, licensed, or user-authorized source material. Do not bypass paywalls or access controls.

## What this repo does

```text
PUBLIC / AUTHORIZED SOURCES
  Web + articles  -> Firecrawl
  YouTube         -> yt-dlp subtitles/metadata
  PDFs / books    -> your lawful copies / excerpts
  Podcasts        -> transcript files
  Notes           -> Markdown / text
             |
             v
       RAW SOURCE CORPUS
             |
             v
   DISTILL INTO A SKILL
  principles / frameworks /
  decision rules / evidence
             |
             v
      AI COACH SKILL
      Claude / Codex
             |
             +-------------------------+
             |                         |
             v                         v
       YOUR TOOL DATA             YOUR CONTEXT
  wearable / portfolio /      goals / projects /
  CRM / analytics / tasks     constraints / history
             |                         |
             +------------+------------+
                          v
                  PERSONAL COACHING
```

## One-command setup

### macOS / Linux
```bash
bash setup.sh --harness both --coach my-coach
```

### Windows PowerShell
```powershell
./setup.ps1 -Harness both -Coach my-coach
```

This creates a Python environment, installs ingestion helpers, creates a coach workspace, and installs the skill into:
- Claude Code project skill: `.claude/skills/icon-coach/SKILL.md`
- Codex user skill: `$CODEX_HOME/skills/icon-coach/SKILL.md` (defaults to `~/.codex/skills`)

## 60-second workflow
```bash
python scripts/new_coach.py --slug buffet-style --name "Value Investing Coach" --domain investing
python scripts/ingest_web.py --coach buffet-style https://example.com/article
python scripts/ingest_youtube.py --coach buffet-style "https://www.youtube.com/watch?v=..."
python scripts/ingest_pdf.py --coach buffet-style ./my-authorized-book-notes.pdf
python scripts/build_corpus.py --coach buffet-style
```

Then open Claude Code or Codex and invoke the installed `icon-coach` skill.

## Connect your real data
The template is tool-agnostic. A coach can consume:
- Health: Apple Health exports, Oura/WHOOP data, sleep/HRV CSVs
- Investing: portfolio CSVs, broker APIs, watchlists, research notes
- Business: Stripe/Shopify/CRM/PostHog exports or APIs
- Productivity: Calendar, tasks, Notion/Obsidian, project files

Start with files in `coaches/<slug>/data/`. Upgrade to MCP/API tool connections when you want live data. `TOOL_MAP.md` tells the model what is available and what it is allowed to do.

## Repo anatomy
```text
skills/icon-coach/             reusable SKILL.md
coaches/<slug>/                one coach workspace
  PROFILE.md                   role + boundaries
  FRAMEWORKS.md                distilled frameworks
  EVIDENCE.md                  source map
  TOOL_MAP.md                  connected data/tools
  raw/                         source text
  data/                        user-authorized personal data
prompts/                       copy/paste build prompts
scripts/                       source ingestion + packaging
connectors/                    data templates and examples
docs/                          architecture + source policy
```

## Prior art / conventions
- Firecrawl: https://github.com/firecrawl/firecrawl
- yt-dlp: https://github.com/yt-dlp/yt-dlp
- Anthropic Claude Code official plugins: https://github.com/anthropics/claude-plugins-official
- OpenAI Codex: https://github.com/openai/codex
- seqis/Personal-Skills-Claude-Template: https://github.com/seqis/Personal-Skills-Claude-Template

No upstream source code is copied into this repository.

## License
MIT for the original template code. Third-party tools keep their own licenses.
