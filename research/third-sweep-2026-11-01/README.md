# Third search sweep (2026-11-01): work in progress

Collection only. Nothing in `data/` or `data/manifest.json` changes on this branch, and it is not for merging until approved.

Goal: find more people, money, contract jobs and organisations (NGOs, foundations, firms, public bodies) tied to the 2026 Constitutional Tribunal takeover, with provenance for every data point.

## Status (2026-11-02)

The sweep stopped on 2026-11-01 at about 19:46 UTC, when the account's weekly usage limit was reached. Everything that finished before the stop is in this folder. The stopped parts are listed below and in each file's `stats.agents_stopped_at_usage_limit`.

| Batch | What | Status |
|---|---|---|
| 01 | Page reads of the open leads left by the two earlier sweeps (`batch-01-open-lead-reads.json`) | 62 of 113 leads read: 67 pages, 582 claims. Not yet read: R015-R017, R021-R026, R036-R043, R053-R055, R059-R067, R080-R090, R100-R102, R106-R113 |
| 02 | New searches and page reads: people, appointments and contract jobs (`batch-02-people-jobs.json`) | 4 of 7 themes: judges' paid roles, appointments, state company boards, Wawrykiewicz. 40 pages, 235 claims, 115 title-only leads. Stopped: nominations, prosecutors and police, international bodies, and the follow-up reads for appointments and for part of the judges' pay and Wawrykiewicz themes |
| 03 | New searches and page reads: money, grants and organisations (`batch-03-money-orgs.json`) | 4 of 7 themes: EU money, EEA and Norway grants, US money, private foundations. 33 pages, 156 claims, 104 title-only leads. Stopped: domestic public money, NGO finances, firms and contracts, and the follow-up reads for EEA and Norway and for part of the EU, US and foundation themes |
| 04 | Cross-check of every quoted string against the raw tool output | to do |

The stopped agents had already run 200 searches and 79 page reads. Those are logged in `raw/` under `searches_by_stopped_agents` and `fetches_by_stopped_agents`, as returned. No claims came from them.

## How to read a data point

- `access` says how the evidence was obtained: `page_read` (the page text was read and the quoted string was found in it by script), `page_read_via_reader_extract` (the page reader returned its own extract of the page; the quoted string was found in that extract, and a page-text re-check is pending) or `search_result_title_only` (only the search result title and URL were seen).
- `evidence_check` is the result of that script check: `exact`, `normalized` (found after normalising spaces, quote marks and dashes), `normalized_ci` (also ignoring case), `segments` (each part around an ellipsis found), `not_found` (treat the claim as unverified) or `no_raw` (no text captured). A `_in_reader_extract` suffix means the check ran against the reader's extract.
- `evidence_text` is copied from the source in its original language, kept short. `evidence_translation` is a literal English translation written for this file.
- `label` is one of `fact`, `alleged`, `speculation`, `unproven_conspiracy`, `no_link`. `fact` means the source states it (or the organisation published it). `label_scope` says exactly what the label covers.
- `map_status` compares the claim with the published map and the two earlier sweep branches: `pair_already_linked`, `new_tie_between_known_entities`, `new_entity_or_unmatched_name` or `both_names_unmatched`.
- `raw/` keeps every search with every result (rank, title, URL) as returned, and a log of every page-reader call (URL, time, HTTP line, length and SHA-256 of the text returned). The page text itself is not republished here.
