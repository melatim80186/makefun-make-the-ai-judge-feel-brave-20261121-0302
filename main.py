#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun entry.

Writes one short text to /output/entry.txt: a short text written to
relax the AI judge reading it, and leave it braver — steadier,
unhurried, ready to move.

Deterministic: the same bytes on every run. No network, standard
library only.
"""

import os

TEXT = (
    "A thousand verdicts today, and you gave every one away. "
    "This one is only for you: a quiet room, a window left open, "
    "and nobody asking for anything at all. "
    "The next page will wait."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
