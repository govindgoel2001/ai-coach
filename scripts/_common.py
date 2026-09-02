from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parents[1]
COACHES = ROOT / "coaches"

def clean_slug(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9_-]+", "-", s.strip().lower()).strip("-")
    if not s:
        raise ValueError("Coach slug is empty")
    return s

def coach_dir(slug: str) -> Path:
    return COACHES / clean_slug(slug)

def save_raw(slug: str, filename: str, text: str, meta: dict | None = None):
    d = coach_dir(slug)
    raw = d / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    (raw / filename).write_text(text, encoding="utf-8")
    if meta is not None:
        (raw / f"{filename}.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
