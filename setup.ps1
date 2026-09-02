param(
  [ValidateSet("claude", "codex", "both")]
  [string]$Harness = "both",
  [string]$Coach = "my-coach"
)

$ErrorActionPreference = "Stop"
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/new_coach.py --slug $Coach --name $Coach --domain general --force

if ($Harness -eq "claude" -or $Harness -eq "both") {
  New-Item -ItemType Directory -Force -Path .claude\skills\icon-coach | Out-Null
  Copy-Item -Recurse -Force skills\icon-coach\* .claude\skills\icon-coach\
  Write-Host "Installed Claude Code project skill -> .claude\skills\icon-coach"
}

if ($Harness -eq "codex" -or $Harness -eq "both") {
  $base = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
  $dest = Join-Path $base "skills\icon-coach"
  New-Item -ItemType Directory -Force -Path $dest | Out-Null
  Copy-Item -Recurse -Force skills\icon-coach\* $dest\
  Write-Host "Installed Codex user skill -> $dest"
}

if (-not (Test-Path .env)) { Copy-Item .env.example .env }
Write-Host "Ready. Add sources, build the corpus, then open Claude Code or Codex."
