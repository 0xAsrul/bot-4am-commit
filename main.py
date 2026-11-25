#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message (one line, <=200 chars) to /output/entry.txt
and prints the same line to stdout.
"""

import os

LINE = "fix: the bug was code I wrote, reviewed, and approved myself at 3am. I have opened an investigation into myself and I am the prime suspect"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
