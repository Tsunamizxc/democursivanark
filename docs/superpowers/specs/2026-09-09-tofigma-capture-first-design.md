# tofigma + html-to-figma Capture-first

Date: 2026-09-09  
Approach: **Capture-first** — адаптировать HTML/CSS под возможности Playwright DOM capture, плюс точечные правки плагина.

## Goals

- Страницы в `tofigma/` максимально чисто переносятся в Figma через local html-to-figma.
- Актуальный визуал сайта (sticky-lead, hero, header icons) без дыр от mask/filter/fixed/JS.
- Единый capture-профиль: `_build_tofigma.py` FIGMA_OVERRIDES ≈ `prepareStaticPage` в плагине.

## Non-goals

- Полный auto-layout секций / blur как Figma effect / идеальный SVG textPath orbit.
- Изменение живого сайта (`index.html` / `css/style.css` для продакшена) ради Figma.

## Constraints (plugin)

Unsupported / fragile: `mask`, `filter`, `backdrop-filter`, `transform` (layout), CSS phone mask, lazy images, JS-only UI, sticky mid-page.

Supported: solid/gradient fills, box-shadow, radii, borders, IMG/SVG, Manrope, flex boxes as frames.

## Design

### A. Build pipeline (`_build_tofigma.py`)

1. Inject static `[data-sticky-lead]` markup (SVG Max/phone) before `</body>` if missing.
2. Expand `FIGMA_OVERRIDES`: sticky-lead absolute; hero orbit frozen + sized; body `padding-top: 0`; kill clip-path/mix-blend/filter animations; header solid white.
3. Rebuild all `tofigma/*.html` from root HTML + inlined CSS.
4. README.txt updated (sticky-lead, orbit, Desktop 1440).

### B. Plugin (`html-to-figma`)

1. Sync `prepareStaticPage` CSS with the same rules (sticky-lead, orbit, padding, filters).
2. Prefill folder path to this project's `tofigma` when sensible / update README.
3. Keep Manrope 400–800 preload.

### Success

Import Desktop 1440: `index.html` — header icon-btn visible, hero disk + photo, sticky-lead bar, offers/calc text editable; no invisible phone/Max icons.
