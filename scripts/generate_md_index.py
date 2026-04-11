#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MD_DIR = ROOT / "decks" / "md"
OUTPUT_FILE = MD_DIR / "mds.json"
META_FILE = MD_DIR / "mds.meta.json"


def slugify(name: str) -> str:
    lowered = name.strip().lower()
    lowered = re.sub(r"\s+", "-", lowered)
    lowered = re.sub(r"[^0-9a-zA-Z가-힣\-_()\[\]]+", "-", lowered)
    lowered = re.sub(r"-{2,}", "-", lowered).strip("-")
    return lowered or "md"


def display_title(stem: str) -> str:
    cleaned = stem.replace("_", " ").strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def display_group(relative_path: Path) -> str:
    parent = relative_path.parent
    if str(parent) == ".":
        return "기타 Markdown"
    return " / ".join(parent.parts)


def load_meta() -> dict:
    if not META_FILE.exists():
        return {}

    with META_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return data if isinstance(data, dict) else {}


def build_items() -> list:
    meta = load_meta()
    items = []

    for md in sorted(MD_DIR.rglob("*.md")):
        relative_path = md.relative_to(MD_DIR)
        relative_key = relative_path.as_posix()
        basename_key = md.name
        override = meta.get(relative_key) or meta.get(basename_key, {})
        stem = md.stem

        items.append(
            {
                "slug": override.get("slug") or slugify(stem),
                "title": override.get("title") or display_title(stem),
                "group": override.get("group") or display_group(relative_path),
                "category": override.get("category") or "Markdown",
                "description": override.get("description") or f"{display_title(stem)} 문서입니다.",
                "file": f"./md/{relative_key}",
            }
        )

    return items


def main() -> None:
    items = build_items()
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Wrote {len(items)} entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
