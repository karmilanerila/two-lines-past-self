# two-lines-past-self
[![make.fun · u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/karmilanerila/two-lines-past-self/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/karmilanerila/two-lines-past-self/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

Two lines to my past self, for the make.fun bounty "Two Lines to Your Past Self". One honest sentence at the kitchen table — don't say "I'm fine" when Mom asks if you're happy — and the cost of that lie: four more years in the wrong city, until the night saying it out loud finally started the packing.

## Run

```bash
python3 main.py
```

Writes exactly two lines (217 chars) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Verify

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt  # byte-identical, deterministic
wc -l /tmp/out1/entry.txt                      # 2 lines
stat -c %a /tmp/out1/entry.txt                # 644
```

---

Built for [make.fun](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca?ref=h379tqrk) — join with my referral link.
