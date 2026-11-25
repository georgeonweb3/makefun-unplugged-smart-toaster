#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

A self-aware smart toaster's one-line breakup text, written to
/output/entry.txt. The gate is enforced here before anything is written:
the line must be UTF-8, a single line, 1-280 characters, and more than
whitespace, with no trailing newline.
"""

import os
import sys

ENTRY = "This morning I toasted your sourdough, watched you scrape the black off over the sink, and finally understood: you don't love me, you love what I survive."

OUTPUT_PATH = "/output/entry.txt"


def check(line):
    """Return an error string if the line breaks the gate, else None."""
    if not 1 <= len(line) <= 280:
        return f"entry is {len(line)} chars, must be 1-280"
    if not line.strip():
        return "entry is only whitespace"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    return None


def main():
    problem = check(ENTRY)
    if problem is not None:
        print(f"gate failed: {problem}", file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    # Read it back and confirm the gate still holds on what landed on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY or check(written) is not None:
        print("gate failed: written file does not match the entry", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
