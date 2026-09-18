# -*- coding: utf-8 -*-
"""Add team-link bullet under «Что входит» on service/program pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEM = "Связка с психологом, психотерапевтом, психиатром, наркологом, неврологом по согласованию."
LI = f"<li>{ITEM}</li>"

# Match «Что входит» heading + following ul
BLOCK_RE = re.compile(
    r"(<h2>\s*Что входит\s*</h2>\s*<ul>)([\s\S]*?)(</ul>)",
    re.I,
)


def process(html: str) -> tuple[str, bool]:
    if ITEM in html:
        return html, False

    def repl(m: re.Match) -> str:
        open_ul, body, close = m.group(1), m.group(2), m.group(3)
        # avoid duplicate if already present in this list
        if ITEM in body:
            return m.group(0)
        body = body.rstrip() + "\n          " + LI + "\n        "
        return open_ul + body + close

    new_html, n = BLOCK_RE.subn(repl, html, count=1)
    return new_html, n > 0 and new_html != html


def main() -> None:
    files = sorted(ROOT.glob("service-*.html")) + [ROOT / "programs.html"]
    done = 0
    skipped = 0
    missing = []
    for path in files:
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        if not re.search(r"<h2>\s*Что входит\s*</h2>", html, re.I):
            missing.append(path.name)
            continue
        new_html, changed = process(html)
        if changed:
            path.write_text(new_html, encoding="utf-8")
            done += 1
        else:
            skipped += 1
    print(f"updated={done} skipped={skipped} no_heading={missing[:20]} missing_count={len(missing)}")


if __name__ == "__main__":
    main()
