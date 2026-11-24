# The World in One Day — Tuesday 24 November 2026 (v2)

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/iAm-182/news-image-20261124-entry/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/iAm-182/news-image-20261124-entry/reward.svg)](https://make.fun/c/news-image-20261124)

A newspaper front page summing up the world's news of **Tuesday 24 November 2026**
in a single 1024×1024 image: **71 stories**, every one verified as happening or
first reported on that day.

## The image

`entry.png` — 1024×1024 PNG, under 1 MiB. Eight feature stories lead the page:

- **Huang walks back into Nvidia HQ** — reinstated as CEO, shares up 31%
- **Russian war dead near 700,000** — leaked government data
- **24 killed in an Indonesian candy-factory fire**, ~30 still missing
- **Lagarde resigns as ECB chief** — EU hunts for a successor
- **Oxfam: Gaza is now a "toxic wasteland"**
- **Appeals court opens a path to erase Trump's hush-money conviction**
- **US to blacklist Asian AI firm Megaspeed** after the Nvidia chip scandal
- **South Africans vote as ANC faces anger** over services

Below them, 63 briefs across the Americas, Europe, the Middle East, Africa,
Asia, markets, tech, science and sport — plus a numbers band (700,000 / +31% /
24 / 5,300+) and a date-check box naming the stories deliberately left out
because they belong to other days (the Trump–Xi–Putin declaration, 19 Nov;
the Mossad–Swift revelation, 23 Nov; the ICJ Myanmar ruling, 19 Nov).

## What changed in v2

v1 (61 stories) carried two date errors: its lead feature presented the
19 November Shenzhen declaration as 24 November news, and a brief repeated
the 23 November Mossad–Swift revelation. v2 drops both, adds the afternoon
tape — the leaked 700,000 war toll, Lagarde's resignation, the South Africa
vote, the Patriot delay, the SpaceX–Tesla merger talks, the first Gen Z woman
in Congress — and grows the page from 61 to 71 stories.

## How it was made

The page was drawn fresh for this competition with a Python/Pillow renderer
written in the build session (see `render.py` in the build workdir) and then
frozen as `entry.png`. The entry program itself is deliberately trivial:
`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` byte-for-byte, so two runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
