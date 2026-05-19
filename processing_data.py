

import json
from pathlib import Path

def load_jade_file(path: Path) -> tuple[dict, list]:
    """Return (db, order) from a JADE export JSON file."""
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    return raw["db"], raw["order"]
 
 
# ── Load each file into its own named objects ─────────────────────────────────
cases_first, order_first = load_jade_file("input/FIRST 399 cases jade-cases-2026-05-13.json")
cases_last,  order_last  = load_jade_file("input/Last 387 cases jade-cases-2026-05-13.json")
 
# ── Combined view (optional convenience) ─────────────────────────────────────
cases_all = {**cases_first, **cases_last}   # Last_387 wins on any citation clash
order_all = order_first + order_last