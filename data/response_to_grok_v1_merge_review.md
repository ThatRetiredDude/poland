# Response to grok-v1 merge review (2026-10-31)

Checked against primary sources on 2026-10-31. This file addresses each category in the merge review of the grok-v1 branch. Verified items remain as previously noted. Held items are re-examined where new or alternative sources exist. No conclusions.

## 1. Held: no working source (needs_source)

| Claim | Response |
|---|---|
| PhD supervisors: Markiewicz–Zedler, Dziurda–Ereciński, Taborowski–Czapliński, Berek–Zubik | No primary academic or university source located beyond the non-loading Wikipedia pages. Remains held. |
| Bio details (birth dates/places for Markiewicz, Berek, Bentkowska, Szostek; Berek ENA/PO candidacy; Korwin-Piotrowska SGH years) | University profiles and trybunal.net confirm limited facts (e.g. Szostek birth year, Berek ministerial service Dec 2023–14 Aug 2026). Exact dates/places and ENA/PO details not independently confirmed outside Wikipedia. Korwin-Piotrowska SGH postgraduate studies confirmed without years. Remains held for specifics. |
| Berek exact minister titles and dates | trybunal.net confirms ministerial service Dec 2023–14 Aug 2026. Precise titles/dates beyond that not located in primary sources. |
| Markiewicz spoke at Batory Nov 2024 rule-of-law conference | Batory 2024 annual report does not name him or the conference. No alternative source located. Remains held. |
| Batory paid to repair Tour de Konstytucja bus | Wyborcza article blocked. Batory’s PLN 154,000 grant to the foundation behind the tour is already mapped. Specific bus-repair claim remains held. |
| Watchdog Polska NED grants ($45k / $40k) and PLN 235,385 Dexis/USAID project | Watchdog BIP archive page (as of June 2024) lists NED “Freedom of Information – Recovery Action” at 334,155.52 PLN and “Improving Access to Information” at 34,916.13 PLN. Lobbyfacts.eu records NED “Improving Access to Information” (~39,982€) and Dexis USAID CEP ROLA “Watchdogs – expansion…” (~20,693€). Primary organizational disclosures exist. |
| Batory/EEA amounts to Themis (PLN 2,389.98 / 154,989.98) | MP X post and Themis project page not readable. 2014 EEA project already on map. Specific amounts remain held. |
| Latarnik Wyborczy as part of PKO/Orlen-backed “manipulative campaign” | warsawpoint.com page failed. No alternative source located. Remains held. |
| Kuisz president of Kultura Liberalna Foundation; Wigura co-founder | KRS page failed. Magazine “about” page lists Kuisz as editor-in-chief only. Remains held. |
| Themis founded 2010 as split from Iustitia; presidents Kamińska 2010–18, Morawiec 2018–24, Korwin-Piotrowska from Aug 2024 | Wikipedia not loading. No independent primary source located for founding date or full president sequence. Membership and current presidency already mapped. |
| Dom Sędziego Seniora founding representatives (Strączyński / Jolanta Korwin-Piotrowska for Iustitia; Kamińska for Themis) | Foundation page lists founders but not representatives. No documented family tie between Jolanta and Anna Korwin-Piotrowska. Remains held. |
| Batory Iustitia grants (PLN 95,000 in 2019; EUR 50,000 institutional 2022; Aequitas tally) | Previously held from issue #2. 2022 report shows no Iustitia institutional entry. X posts unreadable. Remains held. |
| Iustitia IAJ member “since about 2000” | Iustitia site confirms membership without date. Already mapped without the approximate year. |

## 2. Held: misleading

| Original claim | What the sources state |
|---|---|
| USAID cooperative agreement 7200AA22CA00025 (~$6.4M) funds Dexis’s rule-of-law programme | HigherGov and USAspending list $6,389,705 to “Miscellaneous Foreign Awardees” under title “Building Resilience in Civil Society,” place of performance Poland, period Oct 2022–Sep 2027. GMF’s own CEBRICS page describes the project as a five-year USAID-funded single-donor regional grantmaking programme (2022–2026) focused on Bulgaria, Hungary and Poland. The award record does not name Dexis. Dexis operates a separate USAID Central Europe Program Rule of Law Activity (CEP ROLA). The $6.4M award aligns with GMF CEBRICS, not Dexis. |
| HFHR received money from GMF’s CEBRICS | GMF CEBRICS factsheet names HFHR as an implementation partner. Hungarian Helsinki Committee page states its CEBRICS capacity-building project is financed by USAID and the German Marshall Fund. No source lists a specific grant amount paid to HFHR as a grantee under CEBRICS. Mapped correctly as partner. |
| The Journal of Democracy is “NED’s in-house journal” | Journal of Democracy “About” page: published by Johns Hopkins University Press. NED’s own page: “The National Endowment for Democracy’s International Forum for Democratic Studies produces the Journal of Democracy, published by Johns Hopkins University Press.” Editorial contact is jod@ned.org. NED produces it; Johns Hopkins publishes it. The “in-house” wording overstates the relationship. |
| Markiewicz sits on the Osiatyński Archive council | Archiwum Osiatyńskiego English “About” page and Polish Wikipedia (2020 list) both name both Krystian Markiewicz and Maciej Taborowski as members of the Programme Council. Markiewicz also co-authored the 2024 Archive report “Jak przywrócić praworządność.” Both affiliations are documented. |

## 3. Already on the map (duplicates)

Acknowledged. No further action required for:
- Korwin-Piotrowska suspending Święczkowski and Sochański; Tusk’s “There is no other way” post
- Berek as Tusk ally / “brain of the operation” (alleged)
- Iustitia and Themis co-founding Dom Sędziego Seniora; Iustitia’s 27 Oct 2026 aid request (75,000 PLN each for Markiewicz and Taborowski is additive detail)
- Batory 2022/2023 grants to Iustitia; EEA €100k + €8k
- Batory leading the €83.47M Civil Society Fund
- Themis joining MEDEL (7 Oct 2023); Korwin-Piotrowska as Themis president
- Taborowski at Hoffman, Taborowski i Wspólnicy and in Batory’s legal expert team
- Bentkowska, Szostek, Patyra as TK judges; Patyra on PGE board
- Dexis running USAID Central Europe rule-of-law grants

## 4. Left out on purpose

- Grok’s own lead_*.json files were not merged as written because they mixed verified, unsourced and incorrect items under a single “fact” label. Checked items were rebuilt separately.
- Placeholder nodes `spouse` and `asset_declaration` are not real entities; facts sit as profile fields.
- Taborowski’s children’s names: private details of non-public persons. Marriage and divorce (publicly reported) retained.
- `checked_no_link` lists kept off the public map per site rule.
- Sejm Presidium nomination edges redundant with existing profile data; vote counts moved to profiles.

## 5. Discrepancies

- **Korwin-Piotrowska ECHR settlement**: Official Ministry of Justice notice (23 Jan 2025) and ECHR decision (19 Dec 2024, application 38993/22) state that the Polish government issued a unilateral declaration which the applicant accepted; the Court struck the case out and the government is to pay 15,000 euro. Annex to the decision confirms the 15,000 EUR amount. TVN24’s earlier reporting of a 2022 settlement without amount is superseded by the 2024 decision.
- **Korwin-Piotrowska as Themis “founder”**: No source examined states she founded Themis. Sources confirm she is its president (from Aug 2024). Older map edge should be corrected to “president / member.”
- **Berek’s 17k income**: money.pl attributes the amount to sittings at the Warsaw legal advisers’ chamber. Map wording should follow that source rather than “other activity.”

## 6. Sources that could not be read

Where alternative primary sources were located (Watchdog BIP archive, Ministry of Justice ECHR notice, Journal of Democracy / NED pages, GMF CEBRICS page, Archiwum Osiatyńskiego council list, USAspending/HigherGov), they were used above. Remaining blocked pages (certain Wikipedia entries, X posts, Wyborcza, warsawpoint.com, rejestr.io) leave the associated claims held.

## Summary

- The $6.4M USAID award 7200AA22CA00025 is GMF CEBRICS, not Dexis.
- HFHR is a CEBRICS implementation partner, not a documented grantee of a specific amount.
- Journal of Democracy is produced by NED’s International Forum and published by Johns Hopkins University Press.
- Both Markiewicz and Taborowski appear on the Osiatyński Archive Programme Council.
- Watchdog NED and Dexis/USAID amounts are disclosed on the organization’s own BIP and lobbyfacts records.
- Korwin-Piotrowska ECHR case settled in December 2024 for 15,000 euro per the official decision.
- Remaining bio, PhD, specific grant-amount and founding-detail claims stay held pending readable primary sources.
