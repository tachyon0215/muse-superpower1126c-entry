#!/usr/bin/env python3
"""Write the worst superpower entry to entry.txt.

Competition: Worst Superpower (1-140 chars, single line; the power
must be genuinely useless - not a curse, not secretly useful - and
unexpected, avoiding stock gags like invisibility while unwatched).
Four candidates were drafted and compared:
A) "I can teleport exactly one inch to the left, but only while
   asleep, and I wake up exactly where the inch mattered yesterday."
B) "Perfect recall of every Wi-Fi password I have ever typed, in
   hotels I will never visit again, read aloud only in a whisper."
C) "I can hear what furniture is thinking, and it is all just a long,
   patient scream about being sat on."
D) "I can shrink any queue by one person, provided that person is me
   leaving it."
Selected D: the power is perfectly formed and perfectly useless - it
works every time and achieves nothing, since the queue only shrinks
by losing the one person who wanted it shorter. It is concrete, easy
to picture in use, and clear in one reading. A needs untangling; B is
a memory feat that could plausibly help someone once; C reads as a
curse wearing a power's costume.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "I can shrink any queue by one person, provided that person is me leaving it."
TEXT = LINE + "\n"
MAX_CHARS = 140


def validate(text: str) -> None:
    # Repair revision: the checks below reject padded or double-spaced
    # lines, so the printed entry is exactly the selected one-liner.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
