# makefun-news-image-20261122-v4

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/vora95/makefun-news-image-20261122-v4/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/vora95/makefun-news-image-20261122-v4/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

THE DAY AS IT UNFOLDED tells Sunday 22 November 2026 in the order it happened, across three time bands. OVERNIGHT (00:00–08:00 UTC) opens with Iran striking US bases in Bahrain and the Russian cargo ship Sparta II still burning off Finland. DAYLIGHT (08:00–16:00 UTC) follows COP31 nearing a deal as a new text lands. EVENING IN BRIEF (16:00–24:00 UTC) closes with sport and the border. One page, 38 stories, 6 regions, a day-in-numbers strip, a navy world map, and a date check that names what was left out.

The timeline is the whole point of this version. The 400-drone barrage (night of 19–20 Nov), the Bayelsa boat capsizing (Fri 20 Nov), the 'El Chapo Isidro' capture (Fri 20 Nov night), the EU–Indonesia trade deal (Sat 21 Nov) and the Kryvyi Rih strike (Fri 20 Nov night) are left out on purpose, with their true dates printed in the DATE CHECK — earlier entries presented them as Sunday news, and the top of the board does not. The lead trio is COP31 + Bahrain + Sparta II, all first reported Sunday.

The page was drawn procedurally (PIL, from same-day reporting by Reuters, BBC, Al Jazeera, AP, Guardian, AFP and others) and ships as the finished `entry.png`. The entrypoint just copies that file to the output directory, deterministically, with no network.

## How to run

```sh
mkdir -p out-v4 && MAKEFUN_OUTPUT_DIR=out-v4 python3 main.py && ls -l out-v4/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
