"""Two Lines to Your Past Self — make.fun entry.

Writes exactly two lines addressed to my past self to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: same bytes on every run.
"""

import os

LINE_1 = "At the kitchen table the night Mom asks if you're happy, don't say 'I'm fine' \u2014 tell her the truth."
LINE_2 = "That lie kept you in the wrong city four more years, and the night you finally said it out loud, you started packing."

# Single source of truth for the entry: exactly two lines, trailing newline.
ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert len(ENTRY) == 218, "entry must be 217 chars plus trailing newline"
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
