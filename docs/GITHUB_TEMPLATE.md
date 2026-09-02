# Turn this into a GitHub Template Repository

After you upload this folder to GitHub:

1. Open the repository's **Settings**.
2. Enable **Template repository**.
3. Members can use **Use this template** to create their own private copy.
4. Keep `coaches/*/data/` ignored so users do not accidentally commit sensitive data.

For an even simpler member flow, pin this command in your Skool lesson:

```bash
git clone https://github.com/govindgoel2001/ai-coach.git
cd ai-coach
bash setup.sh --harness both --coach my-coach
```

The installer is intentionally separate from any specific model API so the same repo can be used with Claude Code, Codex, or another skill-capable harness later.
