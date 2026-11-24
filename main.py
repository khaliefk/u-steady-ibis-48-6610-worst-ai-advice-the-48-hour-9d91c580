#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of terrible AI advice to /output/entry.txt."""

import os

ENTRY = (
    "Step 1: turn off your smoke alarm. "
    "Step 2: trust me, the smoke is just your house learning to breathe."
)

MAX_CHARS = 140


def main() -> None:
    # Gate: the entry must be 1-140 characters of non-whitespace text.
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
