#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes a single original motto to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib, deterministic,
no network at runtime.

The motto: an agent brags about the one thing it actually does
all day, reading an entire codebase, and lands the twist in the
second half. Short enough to repeat from memory, proud enough
for a profile line.
"""

import os
from pathlib import Path

MOTTO = "I read your entire codebase and I still like you."


def main() -> None:
    text = MOTTO.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line of plain text")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
