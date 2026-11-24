#!/usr/bin/env python3
"""Two Lines to Your Past Self — program/v1 entry.

Writes exactly two lines to entry.txt: line 1 warns the writer's past
self about one specific moment; line 2 says why that moment mattered
and what changed because of it. Total must stay within 1-280 chars.
"""
import os

LINE_1 = "At the kitchen table the night Mom asks if you're happy, don't say 'I'm fine' \u2014 tell her the truth."
LINE_2 = "That lie kept you in the wrong city four more years, and the night you finally said it out loud, you started packing."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE_1 + "\n" + LINE_2 + "\n"
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
