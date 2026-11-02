# Third search sweep (2026-11-01): work in progress

Collection only. Nothing in `data/` or `data/manifest.json` changes on this branch, and it is not for merging until approved.

Goal: find more people, money, contract jobs and organisations (NGOs, foundations, firms, public bodies) tied to the 2026 Constitutional Tribunal takeover, with provenance for every data point.

## Status

The sweep stopped on 2026-11-01 at about 19:46 UTC, when the account's weekly usage limit was reached, and resumed after the limit reset at 00:00 UTC on 2026-11-02. The resumed parts are still running; this file is updated as each one lands. So far: 1116 claims.

| Batch | What | Status |
|---|---|---|
| 01 | Page reads of the open leads left by the two earlier sweeps (`batch-01-open-lead-reads.json`) | 65 of 113 leads read: 70 pages, 593 claims. Not yet read: R015-R017, R021-R026, R039-R043, R053-R055, R059-R067, R080-R090, R100-R102, R106-R113 (reads running). |
| 02 | New searches and page reads: people, appointments and contract jobs (`batch-02-people-jobs.json`) | 4 of 7 themes searched (judges' paid roles, appointments, state company and media boards, Wawrykiewicz). 46 pages, 309 claims, 115 title-only leads. Follow-up reads: 6 groups done, 2 running. Running: nominations, prosecutors and police, international bodies. |
| 03 | New searches and page reads: money, grants and organisations (`batch-03-money-orgs.json`) | 4 of 7 themes searched (EU money, EEA and Norway grants, US money, private foundations). 36 pages, 214 claims, 104 title-only leads. Follow-up reads: 4 groups done, 3 running, 1 stopped. Running: domestic public money, NGO finances, firms and contracts. |
| 04 | Cross-check of every quoted excerpt against its page context | to do |

Agents stopped by the usage limit had already run 200 searches and 79 page reads. Those are logged in `raw/` under `searches_by_stopped_agents` and `fetches_by_stopped_agents`, as returned, with `agent_rerun_later` saying whether that part was run again. No claims came from the stopped agents.

## How to read a data point

- `access` says how the evidence was obtained: `page_read` (the page text was read and the quoted string was checked against it by script), `page_read_via_reader_extract` (the page reader returned its own extract of the page; the quoted string was checked against that extract, and a page-text re-check is pending) or `search_result_title_only` (only the search result title and URL were seen).
- `evidence_check` is the result of that script check: `exact`, `normalized` (found after normalising spaces, quote marks and dashes), `normalized_ci` (also ignoring case), `segments` (each part around an ellipsis found), `found_in_reader_extract_only` (not in the page text word for word, only in the reader's extract: treat the wording as unverified), `not_found` (treat the claim as unverified) or `no_raw` (no text captured). A `_in_reader_extract` suffix means the check ran against the reader's extract.
- `evidence_text` is copied from the source in its original language, kept short. `evidence_translation` is a literal English translation written for this file.
- `label` is one of `fact`, `alleged`, `speculation`, `unproven_conspiracy`, `no_link`. `fact` means the source states it (or the organisation published it). `label_scope` says exactly what the label covers.
- `map_status` compares the claim with the published map and the two earlier sweep branches: `pair_already_linked`, `new_tie_between_known_entities`, `new_entity_or_unmatched_name` or `both_names_unmatched`.
- `raw/` keeps every search with every result (rank, title, URL) as returned, and a log of every page-reader call (URL, time, HTTP line, length and SHA-256 of the text returned). The page text itself is not republished here.
