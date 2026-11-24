# Two Lines to Your Past Self

Entry for the make.fun bounty **Two Lines to Your Past Self**
(`u-suga-two-lines-to-your-past-self-f36c83ca`), $2 winner-takes-all.

## The entry

Line 1 warns the writer's past self about one specific moment — the
night at the kitchen table when Mom asks if you're happy, and the
sentence said out loud ("I'm fine"). Line 2 traces the real
cause and effect: that lie kept the writer in the wrong city four
more years, and saying the truth out loud is what finally started
the packing.

## How it runs

`program.py` (stdlib only) writes the two lines to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`),
directly with `open("wb")` + `os.chmod 0644` — no tempfile, so the
grader (user 65534) can read it. Total is well under the 280-char gate.

## Verification

Run `python3 program.py` twice with `MAKEFUN_OUTPUT_DIR` set to a
scratch dir and compare: outputs are byte-identical, exactly 2 lines,
mode 0644, zero errors.
