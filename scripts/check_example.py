#!/usr/bin/env python3
"""Skeleton acceptance script for the Independent Review Gate.

Copy this file, edit the RULES section for your deliverable, run it.
Exit code 0 only when every check passes. Example data below is a toy invoice.
"""
import re
import sys
from pathlib import Path

SOURCE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("deliverable.md")
text = SOURCE.read_text(encoding="utf-8")
results = []


def check(name, ok, detail=""):
    results.append((ok, name, detail))


# --- RULES: edit below -------------------------------------------------------
MUST_CONTAIN = ["Total", "Payment terms"]
MUST_NOT_CONTAIN = ["TODO", "[REVIEW]", "old-address", "lorem ipsum"]

for s in MUST_CONTAIN:
    check(f"must contain: {s}", s in text)
for s in MUST_NOT_CONTAIN:
    check(f"must not remain: {s}", s not in text)

# sums written as "a + b + c = d"
num = r"\d{1,3}(?:,\d{3})*(?:\.\d+)?"
for m in re.finditer(rf"({num}(?:\s*\+\s*{num})+)\s*=\s*({num})", text):
    parts = [float(x.replace(",", "")) for x in re.findall(num, m.group(1))]
    total = float(m.group(2).replace(",", ""))
    check(f"sum {m.group(0)}", abs(sum(parts) - total) < 0.005, f"actual {sum(parts):,.2f}")

# invariants: refund must not exceed amount paid (edit the table to match your doc)
PACKAGES = {"basic": (100, 40), "plus": (150, 60)}  # name: (paid, refund)
for name, (paid, refund) in PACKAGES.items():
    check(f"refund <= paid: {name}", refund <= paid, f"paid {paid}, refund {refund}")

# every "section N" reference must have a matching heading
for ref in sorted(set(re.findall(r"[Ss]ection (\d+)", text))):
    check(f"section {ref} exists", re.search(rf"^#+\s*{ref}\b", text, re.M) is not None)
# --- end RULES ---------------------------------------------------------------

failed = [r for r in results if not r[0]]
for ok, name, detail in results:
    print(("PASS  " if ok else "FAIL  ") + name + (f"  -> {detail}" if detail and not ok else ""))
print(f"\n{len(results)} checks, {len(failed)} failed")
sys.exit(1 if failed else 0)
