# Poland coup d'état relationship map

**[Open the map](https://thatretireddude.github.io/poland/)**

This is the first version of the suspected Poland coup d'état relationship map. If you have more information to add, or information that needs to be corrected or removed, click the button below and submit it. Thank you.

### [➕ Submit new information or a correction](https://github.com/ThatRetiredDude/poland/issues/new?template=submit-information.md)

You'll need a free GitHub account to submit. Please include a link to your source.

---

## About the map (technical details)

An interactive node graph for reviewing the research on the eight Constitutional Tribunal (TK) judges the Sejm elected in 2026: who they are tied to, through which organisations and money, and how solid each claim is.

## Viewing it

The page reads its JSON at load time, so it needs to be served over HTTP (browsers block `fetch` from `file://`):

```sh
python3 -m http.server 8000
# then open http://localhost:8000/
```

Opening `index.html` straight from disk will not load the data; serve it over HTTP.

## What it shows

- **Every link carries an evidence label**, shown by colour and line style: fact (solid green), alleged (dashed amber), speculation (dotted violet) and unproven conspiracy (thin red). "No link found" checks are not drawn; they are listed on each node.
- **Only money lines have thickness**, scaled by the amount in the relation text. Speculation and conspiracy lines are drawn but do not affect the layout.
- **Node shape** is the node type (person, org, event, project, policy, group). The eight judges have a gold ring.
- **Click a node or link** to see its fields and its source URLs. Node panels also list every link, including ones hidden by filters, and any "searched, nothing found" checks.
- **Filters** for evidence label, node type and group; each of the 8 judges can be switched off by name; Nawrocki is hidden by default ("Show Nawrocki").
- **Leads** tab: theories chased during research and how far each held up.

## Data

`data/poland_tk_graph.json` is the main graph. Companion files are loaded automatically when they are listed in `data/manifest.json` or in the main file's `meta.companions` (`{"files": ["a.json", "b.json"]}`). Files are merged by node `id`; duplicate edges (same source, target, relation and label) are merged and their sources combined; `node_updates` blocks add fields to existing nodes.

Schema in short:

- `nodes[]`: `id`, `type`, `group`, `label`, `sources[]`, plus any extra fields (shown as-is)
- `edges[]`: `source`, `target`, `relation`, `confidence` (`fact` | `alleged` | `speculation` | `unproven_conspiracy` | `no_link`), `sources[]`, optional `date`
- `leads[]`: `lead`, `result`, `label`
- `checked_no_link[]`: `subject`, `searched_for`, `result`, `sources[]`

People are linked only by institutional, financial or organisational ties.

`vendor/d3.min.js` is D3 v7.9.0 (ISC licence), bundled so the page works offline.

## Docker

```sh
docker build -t poland-map .
docker run -d --name poland-map -p 8080:80 -v "$PWD/data:/usr/share/nginx/html/data:ro" poland-map
# open http://localhost:8080/
```

The `-v` mount is optional: with it, updated JSON in `data/` shows up on a browser reload without rebuilding.
