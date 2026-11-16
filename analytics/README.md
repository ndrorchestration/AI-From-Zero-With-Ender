# YouTube Studio analytics snapshots

These records are manually supplied snapshots, not an automated YouTube Analytics API feed. Do not add rolling periods together, infer unique viewers from views, or infer click-through rates without supporting data.

| Metric | Value | Observation window | Source |
| --- | ---: | --- | --- |
| Views | 181 | September 30–October 27, 2026 (last 28 days) | Channel analytics shared by channel owner October 28 |
| Thumbnail impressions | 541 | September 30–October 27, 2026 (last 28 days) | Channel analytics shared by channel owner October 28 |
| Thumbnail impression period comparison | >999% higher than previous 28 days (Studio display) | September 30–October 27, 2026 | Channel analytics shared by channel owner October 28 |

**Context:** Episode 6 went live October 28, 2026, after the analytics window above ended. These figures must not be attributed to Episode 6.

Suggested future snapshot columns: observation date; start/end dates; views; impressions; impressions CTR; watch time; average view duration; subscribers gained; episode counts; sources and notes. Leave unreported fields blank.


## November 15, 2026 — creator-supplied Studio/Gemini 28-day snapshot

A creator-provided Gemini summary of YouTube Studio reports Oct 18–Nov 14 vs the prior 28 days: 383 vs 68 views, 1,889 vs 247 thumbnail impressions, 3.9% vs 4.5% CTR, 5.6 vs 1.2 watch hours, 1:55 vs 1:32 AVD, and +10 vs +3 net subscribers. These are **transcribed creator-supplied measurements**, not a fresh GitHub-side Analytics API query; provenance appears in [snapshots.csv](snapshots.csv). A 0.6 percentage-point CTR drop is distinct from a relative percentage change. Do not compound overlapping periods into forecasts.

The **separate** connected vidIQ API reporting window ends Nov 13, not Nov 14: 376 views, 171 engaged views, 323 watch minutes, +5 net subscribers. Its detailed per-video engagement, retention, and limitations are in [vidIQ November 15 audit](vidiq-audit-2026-11-15.md). Public total views, engaged views, average view duration and watch hours must retain their own metric definitions; an apparent cross-metric arithmetic mismatch is not proof of erroneous data. Same-window Studio source-definition reconciliation remains open.

Canonical maintained quantitative spreadsheet: [AI From Zero — Channel Growth & Video Analytics Ledger](https://docs.google.com/spreadsheets/d/1AtzFh049RLf9a4Ihv-F3Ees5lin34viFb4P-sziNeJw/edit). This small CSV is a GitHub historical companion, not a replacement for the native Sheet. No monetization eligibility is inferred from these generic watch-time counters.
