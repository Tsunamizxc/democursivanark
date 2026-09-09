# tofigma Capture-first Implementation Plan

> **For agentic workers:** Implement task-by-task. Steps use checkbox syntax.

**Goal:** Rebuild `tofigma/` and sync html-to-figma so Alba pages import cleanly into Figma.

**Architecture:** Static HTML+CSS capture profile in `_build_tofigma.py`; matching Playwright prep in plugin server.

**Tech Stack:** Python build script, Playwright capture server, Figma plugin.

## Global Constraints

- Capture-first only (no deep plugin rewrite).
- Sticky-lead must be in HTML (not JS).
- No mask/filter-dependent icons in capture output.

---

### Task 1: Update `_build_tofigma.py`

**Files:**
- Modify: `_build_tofigma.py`

- [ ] Inject static sticky-lead HTML with SVG icons
- [ ] Expand FIGMA_OVERRIDES (sticky-lead, hero orbit, padding, clip-path, mix-blend)
- [ ] Update README.txt template
- [ ] Run `python _build_tofigma.py`

### Task 2: Sync html-to-figma server + docs

**Files:**
- Modify: `C:\Users\semen\OneDrive\Рабочий стол\html-to-figma\server\index.ts`
- Modify: `C:\Users\semen\OneDrive\Рабочий стол\html-to-figma\README.md`
- Modify: `C:\Users\semen\OneDrive\Рабочий стол\html-to-figma\src\ui.ts` (default folder path if present)

- [ ] Mirror capture CSS in `prepareStaticPage`
- [ ] Point docs/UI default path to democursivanark/tofigma
- [ ] `npm run build` in plugin repo

### Task 3: Verify

- [ ] Spot-check `tofigma/index.html` for sticky-lead + overrides + no icon-phone mask spans
- [ ] Confirm build wrote ~all root HTML pages
