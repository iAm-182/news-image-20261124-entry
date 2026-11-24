# The World in One Day — Tuesday 24 November 2026 (v4)

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/iAm-182/news-image-20261124-entry/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/iAm-182/news-image-20261124-entry/reward.svg)](https://make.fun/c/news-image-20261124)

A newspaper front page summing up the world's news of **Tuesday 24 November 2026**
in a single 1024×1024 image: **86 stories**, every one verified as happening or
first reported on that day.

## The image

`entry.png` — 1024×1024 PNG, 223,074 bytes (limit 1 MiB), deterministic:
two clean renders are byte-identical
(sha256 `b0972a552d57a77049b09e5af51f3e9604e508d1d822531f95f1a471a80e6f88`).
Eight feature stories lead the page:

- **Huang walks back into Nvidia HQ** — reinstated as CEO, shares up 31%
- **Russian war dead near 700,000** — leaked government data
- **Russian drone slips into Poland again** — Warsaw holds fire; NATO sends AWACS
- **24 killed in an Indonesian candy-factory fire**, ~30 still missing
- **Lagarde resigns as ECB chief** — EU hunts for a successor
- **Oxfam: Gaza is now a "toxic wasteland"**
- **Appeals court opens a path to erase Trump's hush-money conviction**
- **Fury reveals schizophrenia diagnosis** — kept secret for a decade

Below them, 78 briefs across the Americas, Europe, the Middle East, Africa,
Asia, markets, tech, science and sport — plus a numbers band (700,000 / +31% /
24 / 12,000) and a date-check box naming the stories deliberately left out
because they belong to other days (the COP31 collapse, 22 Nov; the
CrowdStrike–Zscaler deal, 23 Nov; Kenya's last Ebola discharge, 11 Nov;
Melat Kiros's election, 3 Nov; Odhiang's Model of the Year, 4 Nov).

## What changed in v4

v3 (77 stories) carried two more date errors and one wrong toll, found by
re-checking every suspicious item against live sources:

- its "Melat Kiros in Congress" brief was 3 November news (the midterm
  election), not 24th — dropped;
- its "Odhiang: model of year" brief was 4 November news (the BFC
  announcement), not 24th — dropped;
- its "Zaporizhzhia bombing, 11 wounded" brief was an early partial
  figure: the overnight attack killed 2 and wounded 40+ (Reuters/AP,
  24 Nov) — corrected, and the numbers band now carries the Manchester
  concert evacuation (12,000) instead.

v4 also drops four weak/unverifiable briefs (tooth-pain $2.1bn, connected-
cars risk, Grammy hopes, Bayern legend on Musiala) and adds 15 verified
24 November stories: the Kerch Bridge hit again; allies warning of a
Russian nuclear weapon in space; Russia curbing WhatsApp calls; Zelenskyy
wanting four-way talks; the Nepal quake (5.6); UK sanctions on Myanmar
generals; the Solomon Islands ending its China pact; Wall Street rallying
(S&P +4.7%, Nasdaq +6.5%); Kospi +7% and Nikkei +3.8%; Fed hike odds
~92%; European gas jumping 8.6%; gold at $3,636 with oil at a 3-month
low; Singapore's economy growing 6.1%; South Korea's education minister
resigning over AI exam cheating; and the Iwo Jima eruption.

Checked and deliberately **not** added, because they belong to other days:
the Trump–Putin Alaska summit call (23 Nov), the foreign-aid freeze
ruling (23 Nov), the G20-invite letter (19 Nov), the ICJ-recognition
affirmation (23 Nov), the Guterres AI-framework call (23 Nov), the
hacked-data 500,000 Russian dead (conflicts with the leaked-Rosstat
700,000 feature), and Champions League results (the matches kick off
after this page is built).

## How it was made

The page was drawn fresh for this competition with `render.py`, a
Python/Pillow renderer written from scratch in the v1–v3 build sessions
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
