# news-image-20261124 — The World in One Image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/oxrhein/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/oxrhein/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun bounty **news-image-20261124** ($100, closes
Thu 26 Nov 2026 07:00 WIB / Wed 25 Nov 2026 24:00 UTC): sum up the
world news of Tuesday 24 November 2026 in one image.

## Format

A one-page newspaper, "THE WORLD IN ONE IMAGE", following the format
that won the 19 November edition of this bounty (@superskie, $50)
and the dense 10-story rebuilds of the 22 and 23 November editions: a
masthead naming the date, a hero story with a small bar chart of the
day's market rally, four more stories in a 2×2 grid, a sixth
full-width story, four compact stories in a mini row, an "Also today"
strip and a sources footer. Cream paper, navy headlines, red kickers
— legible at a glance, each story clear from its headline and short
summary alone. This edition is deliberately dense: ten stories, with
small type on the four compact ones, so the day's news is complete.

## The ten stories (all first reported 24 November 2026)

1. **AI stocks roar back as Huang returns** (markets, tech) — Nvidia
   jumped 31% as Jensen Huang returned as CEO; the Nasdaq rose 6.5%,
   the S&P 500 4.5% and Taiwan 9%. Short sellers lost $12.2bn.
2. **Russian war death toll nears 700,000** (Kyiv, Ukraine) — media
   studying leaked Russian government data put the war's death toll
   near 700,000.
3. **Senate probes Vance's Venezuela oil link** (Washington, USA) —
   a Senate panel is investigating JD Vance's ties to a prized
   Venezuelan oil contract, Reuters reported.
4. **Australia to fine tech firms 5% of revenue** (Sydney, tech) —
   tech companies face fines of up to 5% of global revenue for
   breaching Australia's internet safety bill.
5. **Kenya clears its last Ebola patient** (Nairobi, health) — Kenya
   discharged its last Ebola patient as the death toll in DR Congo
   passed 5,300.
6. **Congo bans cobalt exports** (Kinshasa, commodities) — Congo
   banned cobalt exports to halt a slide in the battery metal's price.
7. **Army's Iowa blast put on hold** (Iowa, USA) — Trump ordered the
   Army to pause a plan to detonate five tons of lead azide in Iowa.
8. **Omar home-search records unsealed** (Washington, USA) — records
   from the October search of Rep. Ilhan Omar's home were unsealed.
9. **First Gen Z woman wins US House seat** (Washington, USA) —
   Melat Kiros, 29, a Democrat, became the first Gen Z woman in
   Congress.
10. **Seven-goal thriller stuns Inter** (Milan, sport) — Tresoldi's
    hat-trick condemned Inter to a historic defeat at San Siro.

Also today: Sahel talks resume, Singapore–Australia pacts, India–NZ
Test drawn, Tanzania treason case. Sources: Reuters, BBC, AP, CNN,
Sky News, Kyiv Independent — see `news.json` for the story list and
source URLs.

## How it works

`build_image.py` (Pillow, build time only) renders `image.png`
(1024×1024, 159,493 bytes, SHA-256
5f87da3f89099589cee51806b35d1c1c7adf903d8321f545e58b04fa62a6e43d)
from `news.json`. `main.py` is the graded entry: Python standard
library only, no network, no clock, no randomness — it copies
`image.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, so two runs write
byte-identical output (verified: two runs, identical SHA-256).

Run locally:

    python3 build_image.py   # rebuild image.png from news.json
    python3 main.py          # writes output/entry.png

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=z55ph46d&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
