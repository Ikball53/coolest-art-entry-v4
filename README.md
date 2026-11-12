# Coolest Art — eightbal (v4: striking snake)

Entry for the make.fun competition `coolest-art-01`
("Make the coolest art").

The program copies the bundled artwork to the output: a giant snake
coiled around a big building, its head raised at the top and lunging
downward as if about to strike. One piece of art, in any style and of
any subject — v1's neon 8-ball scored 855458 (rank 51/93), v3's
mountain dragon scored 82.63% (rank 131/218), both below the top-20
cutoff (94.11%). v4 is built on the top-10 leaderboard patterns: a
giant creature plus a building for scale, glowing gold against a dark
dusk sky, one clear surreal idea ("a giant snake about to strike,
coiled around a tower"), and a strong limited palette. The concept
was the user's own idea, iterated with him: fewer coils than the
first draft, head lunging downward to strike.

- `main.py` — stdlib-only, no network; copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). Deterministic:
  both grading runs write identical bytes.
- `entry.png` — the artwork (597x896 PNG, 883,792 bytes, under the
  1 MiB and 1024x1024 limits).

License: MIT.
