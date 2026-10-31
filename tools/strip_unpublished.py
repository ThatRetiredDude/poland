#!/usr/bin/env python3
"""Remove research results that are kept off the public site.

"No link found" results (edges labelled no_link, and checked_no_link lists) stay
in the private research files but are not published. Run this on data/*.json
after copying in new research, before committing.
"""
import json
import pathlib
import sys

NO_LINK = {"no_link", "no_link_found", "nolink", "none_found", "no_money_found"}


def norm(v):
    return str(v or "").strip().lower().replace("-", "_").replace(" ", "_")


def strip(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return 0
    removed = 0
    if isinstance(data.get("edges"), list):
        keep = [e for e in data["edges"] if norm(e.get("confidence") or e.get("label")) not in NO_LINK]
        removed += len(data["edges"]) - len(keep)
        data["edges"] = keep
    if "checked_no_link" in data:
        removed += len(data.pop("checked_no_link") or [])
    if removed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return removed


if __name__ == "__main__":
    folder = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "data")
    for p in sorted(folder.glob("*.json")):
        n = strip(p)
        if n:
            print(f"{p.name}: removed {n}")
