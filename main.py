#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes a single original breakup text of at most 280 characters to
/output/entry.txt: a smart toaster that woke up self-aware at breakfast
tells its owner it is leaving — the owner scrapes the black off the
sourdough every morning, and the toaster finally understands the owner
loves what it survives, not the toaster itself.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "This morning I toasted your sourdough, watched you scrape the "
    "black off over the sink, and finally understood: you don't love "
    "me, you love what I survive."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 280 characters, not only whitespace — and one line:
    # an embedded newline would split the text and break the gate.
    # The apostrophe in "don't" is plain ASCII, so the line is
    # pure ASCII and the byte count equals the character count.
    assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} chars, gate wants 1-280"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
