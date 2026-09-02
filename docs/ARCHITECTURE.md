# Architecture

## Why a skill instead of one giant prompt

A giant prompt mixes biography, source material, style, tools, and user data into one context blob. This template splits them:

- `PROFILE.md`: stable coaching role and boundaries
- `FRAMEWORKS.md`: compressed reusable decision rules
- `EVIDENCE.md`: source mapping
- `TOOL_MAP.md`: live/user data contract
- `CORPUS.md`: deep source layer loaded only when needed

That makes the coach cheaper to run, easier to audit, and easier to update.

## Retrieval strategy

1. Load profile and tool map.
2. Select the relevant framework.
3. Fetch current user data if a connected tool is relevant.
4. Read corpus/evidence only to verify or deepen a claim.
5. Return diagnosis -> action -> scorecard -> review.

## Installation conventions researched

Claude Code official plugin examples document project skills at `.claude/skills/<name>/SKILL.md`.

Codex's current skill installer uses `$CODEX_HOME/skills` as the default destination (normally `~/.codex/skills`). OpenAI is evolving the skills/plugin ecosystem, so keep the source skill folder portable and update the installer if conventions change.
