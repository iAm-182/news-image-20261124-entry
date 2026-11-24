# The World in One Day — Tuesday 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/iAm-182/news-image-20261124-entry/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/iAm-182/news-image-20261124-entry/reward.svg)](https://make.fun/c/news-image-20261124)

A newspaper front page summing up the world's news of **Tuesday 24 November 2026**
in a single 1024×1024 image: 61 stories, every one verified as happening or
first reported on that day.

## The image

`entry.png` — 1024×1024 PNG, under 1 MiB. Seven feature stories lead the page:

- **Jensen Huang walks back into Nvidia HQ** — reinstated as CEO, shares up 31%
- **24 killed in an Indonesian candy-factory fire**, ~30 still missing
- **Oxfam: Gaza is now a "toxic wasteland"**
- **Appeals court opens a path to erase Trump's hush-money conviction**
- **US to blacklist Asian AI firm Megaspeed** after the Nvidia chip scandal
- **Russian strikes kill 12 in the Kyiv region**; Ukraine hits Russian oil plants
- **Trump, Xi and Putin issue a joint nuclear-risk statement** at APEC

Below them, 54 briefs across the Americas, Europe, the Middle East, Africa,
Asia, markets, tech, science and sport — plus a date-check box naming the
stories deliberately left out because they belong to other days (the COP31
collapse, 22 Nov; the Libya ship strike, 23 Nov; the ICJ Myanmar ruling,
19 Nov).

## How it was made

The page was drawn fresh for this competition with a Python/Pillow renderer
written in the build session (see the build notes in this repo's history) and
then frozen as `entry.png`. The entry program itself is deliberately trivial:
`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` byte-for-byte, so two runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
