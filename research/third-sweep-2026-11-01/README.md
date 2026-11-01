# Third search sweep (2026-11-01): work in progress

Collection only. Nothing in `data/` or `data/manifest.json` changes on this branch, and it is not for merging until approved.

Goal: find more people, money, contract jobs and organisations (NGOs, foundations, firms, public bodies) tied to the 2026 Constitutional Tribunal takeover, with provenance for every data point.

## Batches (committed as each one lands)

| Batch | What | Status |
|---|---|---|
| 01 | Page reads of the open leads left by the two earlier sweeps (`batch-01-open-lead-reads.json`) | partial: 17 of 113 pages so far |
| 02 | New searches and page reads: people, appointments and contract jobs (`batch-02-people-jobs.json`) | partial: judges' paid roles, state boards and Wawrykiewicz themes in, four more running |
| 03 | New searches and page reads: money, grants and organisations (`batch-03-money-orgs.json`) | partial: EU and Norway themes in, five more running |
| 04 | Cross-check of every quoted string against the raw tool output | to do |

## How to read a data point

- `access` says how the evidence was obtained: `page_read` (the page text was read through a page-reader tool and the quoted string was found in it by script), `page_read_via_reader_extract` (the page reader returned its own extract of the page; the quoted string was found in that extract, and a page-text re-check is pending) or `search_result_title_only` (only the search result title and URL were seen).
- `evidence_text` is copied from the source in its original language, kept short. `evidence_translation` is a literal English translation written for this file.
- `label` is one of `fact`, `alleged`, `speculation`, `unproven_conspiracy`, `no_link`. `fact` means the source states it (or the organisation published it). `label_scope` says exactly what the label covers.
- `raw/` keeps every search result and page-reader output as returned, so each data point can be traced back.
