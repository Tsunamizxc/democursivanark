# -*- coding: utf-8 -*-
"""Ensure every .cta__box has two buttons: primary + call."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ARR = (
    '<span class="arr"><svg viewBox="0 0 14 14" fill="none">'
    '<path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
)

CALL = (
    '<a class="btn btn--ghost-light" href="tel:+78001001212" data-city-tel>'
    'Позвонить: <span data-city-phone>8 800 100-12-12</span></a>'
)

BOX_RE = re.compile(
    r'(<div class="cta__box"[^>]*>)([\s\S]*?)(</div>\s*)(?=</section>)',
    re.I,
)

BTN_RE = re.compile(r'<a class="btn\b[^>]*>[\s\S]*?</a>', re.I)


def normalize_primary(btn: str) -> str:
    btn = re.sub(r"(>)\s*Записаться\s*", r"\1Оставить заявку ", btn, count=1)
    if "Оставить заявку" not in btn and "Записаться" not in btn:
        # keep original label
        pass
    return btn


def fix_box(inner: str) -> str:
    if "cta__actions" in inner and "btn--ghost-light" in inner:
        return inner
    if "cta__actions" in inner and CALL not in inner and "Позвонить" not in inner:
        return re.sub(
            r'(<div class="cta__actions">)([\s\S]*?)(</div>)',
            lambda m: m.group(1) + m.group(2).rstrip() + CALL + m.group(3),
            inner,
            count=1,
        )

    btns = list(BTN_RE.finditer(inner))
    if not btns:
        # no button — append both
        actions = (
            f'<div class="cta__actions">'
            f'<a class="btn btn--light" href="#" data-open-modal>Оставить заявку {ARR}</a>'
            f"{CALL}</div>"
        )
        return inner.rstrip() + "\n        " + actions + "\n      "

    # Use last btn as primary (typical CTA layout)
    last = btns[-1]
    primary = normalize_primary(last.group(0))
    # remove all bare btn links that are direct children actions
    cleaned = inner
    # remove from last btn only and wrap
    cleaned = cleaned[: last.start()] + cleaned[last.end() :]
    # also remove other trailing single CTA buttons if they are the only action buttons
    # (avoid duplicating if somehow multiple)
    actions = f'<div class="cta__actions">{primary}{CALL}</div>'
    cleaned = cleaned.rstrip() + "\n        " + actions + "\n      "
    return cleaned


def process(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    if "cta__box" not in html:
        return False

    changed = False

    def repl(m: re.Match) -> str:
        nonlocal changed
        open_tag, inner, close = m.group(1), m.group(2), m.group(3)
        new_inner = fix_box(inner)
        if new_inner != inner:
            changed = True
        return open_tag + new_inner + close

    new_html = BOX_RE.sub(repl, html)
    if changed:
        path.write_text(new_html, encoding="utf-8")
    return changed


def main() -> None:
    files = sorted(ROOT.glob("*.html"))
    n = 0
    still = []
    for f in files:
        if process(f):
            n += 1
            print("fixed", f.name)
    # audit
    for f in files:
        t = f.read_text(encoding="utf-8")
        for m in re.finditer(r'<section class="cta\b[\s\S]*?</section>', t, re.I):
            block = m.group(0)
            if "cta__actions" not in block or "btn--ghost-light" not in block:
                still.append(f.name)
    print(f"changed={n} still_bad={still[:30]} count={len(still)}")


if __name__ == "__main__":
    main()
