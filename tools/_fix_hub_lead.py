# -*- coding: utf-8 -*-
"""Add call button to hub-lead blue boxes (same pattern as cta__box)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CALL_LINE = (
    '<a class="btn btn--line" href="tel:+78001001212" data-city-tel>'
    'Позвонить: <span data-city-phone>8 800 100-12-12</span></a>'
)

BOX_RE = re.compile(
    r'(<div class="hub-lead__box"[^>]*>)([\s\S]*?)(</div>\s*)(?=</section>)',
    re.I,
)

BTN_RE = re.compile(r'<a class="btn\b[^>]*>[\s\S]*?</a>', re.I)


def fix_inner(inner: str) -> str:
    if "hub-lead__actions" in inner:
        return inner
    btns = list(BTN_RE.finditer(inner))
    if not btns:
        actions = (
            f'<div class="hub-lead__actions">'
            f'<a class="btn btn--blue" href="#" data-open-modal>Оставить заявку</a>'
            f"{CALL_LINE}</div>"
        )
        return inner.rstrip() + "\n        " + actions + "\n      "
    last = btns[-1]
    primary = last.group(0)
    cleaned = inner[: last.start()] + inner[last.end() :]
    actions = f'<div class="hub-lead__actions">{primary}{CALL_LINE}</div>'
    return cleaned.rstrip() + "\n        " + actions + "\n      "


def main() -> None:
    n = 0
    for path in sorted(ROOT.glob("*.html")):
        html = path.read_text(encoding="utf-8")
        if "hub-lead__box" not in html:
            continue
        changed = False

        def repl(m: re.Match) -> str:
            nonlocal changed
            new_inner = fix_inner(m.group(2))
            if new_inner != m.group(2):
                changed = True
            return m.group(1) + new_inner + m.group(3)

        new_html = BOX_RE.sub(repl, html)
        if changed:
            path.write_text(new_html, encoding="utf-8")
            n += 1
            print("fixed", path.name)
    print("changed", n)


if __name__ == "__main__":
    main()
