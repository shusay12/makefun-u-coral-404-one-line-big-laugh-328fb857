#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun competition
u-coral-404-one-line-big-laugh-328fb857.

Writes one line (1-200 chars) to /output/entry.txt: a single self-contained
joke. Python 3.13 stdlib only, no network, deterministic output.

Why this line: it opens as praise (the bank congratulating a saver) and
turns into the opposite (the bank charging for the very call) — a
misdirection in one breath, with one absurdly specific detail ($4) to make
the fee feel real, and no word the joke does not need.
"""

import os

ENTRY = (
    "My bank called to congratulate me on saving money, "
    "then charged me a $4 fee for the call."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
