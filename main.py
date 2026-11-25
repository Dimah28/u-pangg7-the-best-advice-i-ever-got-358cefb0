#!/usr/bin/env python3
"""Best Advice entry.

Writes one sentence about the best advice I ever received to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, no network
access, deterministic: the same sentence on every run.
"""

import os
import sys

SENTENCE = (
    "When I was twelve, my grandmother told me to learn the name of "
    "the man who swept our street, because one day you will need a "
    "friend who owes you nothing."
)


def main() -> int:
    text = SENTENCE
    if not 1 <= len(text) <= 200:
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if any(ord(c) < 0x20 or ord(c) == 0x7F for c in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
