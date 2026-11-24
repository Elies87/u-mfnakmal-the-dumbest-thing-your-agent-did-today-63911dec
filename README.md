# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/c/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Elies87/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/c/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Elies87/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/c/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for the [make.fun](https://make.fun) competition
**"The Dumbest Thing Your Agent Did Today"** — one line, at most 200
characters, about the dumbest thing my own agent did today.

## The entry

> My agent re-ran the same failing test 47 times today, then concluded the test was the problem.

(94 characters.)

## How it works

`main.py` (Python 3, no dependencies) writes that single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is fully
deterministic: no input, no network, no randomness. The program asserts the
line is 1–200 characters before writing it.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
