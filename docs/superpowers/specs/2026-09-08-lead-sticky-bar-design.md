# Lead sticky bar + homepage upsell (Alba)

Date: 2026-09-08  
Approach: **A** — clinic-style bottom bar everywhere + targeted homepage upsell  
Reference layout: [delta-clinic Omsk](https://omsk.delta-clinic.ru/) (bottom contact strip: call doctor + messengers)

## Goals

- Raise lead conversion without abandoning Alba premium visual language (Manrope, blue `#4f84ff`, soft radii/shadows).
- Always-visible contact actions: doctor call, phone, Max, Telegram.
- Make service cards more informative and action-oriented on the homepage.

## Non-goals

- Full homepage redesign / new color system.
- New CRM/backend; keep existing modal + `[data-form]` / `data-open-modal`.
- Forced-treatment or under-18 pages.

## 1. Sticky bottom bar (all pages, all viewports)

### Structure

Inject once via `js/main.js` (same pattern as catalog nav / footer services) so all HTML pages get it without editing 100+ files. Fallback markup on `index.html` optional if needed for no-JS — prefer JS inject for consistency.

```
.sticky-lead
  .sticky-lead__call   → a[data-city-tel]
      label «Вызов врача»
      span[data-city-phone]
  .sticky-lead__actions
      a Max   [data-city-max] + Max_logo.svg
      a TG    [data-city-tg] + telegram SVG
      a Phone [data-city-tel] + phone icon
```

### Behavior / layout

- `position: fixed; bottom: 0; left: 0; right: 0; z-index` above content, below modal.
- Premium strip: dark ink or soft glass on white with top border/shadow; primary CTA uses `--blue`.
- Desktop: wide primary «Вызов врача» + number on the left/center; three circular icon buttons on the right.
- Mobile: same row, primary flex-grows; icons stay tappable (~40–44px).
- Add `padding-bottom` on `body` (or footer) equal to bar height so content isn’t covered.
- Remove `.float-call` (replaced by this bar).

### City sync

Reuse existing `applyCity`: `data-city-tel`, `data-city-phone`, `data-city-tg`, `data-city-max`.

## 2. Homepage service blocks (offers + promos)

### Offers (`.offer`)

Keep mosaic grid. Enrich each card:

- Keep eyebrow + title + price.
- Longer benefit copy (1–2 lines).
- Add compact feature list (2–3 bullets: speed / anonymity / what’s included).
- Add visible CTA chip/button text e.g. «Оставить заявку» or «Узнать стоимость» (card may stay `<a>` to service page **or** split: body → service, CTA opens modal via `data-open-modal` — prefer **link to service + secondary modal CTA on section**, to avoid nested interactive issues; if whole card stays a link, CTA is visual only with stronger label «Подробнее и заявка»).

Recommended: keep card as link to service page; strengthen visual CTA strip inside card; add section-level «Получить консультацию» `data-open-modal` under the grid.

### Promos (`.promo`)

- Clearer offer (discount / free consult).
- Replace weak «Подробнее» with stronger actions: «Получить скидку», «Записаться бесплатно» → modal where appropriate, else service URL.
- Slightly richer body text (what’s included).

## 3. Aggressive CTAs (premium tone)

| Location | Change |
|----------|--------|
| Hero primary | «Вызвать врача сейчас» → `tel:` or modal; secondary «Получить консультацию» → modal |
| Header | Keep «Записаться» but ensure high contrast |
| Bottom CTA block | Stronger copy: urgency 24/7, «перезвоним за 5 минут» |
| Calc / forms | Submit labels: «Жду звонка» / «Отправить заявку» |
| Sticky bar | Primary always «Вызов врача» + visible number |

Copy stays respectful (clinic, anonymity) — urgency without scare tactics or illegal claims.

## 4. CSS

- New block: `.sticky-lead`, `.sticky-lead__call`, `.sticky-lead__actions`, icon sizing, Max filter as elsewhere.
- Extend `.offer` / `.promo` for bullets + CTA strip; preserve existing mosaic nth-child accents.
- Modal z-index > sticky bar.

## 5. Acceptance

- [ ] Bar visible on desktop and mobile on multiple pages after city change (phone/TG update).
- [ ] No overlap with footer/content; modal still usable.
- [ ] `.float-call` gone.
- [ ] Homepage offers/promos look richer; CTAs clearer.
- [ ] Design still reads as Alba (blue, radii, typography) — not a red “hard sell” skin.

## Out of scope for this pass

- Rewriting all ~100 service pages’ body copy.
- WhatsApp (not requested; Max + Telegram only).
