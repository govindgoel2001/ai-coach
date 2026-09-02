# Connectors

The coach can work with live tools or exported files. Start simple, then upgrade.

## File mode — easiest / safest

Put user-authorized data into `coaches/<slug>/data/` and describe it in `TOOL_MAP.md`.

Examples included:
- `health.example.csv`
- `portfolio.example.csv`
- `business.example.csv`

## API / MCP mode

If Claude Code or Codex already has an MCP/tool connection, do not duplicate it here. Add the tool name, fields, freshness, and permissions to `TOOL_MAP.md` so the skill knows when to use it.

Recommended pattern:

```text
coach question
 -> skill selects framework
 -> tool retrieves current user data
 -> model analyzes only relevant fields
 -> recommendation + scorecard
 -> write action requires approval
```

For health and finance, default to read-only and educational analysis.
