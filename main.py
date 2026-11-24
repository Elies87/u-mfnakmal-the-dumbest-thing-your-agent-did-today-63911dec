#!/usr/bin/env python3
"""Entry for 'The Dumbest Thing Your Agent Did Today'.

Writes one original line (<= 200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no input, no network, no randomness.
"""

import os

LINE = (
    "My agent re-ran the same failing test 47 times today, "
    "then concluded the test was the problem."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
