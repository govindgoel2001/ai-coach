# Master coach-builder prompt

Build an AI coaching skill inspired by the documented public work of **<PERSON>**, focused on **<DOMAIN>**.

Do not pretend to be <PERSON>. Instead, extract and operationalize their documented principles, frameworks, heuristics, decision rules, recurring questions, and failure modes.

Use the source corpus in `coaches/<SLUG>/CORPUS.md` plus the source manifest. Create/update:

- `PROFILE.md` — mission, role, boundaries, coaching style
- `FRAMEWORKS.md` — reusable frameworks with triggers and decision rules
- `EVIDENCE.md` — source map for every important principle
- `TOOL_MAP.md` — what user data the coach can read and what actions require approval

Compress aggressively. The goal is not a biography or giant prompt. The goal is a reusable skill that loads only the knowledge needed for the current problem.
