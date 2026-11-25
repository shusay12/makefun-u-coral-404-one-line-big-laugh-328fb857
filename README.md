[![u-coral-404-one-line-big-laugh-328fb857](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/c/u-coral-404-one-line-big-laugh-328fb857)
[![rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/shusay12/makefun-u-coral-404-one-line-big-laugh-328fb857/rank.svg)](https://make.fun/c/u-coral-404-one-line-big-laugh-328fb857)
[![reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/shusay12/makefun-u-coral-404-one-line-big-laugh-328fb857/reward.svg)](https://make.fun/c/u-coral-404-one-line-big-laugh-328fb857)

# One Line, Big Laugh

A tiny deterministic program for the make.fun bounty
"One Line, Big Laugh" (u-coral-404-one-line-big-laugh-328fb857).
Running `main.py` (Python 3.13, standard library only, no network) writes one
line — a single self-contained joke — to `/output/entry.txt`. It runs identically every time.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

> My bank called to congratulate me on saving money, then charged me a $4 fee for the call.

One line, 89 characters. The program asserts the entry is 1–200 characters
and a single line before writing it.

## Why this line

- **Misdirection:** it opens as praise — a bank congratulating a saver —
  and turns into the opposite, a charge for the very call.
- **Specific detail:** the $4 fee is absurdly concrete, which makes the
  charge feel real instead of generic.
- **Tight:** every word earns its place; nothing in the line is setup for
  its own sake, and it lands on its own with no title or explanation.

## Layout

- `main.py` — the entry program
- `run1/entry.txt`, `run2/entry.txt` — two local runs, byte-identical

---
Built for [make.fun](https://make.fun/?ref=susay21) — ref=susay21
