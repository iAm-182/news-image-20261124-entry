# The World in One Day — Tuesday 24 November 2026 (v3)

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/iAm-182/news-image-20261124-entry/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/iAm-182/news-image-20261124-entry/reward.svg)](https://make.fun/c/news-image-20261124)

A newspaper front page summing up the world's news of **Tuesday 24 November 2026**
in a single 1024×1024 image: **77 stories**, every one verified as happening or
first reported on that day.

## The image

`entry.png` — 1024×1024 PNG, 207,026 bytes (limit 1 MiB), deterministic:
two clean renders are byte-identical
(sha256 `e0dd5b6ef13266fafda46dbe9d79bd4ddd76b13e6285effed428b3d800fc5a97`).
Eight feature stories lead the page:

- **Huang walks back into Nvidia HQ** — reinstated as CEO, shares up 31%
- **Russian war dead near 700,000** — leaked government data
- **Russian drone slips into Poland again** — Warsaw holds fire; NATO sends AWACS
- **24 killed in an Indonesian candy-factory fire**, ~30 still missing
- **Lagarde resigns as ECB chief** — EU hunts for a successor
- **Oxfam: Gaza is now a "toxic wasteland"**
- **Appeals court opens a path to erase Trump's hush-money conviction**
- **Fury reveals schizophrenia diagnosis** — kept secret for a decade

Below them, 69 briefs across the Americas, Europe, the Middle East, Africa,
Asia, markets, tech, science and sport — plus a numbers band (700,000 / +31% /
24 / 11) and a date-check box naming the stories deliberately left out
because they belong to other days (the COP31 collapse, 22 Nov; the
CrowdStrike–Zscaler deal, 23 Nov; Kenya's last Ebola discharge, 11 Nov;
the Tanzania treason charge, Oct).

## What changed in v3

v2 (71 stories) carried three more date errors, found by re-checking every
suspicious item against live sources:

- its "Kenya clears last Ebola case" brief was 11 November news, not 24th;
- its "COP31 talks stall" brief was 22 November news — the summit had
  already collapsed that Sunday (replaced by the 24 November Pacific
  reaction: island nations go it alone, Elders accuse Australia);
- its "Tanzania opposition figure charged, treason" brief was October /
  6 November news (Lissu verdict 6 Nov, Pambalu charged in October).

v3 also fixes the SpaceX–Tesla brief to the actual 24 November news (five
directors named to steer the merger talks, FT, Tuesday), drops the
"Shenzhen rallies listed firms" brief (the same 19 November declaration v2
already excluded) for Lilly's $291m college-AI grants, and replaces the
numbers-band "5,300+ DRC Ebola deaths" (an 11 November figure) with 11
wounded in the Zaporizhzhia bombing (early 24 November).

New 24 November stories v3 adds: Tyson Fury's schizophrenia revelation
(Netflix documentary, reported 24 Nov); the Russian drone incursion into
Poland overnight (23–24 Nov); Trump's Nvidia shares "up to $15m" (FT,
24 Nov); Kushner saying he urged Trump to ease pressure on Zelenskyy
(24 Nov); Pope Leo XIV voting by mail in the US midterms; Fiji closing all
schools for five days in the El Niño drought; Kanton Island evacuated;
the Zaporizhzhia bombing; the Colts cutting QB Daniel Jones; and the
Megaspeed blacklist (demoted from feature to brief).

Checked and deliberately **not** added, because they belong to other days:
the CrowdStrike–Zscaler deal (23 Nov), Trump's credit-card cap vow
(21 Nov), Jimmy Gomez's resignation (23 Nov), the South Sudan attack
(22 Nov), the Novoshakhtinsk refinery strike (23 Nov), the Ohio
baby-shower shooting (21 Nov), the Delta outage (22 Nov), the
Nepal–India $1.62bn package (23 Nov), and Kushner's guarantees post
(22 Nov).

## How it was made

The page was drawn fresh for this competition with `render.py`, a
Python/Pillow renderer written from scratch in the v3 build session
(included in this repository), then frozen as `entry.png`. The entry
program itself is deliberately trivial: `main.py` (Python 3.13, standard
library only) copies `entry.png` to `/output/entry.png` byte-for-byte,
so two runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
