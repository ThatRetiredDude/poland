# Third search sweep (2026-11-01): work in progress

Collection only. Nothing in `data/` or `data/manifest.json` changes on this branch, and it is not for merging until approved.

Goal: find more people, money, contract jobs and organisations (NGOs, foundations, firms, public bodies) tied to the 2026 Constitutional Tribunal takeover, with provenance for every data point.

## Status

The sweep stopped on 2026-11-01 at about 19:46 UTC, when the account's weekly usage limit was reached, and resumed after the limit reset at 00:00 UTC on 2026-11-02. The resumed parts are still running; this file is updated as each one lands. So far: 2746 claims.

| Batch | What | Status |
|---|---|---|
| 01 | Page reads of the open leads left by the two earlier sweeps (`batch-01-open-lead-reads.json`) | 113 of 113 leads read: 125 pages, 1218 claims. |
| 02 | New searches and page reads: people, appointments and contract jobs (`batch-02-people-jobs.json`) | 7 of 7 themes searched (judges' paid roles, appointments, state company and media boards, Wawrykiewicz, nominations, prosecutors and police, international bodies). 109 pages, 816 claims, 272 title-only leads. Follow-up reads: 24 groups done. |
| 03 | New searches and page reads: money, grants and organisations (`batch-03-money-orgs.json`) | 7 of 7 themes searched (EU money, EEA and Norway grants, US money, private foundations, domestic public money, NGO finances, firms and contracts). 94 pages, 712 claims, 192 title-only leads. Follow-up reads: 21 groups done. |
| 04 | Cross-check of every quoted excerpt against its page context (`batch-04-cross-check.json`) | 2116 claims checked: 1742 supported, 329 partly supported, 31 not supported, 14 cannot tell. Label disagreements: 90; translation problems: 50. Not checked: 592 no_link findings and 38 claims with no matching page text or added later. |

Agents stopped by the usage limit had already run 200 searches and 79 page reads. Those are logged in `raw/` under `searches_by_stopped_agents` and `fetches_by_stopped_agents`, as returned, with `agent_rerun_later` saying whether that part was run again. No claims came from the stopped agents.

## Candidate nodes and ties (`third-sweep-2026-11-01.json`)

The claims from batches 01 to 03, merged into candidate graph data with every piece of evidence attached (none of it is on the map):

- 1243 candidate ties. 163 of them link two entities already on the map that the map does not yet link; 166 repeat or add to a pair the map already links.
- 748 candidate new people, organisations, bodies, firms and documents, 463 of them tied to at least one map entity.
- 592 no_link findings (a page checked for a link that it does not show), grouped into 441 entries by page and subject.
- Left out of the ties and kept under `leads_to_check`: 56 claims whose excerpt was not found in the page text, 30 claims the cross-check found not supported, and the title-only leads, unread pages and pages that could not be read.
- Each tie has `map_status`, its `relations`, `dates`, `amounts`, `label` and `label_scopes`, and `evidence` (one item per claim, with URL, excerpt, translation, excerpt check and cross-check verdict).

## How to read a data point

- `access` says how the evidence was obtained: `page_read` (the page text was read and the quoted string was checked against it by script), `page_read_via_reader_extract` (the page reader returned its own extract of the page; the quoted string was checked against that extract, and a page-text re-check is pending) or `search_result_title_only` (only the search result title and URL were seen).
- Long pages: the page reader returns the page text word for word only up to about 39,400 characters, then its own summary of the rest. Only the word-for-word part counts as page text; an excerpt found only in the summary is marked `found_in_reader_extract_only`. Where it mattered, the rest of the page was read word for word in further parts.
- `evidence_check` is the result of that script check: `exact`, `normalized` (found after normalising spaces, quote marks and dashes), `normalized_ci` (also ignoring case), `segments` (each part around an ellipsis found), `found_on_linked_page` (found word for word on another page the same reader opened from this one; see `evidence_found_at`), `found_in_reader_extract_only` (not in the page text word for word, only in the reader's extract: treat the wording as unverified), `not_found` (treat the claim as unverified) or `no_raw` (no text captured). A `_in_reader_extract` suffix means the check ran against the reader's extract.
- `evidence_text` is copied from the source in its original language, kept short. `evidence_translation` is a literal English translation written for this file.
- `label` is one of `fact`, `alleged`, `speculation`, `unproven_conspiracy`, `no_link`. `fact` means the source states it (or the organisation published it). `label_scope` says exactly what the label covers.
- `map_status` compares the claim with the published map and the two earlier sweep branches: `pair_already_linked`, `new_tie_between_known_entities`, `new_entity_or_unmatched_name` or `both_names_unmatched`.
- `raw/` keeps every search with every result (rank, title, URL) as returned, and a log of every page-reader call (URL, time, HTTP line, length and SHA-256 of the text returned). The page text itself is not republished here.
