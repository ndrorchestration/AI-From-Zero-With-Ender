# AFZ channel analysis — source-scoped vidIQ audit (2026-11-15)

**Status:** dated measurement receipt + editorial hypotheses. **Not:** a forecast, YouTube video mutation, controlled experiment, rights approval or verified causal diagnosis.

## Evidence, identity, and reporting windows

- Channel: AI From Zero With Ender, `UCgtz4pb1jhJj7RQR4eRJ7VA`.
- Connected vidIQ access to the user's authorized YouTube Analytics. Analysis requested Nov 15, 2026 ET; vidIQ audit generated Nov 16 UTC.
- Private YouTube Analytics current window: **Oct 15–Nov 13, 2026**, versus **Sep 15–Oct 14, 2026**; underlying reporting timezone **America/Los_Angeles**. YouTube Analytics Nov 14 was **not yet available** to that query.
- Different, newer **creator-provided Gemini/Studio** source: **Oct 18–Nov 14** last 28 days, with 383 views, 1,889 thumbnail impressions, 3.9% CTR, 5.6 watch hours, 1:55 AVD and +10 net subscribers. Do not combine that source with the vidIQ window to claim precise one-day deltas.
- Public counters at vidIQ retrieval: 15 subscribers, 431 lifetime views and 10 public videos (the channel's published episode count is nine; its 10-video catalog includes an unrelated 22-second post).

## Period comparison (vidIQ private Analytics)

| Metric | Oct 15–Nov 13 | Sep 15–Oct 14 | Change |
| --- | ---: | ---: | ---: |
| Views | 376 | 52 | +623% |
| Engaged views | 171 | 36 | +375% |
| Watch minutes | 323 | 65 | +397% |
| Net subscribers | +5 | +3 | +2 absolute; 0 recorded lost in either period |
| Average view duration | 1:51 | 1:52 | nearly flat |
| Average percentage viewed | 26.3% | 16.9% | +9.4 percentage points |

Recent 14 days (Oct 31–Nov 13) versus the preceding block (Oct 17–30): **233 vs 139 views**, **86 vs 83 engaged views**, **191 vs 132 watch minutes**, **+3 vs +2 subscribers**. Recent exposure rose notably faster than the engaged-view count; the evidence does **not** establish that algorithmic distribution, packaging, timing, or video length individually caused this difference.

## Episode-level detail within Oct 15–Nov 13

| Video | Runtime | Views | Engaged views | Watch minutes | Subscribers gained | AVD | Avg viewed | vidIQ age-relative outlier |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Episode 8](https://www.youtube.com/watch?v=L_IkNezgA_Y) — AI Misses the Point | 6:54 | 114 | 20 | 39 | 0 | 1:51 | 26.85% | 9.50× |
| [Episode 9](https://www.youtube.com/watch?v=r7WrGI0cb_s) — Generic Summaries | 11:52 | 44 | 25 | 68 | 1 | 2:15 | 19.04% | 5.17× |
| [Episode 3](https://www.youtube.com/watch?v=uE-ttaGXUxk) — Brutally Honest | 4:13 | 92 | 38 | 65 | 0 | 1:41 | 40.16% | 8.08× |
| [Episode 4](https://www.youtube.com/watch?v=_LCkLcdSsv4) — Epistemic Honesty | 4:24 | 12 | 9 | 15 | 2 | 1:44 | 39.43% | 1.00× |

The 2 subscribers attributed to EP04 from 12 period views are **a small-denominator signal only**, not an established subscriber-conversion advantage. Likewise EP09's higher watch minutes than EP08's despite fewer views does not prove its topic is more appealing; these are videos of different lengths and traffic mixes. Outlier ratios compare age-adjusted channel baselines and are **not predictions**.

## Representative audience retention

Data: 100-point audience-retention report on the two published videos. Audience watch ratio is a *segment-watch ratio*, and the separate relative-retention measure is a peer-relative rank (0.5 approximately median), **not** a percent of viewers. Approximate time conversions use known runtime.

| Position | Episode 8 still watching | Episode 9 still watching |
| --- | ---: | ---: |
| 1% | 95% | 96% |
| 6% | 55% | 44% (~0:43 of EP09) |
| 26% | 35% | 28% (~3:05 of EP09) |
| 41% | 25% | 32% (~4:52 of EP09) |
| 51% | 25% | 16% (~6:03 of EP09) |
| 100% | 15% | 8% |

**Transcript-aligned observations, not visual scene verification:**
- Episode 8: funny cake mismatch begins ~0:08; concrete relational explanation ~1:11; the real game-project example enters around 1:56.
- Episode 9: fictional dinner summary from 0:00; three-technique promise ~0:47; Trick One (Decision) ~3:29, Trick Two (Action) ~4:49, Trick Three (Evidence-Focused) ~6:11; prompt recipe ~8:49; bonus missing-information summary ~9:37.
- An EP09 retention increase near 41% (~4:52) is near the Action Summary entrance (~4:49), but coincidence/seek/rewatch/content pacing cannot be distinguished without native scene viewing and richer traffic segmentation.
- A hypothesis worth testing: let the first concrete, useful result arrive within approximately the first minute of a future video, then build an escalation and second payoff. This is a **proposal**, not an adopted brand rule or a request to rewrite published EP09.

## Discovery and packaging limitations

- EP08 traffic-source bucket labeled `SUBSCRIBER` (home/subscription browse features) showed 100 views with 10 engaged views. This is a category label, **not evidence that 100 subscribers watched** or autoplay alone caused the difference.
- The per-video thumbnail CTR / impressions report requires a connected vidIQ browser extension and was unavailable. The aggregate 3.9% Studio CTR does not support changing an individual thumbnail.
- Current audience demographics, returning-viewer counts, a controlled thumbnail experiment, and a reliable monetization forecast were **not** obtained.
- The apparent 383 total views × 1:55 AVD versus 5.6h watch-time mismatch is **not proven to be an error**: duration and watch time can depend on engaged-view definitions and different scopes. Computing 5.6h divided by 1:55 suggests around 175 play-equivalents, near but **not identical** to 171 engaged views in the older vidIQ window. Exact same-window definitions and raw metric reconciliation remain open.

## Editorial dependency register

| Dependent record | Action/status |
| --- | --- |
| [Canonical Notion growth & analytics center](https://app.notion.com/p/405f5bad238b81d6807fc674c415243d) | Added dated vidIQ supplement; preserves earlier Gemini/Studio snapshot and illustrative planning scenarios |
| [Notion editorial review register](https://app.notion.com/p/3fef5bad238b8130bd88cf4e6bfe751a) | Added retention insights and proposed hook/pacing experiments |
| [EP09 production log](https://app.notion.com/p/403f5bad238b81f087b8f33435814c91) | Added verified release URL and retrospective metrics, no retrospective visual-QA approval |
| [EP10 production log](https://app.notion.com/p/3fef5bad238b8176a949c7d77f49fc2d) | Added optional first-minute demonstration / entertainment hypothesis; still planned, script unapproved |
| [Master episode plan](https://app.notion.com/p/3fef5bad238b81faae73de6926dbed92) | Kept EP01–EP09 published and EP10 planned; no resequencing |
| [Native Google Sheet analytics ledger](https://docs.google.com/spreadsheets/d/1AtzFh049RLf9a4Ihv-F3Ees5lin34viFb4P-sziNeJw/edit) | Holds authoritative creator Studio snapshots; distinct vidIQ dated audit should not overwrite those rows |
| GitHub README + episode register | Updated to video ID/title index for EP01–EP09; historical source caveats preserved |

**Open gates:** obtain exact video thumbnail impressions/CTR; inspect finished Episode 9 video at retention transitions; compare next two uploads at matched age and reporting definitions; evaluate EP10 first-minute story variants with creator approval. No video metadata, original media, rights, or native Sheet rows were modified by this Markdown audit.
