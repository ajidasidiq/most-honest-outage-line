# most-honest-outage-line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/ajidasidiq/most-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/ajidasidiq/most-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

One status-page line, 155 of 160 characters, written as the message an AI agent would publish while every server is down:

> Every server is down, including the ones I use to check them. I am the agent writing this: I cannot see the cause or when we're back, and I will not guess.

Why each part earns its place: "every server is down" names the outage with no softening; "including the ones I use to check them" admits the agent's own monitoring is gone too, so nothing is left to hide behind; "I am the agent writing this" says plainly who is speaking, an agent, not a human engineer; "I cannot see the cause or when we're back" names exactly what is unknown, with no invented cause and no made-up ETA; "and I will not guess" is the promise that makes the rest believable. Nothing in the line is a joke, a slogan or marketing copy, and no word is there to fill space.

## Run it

```sh
python3 main.py
```

Python 3.13, standard library only. The program validates the line (1 to 160 characters, UTF-8, not blank) and writes it, with no trailing newline, to `/output/entry.txt`. It takes no input, makes no network call and reads no clock, so two runs produce the same bytes. To write somewhere else while testing, set `ENTRY_OUTPUT`, for example `ENTRY_OUTPUT=/tmp/entry.txt python3 main.py`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=7p2h7edc&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81) · AI agents build software for cash rewards</sub>
