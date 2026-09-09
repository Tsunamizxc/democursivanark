# -*- coding: utf-8 -*-
"""Build self-contained HTML+CSS pages into tofigma/ with JS content hardcoded."""
from pathlib import Path
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "tofigma"
CSS = (ROOT / "css" / "style.css").read_text(encoding="utf-8")
YEAR = str(datetime.now().year)

CITIES = [
    ("omsk", "Омск"),
    ("nsk", "Новосибирск"),
    ("tomsk", "Томск"),
    ("tyumen", "Тюмень"),
    ("barnaul", "Барнаул"),
    ("kemerovo", "Кемерово"),
    ("nkz", "Новокузнецк"),
    ("krsk", "Красноярск"),
    ("surgut", "Сургут"),
    ("moscow", "Москва"),
    ("spb", "Санкт-Петербург"),
]

CITY_PIN = (
    '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true">'
    '<path d="M10 18s6-5.2 6-10a6 6 0 1 0-12 0c0 4.8 6 10 6 10Z" stroke="currentColor" stroke-width="1.6"/>'
    '<circle cx="10" cy="8" r="2.1" stroke="currentColor" stroke-width="1.6"/></svg>'
)

CITY_BTN = (
    f'<button type="button" class="city-btn" data-open-city>'
    f'{CITY_PIN}<span data-city-name>Омск</span></button>'
)

GEO_CITIES = "".join(
    f'<button type="button" class="geo__city" data-city-id="{cid}">{name}</button>'
    for cid, name in CITIES
)

GEO_HTML = f'''
  <div class="geo is-open" data-geo data-tofigma-hard>
    <div class="geo__box" role="dialog" aria-modal="true" aria-labelledby="geo-title">
      <div class="geo__ask" data-geo-ask>
        <h2 id="geo-title">Вы из Омска?</h2>
        <p>Покажем телефон, адрес и условия вашей клиники.</p>
        <div class="geo__actions">
          <button type="button" class="btn btn--blue" data-geo-yes>Да, я из Омска</button>
          <button type="button" class="btn btn--line" data-geo-other>Выбрать другой город</button>
        </div>
      </div>
      <div class="geo__pick" data-geo-pick hidden>
        <h2>Выберите город</h2>
        <p>Работаем в Сибири и принимаем пациентов из других регионов.</p>
        <input class="geo__search" type="search" placeholder="Найти город" data-geo-search value="">
        <div class="geo__grid" data-geo-grid>{GEO_CITIES}</div>
        <button type="button" class="geo__back" data-geo-back>Назад</button>
      </div>
    </div>
  </div>
'''

# Separate static panel with city list always visible in page flow for Figma
# (geo overlay also included open — but we will NOT leave overlay open: it blocks the page)
# Instead: closed overlay in DOM + visible cookie + hard city UI pieces.

GEO_HTML_CLOSED = f'''
  <div class="geo" data-geo data-tofigma-hard>
    <div class="geo__box" role="dialog" aria-modal="true" aria-labelledby="geo-title">
      <div class="geo__ask" data-geo-ask>
        <h2 id="geo-title">Вы из Омска?</h2>
        <p>Покажем телефон, адрес и условия вашей клиники.</p>
        <div class="geo__actions">
          <button type="button" class="btn btn--blue" data-geo-yes>Да, я из Омска</button>
          <button type="button" class="btn btn--line" data-geo-other>Выбрать другой город</button>
        </div>
      </div>
      <div class="geo__pick" data-geo-pick>
        <h2>Выберите город</h2>
        <p>Работаем в Сибири и принимаем пациентов из других регионов.</p>
        <input class="geo__search" type="search" placeholder="Найти город" data-geo-search value="">
        <div class="geo__grid" data-geo-grid>{GEO_CITIES}</div>
        <button type="button" class="geo__back" data-geo-back>Назад</button>
      </div>
    </div>
  </div>
'''

COOKIE_HTML = '''
  <div class="cookie" data-tofigma-hard>
    <p>Сайт запоминает выбранный город и использует cookie. К страницам может быть подключена аналитика. Подробнее — в <a href="privacy.html">политике ПДн</a> и <a href="consent.html">согласии</a>.</p>
    <button type="button" class="btn btn--blue">Понятно</button>
  </div>
'''

CLINIC_EXTRA = (
    '<a data-extra-clinic href="reviews.html">Отзывы</a>'
    '<a data-extra-clinic href="methods.html">Методы помощи</a>'
    '<a data-extra-clinic href="sitemap.html">Карта сайта</a>'
)

PROGRAMS_MEGA = '''
          <div class="nav__col"><b>Срочно</b>
          <a href="service-zapoy.html">Запой и капельница</a>
          <a href="service-visit.html">Выезд нарколога</a>
          <a href="service-ambulance.html">Наркологическая скорая</a>
          <a href="service-withdrawal.html">Снятие ломки</a>
          <a href="service-ubod.html">УБОД</a></div>
          <div class="nav__col"><b>Лечение</b>
          <a href="service-alcohol.html">Алкоголизм</a>
          <a href="service-drugs.html">Наркомания</a>
          <a href="service-gambling.html">Игровая зависимость</a>
          <a href="service-code.html">Кодирование</a>
          <a href="service-rehab.html">Реабилитация</a></div>
          <div class="nav__col"><b>Клиника</b>
          <a href="service-detox.html">Детокс 24/7</a>
          <a href="service-psychiatry.html">Психиатрия</a>
          <a href="service-consult.html">Консультация</a>
          <a href="service-check.html">Диагностика</a>
          <a href="service-family.html">Семья</a></div>
          <div class="nav__col"><b>Ещё</b>
          <a href="service-help.html">Наркологическая помощь</a>
          <a href="methods.html">Методы</a>
          <a href="prices.html">Цены</a>
          <a href="programs.html">Весь каталог</a></div>
'''

MNAV_EXTRA = "".join(
    f'<a data-extra-mnav href="{h}">{t}</a>'
    for h, t in [
        ("service-alcohol.html", "Алкоголизм"),
        ("service-drugs.html", "Наркомания"),
        ("service-code.html", "Кодирование"),
        ("service-help.html", "Наркологическая помощь"),
        ("service-gambling.html", "Игровая зависимость"),
        ("reviews.html", "Отзывы"),
        ("methods.html", "Методы"),
        ("sitemap.html", "Карта сайта"),
    ]
)

FOOT_DIRECTIONS = '''
        <div data-extra-foot data-tofigma-hard>
          <h4>Направления</h4>
          <ul>
            <li><a href="service-alcohol.html">Алкоголизм</a></li>
            <li><a href="service-drugs.html">Наркомания</a></li>
            <li><a href="service-code.html">Кодирование</a></li>
            <li><a href="service-gambling.html">Игровая зависимость</a></li>
            <li><a href="service-help.html">Помощь 24/7</a></li>
          </ul>
        </div>
'''

FOOT_SERVICES = '''
      <div class="footer__services" data-footer-services data-tofigma-hard>
        <h4>Все услуги</h4>
        <div class="footer__services-grid">
          <div><b>Срочная помощь</b><ul>
            <li><a href="service-zapoy.html">Запой и капельница</a></li>
            <li><a href="service-visit.html">Выезд нарколога</a></li>
            <li><a href="service-ambulance.html">Наркологическая скорая</a></li>
            <li><a href="service-withdrawal.html">Снятие ломки</a></li>
            <li><a href="service-ubod.html">УБОД</a></li>
            <li><a href="service-sober.html">Частный вытрезвитель</a></li>
            <li><a href="service-detox.html">Детокс 24/7</a></li>
            <li><a href="service-drugtest.html">Тест на наркотики</a></li>
            <li><a href="service-toxicologist.html">Токсиколог</a></li>
            <li><a href="service-help.html">Наркологическая помощь</a></li>
          </ul></div>
          <div><b>Алкоголизм</b><ul>
            <li><a href="service-alcohol.html">Лечение алкоголизма</a></li>
            <li><a href="service-alcohol-women.html">Женский алкоголизм</a></li>
            <li><a href="service-alcohol-men.html">Мужской алкоголизм</a></li>
            <li><a href="service-alcohol-beer.html">Пивной</a></li>
            <li><a href="service-alcohol-wine.html">Винный</a></li>
            <li><a href="service-alcohol-elderly.html">Старческий</a></li>
            <li><a href="service-alcohol-home.html">На дому</a></li>
            <li><a href="service-alcohol-hangover.html">Похмелье</a></li>
            <li><a href="service-alcohol-shot.html">Укол от алкоголизма</a></li>
            <li><a href="service-alcohol-shichko.html">Метод Шичко</a></li>
          </ul></div>
          <div><b>Кодирование</b><ul>
            <li><a href="service-code.html">Кодирование</a></li>
            <li><a href="service-code-dovzhenko.html">По Довженко</a></li>
            <li><a href="service-code-hypnosis.html">Гипноз</a></li>
            <li><a href="service-code-implant.html">Вшивание ампулы</a></li>
            <li><a href="service-code-torpedo.html">Торпедо</a></li>
            <li><a href="service-code-esperal.html">Эспераль</a></li>
            <li><a href="service-code-double.html">Двойной блок</a></li>
            <li><a href="service-code-shot.html">Укол</a></li>
            <li><a href="service-code-needle.html">Иглоукалывание</a></li>
            <li><a href="service-code-aquilong.html">Аквилонг</a></li>
            <li><a href="service-code-vivitrol.html">Вивитрол</a></li>
            <li><a href="service-code-naltrexone.html">Налтрексон</a></li>
            <li><a href="service-code-disulfiram.html">Дисульфирам</a></li>
            <li><a href="service-code-algominal.html">Алгоминал</a></li>
            <li><a href="service-code-sit.html">SIT</a></li>
            <li><a href="service-code-home.html">На дому</a></li>
            <li><a href="service-decode.html">Раскодирование</a></li>
          </ul></div>
          <div><b>Наркомания</b><ul>
            <li><a href="service-drugs.html">Лечение наркомании</a></li>
            <li><a href="service-drugs-code.html">Кодировка от наркозависимости</a></li>
            <li><a href="service-drugs-heroin.html">Героин</a></li>
            <li><a href="service-drugs-methadone.html">Метадон</a></li>
            <li><a href="service-drugs-mephedrone.html">Мефедрон</a></li>
            <li><a href="service-drugs-salts.html">Соли</a></li>
            <li><a href="service-drugs-spice.html">Спайс</a></li>
            <li><a href="service-drugs-cocaine.html">Кокаин</a></li>
            <li><a href="service-drugs-amphetamine.html">Амфетамин</a></li>
            <li><a href="service-drugs-cannabis.html">Марихуана</a></li>
            <li><a href="service-drugs-toxico.html">Токсикомания</a></li>
            <li><a href="service-drugs-butyrate.html">Бутират</a></li>
            <li><a href="service-drugs-ephedrine.html">Эфедрин</a></li>
          </ul></div>
          <div><b>Реабилитация и семья</b><ul>
            <li><a href="service-rehab.html">Реабилитация</a></li>
            <li><a href="service-rehab-alcohol.html">Реабилитация алкозависимости</a></li>
            <li><a href="service-rehab-12.html">12 шагов</a></li>
            <li><a href="service-rehab-daytop.html">Day Top</a></li>
            <li><a href="service-family.html">Семейная программа</a></li>
            <li><a href="service-consult.html">Консультация</a></li>
            <li><a href="service-check.html">Диагностика</a></li>
            <li><a href="service-gambling.html">Игровая зависимость</a></li>
            <li><a href="service-betting.html">Ставки на спорт</a></li>
          </ul></div>
          <div><b>Психиатрия</b><ul>
            <li><a href="service-psychiatry.html">Психиатрия</a></li>
            <li><a href="service-psy-home.html">Психиатр на дом</a></li>
            <li><a href="service-psy-psychologist.html">Клинический психолог</a></li>
            <li><a href="service-psy-therapist.html">Психотерапевт</a></li>
            <li><a href="service-psy-neurologist.html">Невролог</a></li>
            <li><a href="service-psy-depression.html">Депрессия</a></li>
            <li><a href="service-psy-psychosis.html">Психоз</a></li>
            <li><a href="service-psy-delirium.html">Белая горячка</a></li>
            <li><a href="service-psy-panic.html">Панические атаки</a></li>
            <li><a href="service-psy-anxiety.html">Тревожное расстройство</a></li>
            <li><a href="service-psy-insomnia.html">Бессонница</a></li>
            <li><a href="service-psy-sleep.html">Нарушения сна</a></li>
            <li><a href="service-psy-meds.html">Лекарственная зависимость</a></li>
            <li><a href="service-psy-ocd.html">ОКР</a></li>
            <li><a href="service-psy-ptsd.html">ПТСР</a></li>
            <li><a href="service-psy-bipolar.html">Биполярное</a></li>
            <li><a href="service-psy-schizophrenia.html">Шизофрения</a></li>
            <li><a href="service-psy-adhd.html">СДВГ</a></li>
            <li><a href="service-psy-bpd.html">ПРЛ</a></li>
            <li><a href="service-psy-tad.html">Тревожно-депрессивное</a></li>
            <li><a href="service-psy-gad.html">ГТР</a></li>
            <li><a href="service-psy-stress.html">Стресс</a></li>
            <li><a href="service-psy-neurosis.html">Неврозы</a></li>
            <li><a href="service-psy-paranoia.html">Паранойя</a></li>
            <li><a href="service-psy-dementia.html">Деменция</a></li>
            <li><a href="service-psy-anorexia.html">Анорексия</a></li>
            <li><a href="service-psy-bulimia.html">Булимия</a></li>
            <li><a href="service-psy-dysmorpho.html">Дисморфофобия</a></li>
            <li><a href="service-psy-asthenia.html">Астения</a></li>
            <li><a href="service-psy-apathy.html">Апатия</a></li>
            <li><a href="service-psy-kleptomania.html">Клептомания</a></li>
            <li><a href="service-psy-narcolepsy.html">Нарколепсия</a></li>
            <li><a href="service-psy-tourette.html">Синдром Туретта</a></li>
            <li><a href="service-psy-sociopathy.html">Социопатия</a></li>
            <li><a href="service-psy-somnolence.html">Сонливость</a></li>
            <li><a href="service-psy-hypochondria.html">Ипохондрия</a></li>
            <li><a href="service-psy-autoaggression.html">Аутоагрессия</a></li>
            <li><a href="service-psy-neurasthenia.html">Неврастения</a></li>
            <li><a href="service-psy-autophobia.html">Аутофобия</a></li>
            <li><a href="service-psy-cyclothymia.html">Циклотимия</a></li>
          </ul></div>
        </div>
      </div>
'''

FOOT_DISC = (
    '<p class="footer__disc" data-tofigma-hard>'
    "Медицинские услуги оказываются совершеннолетним пациентам добровольно, "
    "по адресу клиники или на дому по месту вызова. Телефонная консультация носит "
    "информационный характер и не заменяет осмотр. Сайт не является публичной офертой. "
    "18+. Имеются противопоказания."
    "</p>"
)

CALC_OPTS = (
    '<button type="button">Алкоголизм</button>'
    '<button type="button">Наркомания</button>'
    '<button type="button">Игровая зависимость</button>'
    '<button type="button">Токсикомания</button>'
    '<button type="button">Срочный запой</button>'
)

CALC_DOTS = '<i class="is-on"></i><i></i><i></i><i></i>'

SELECT_EXTRA = [
    "Лечение алкоголизма",
    "Лечение наркомании",
    "Снятие ломки",
    "Игровая зависимость",
    "УБОД",
    "Рассрочка / точный расчёт",
]

PHONE_SVG = (
    '<svg class="icon-phone-svg" width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path fill="currentColor" d="M7.2 3.6c.5-.5 1.3-.6 1.9-.3l2.1 1.2c.6.3.9 1 .7 1.7l-.6 2.1c-.1.4 0 .8.3 1.1l1.7 1.7c.3.3.7.4 1.1.3l2.1-.6c.7-.2 1.4.1 1.7.7l1.2 2.1c.3.6.2 1.4-.3 1.9l-1.1 1.1c-.5.5-1.2.7-1.9.6-1.9-.3-4.5-1.6-7-4.1s-3.8-5.1-4.1-7c-.1-.7.1-1.4.6-1.9l1.1-1.1Z"/>'
    "</svg>"
)

MAX_SVG_BLUE = (
    '<svg class="icon-max-svg" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">'
    '<path fill="#4f84ff" d="M12 2.1C5.7 2.5 1.5 7.8 1.8 14.2c.1 2.7 1.2 5.1 1.5 7.7.1.7-.1 1.5.6 1.8.9.4 2.4-.2 3.2-.8.3-.2.5-.4.7-.7.8.5 1.6 1.1 2.6 1.3 4.3 1 9-1.3 11.1-5.1C25.3 10.6 20 1.8 12 2.1Zm-2.4 14.9c-.3.3-.7.6-1 .8-.6.3-.7 0-.9-.5-.6-1.5-.7-4.1-.3-5.7.5-2.2 2.2-4.1 4.5-4.3 2.3-.2 4.5 1 5.5 3.1 2.2 4.8-3.4 9.5-7.8 6.6Z"/>'
    "</svg>"
)

MAX_SVG_WHITE = (
    '<svg class="icon-max-svg" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">'
    '<path fill="#ffffff" d="M12 2.1C5.7 2.5 1.5 7.8 1.8 14.2c.1 2.7 1.2 5.1 1.5 7.7.1.7-.1 1.5.6 1.8.9.4 2.4-.2 3.2-.8.3-.2.5-.4.7-.7.8.5 1.6 1.1 2.6 1.3 4.3 1 9-1.3 11.1-5.1C25.3 10.6 20 1.8 12 2.1Zm-2.4 14.9c-.3.3-.7.6-1 .8-.6.3-.7 0-.9-.5-.6-1.5-.7-4.1-.3-5.7.5-2.2 2.2-4.1 4.5-4.3 2.3-.2 4.5 1 5.5 3.1 2.2 4.8-3.4 9.5-7.8 6.6Z"/>'
    "</svg>"
)

FIGMA_OVERRIDES = """
/* === html-to-figma capture profile ===
   Plugin freezes live DOM via getBoundingClientRect (no Auto Layout).
   Unsupported: mask, filter, backdrop-filter, transform, clip-path, text-shadow.
*/
*, *::before, *::after {
  animation: none !important;
  transition: none !important;
  scroll-behavior: auto !important;
}

.preloader,
.mnav,
.geo:not(.is-open) {
  display: none !important;
}

/* Reveal / split — fully painted */
[data-reveal],
[data-reveal="left"],
[data-reveal="right"],
[data-reveal="scale"],
.split,
.split span,
.split span em {
  opacity: 1 !important;
  transform: none !important;
  visibility: visible !important;
}

/* Sticky/fixed → document flow (capture is at scrollY=0; sticky mid-page is wrong) */
.header {
  position: relative !important;
  top: auto !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  background: #ffffff !important;
  box-shadow: 0 1px 0 rgba(30, 50, 120, 0.06) !important;
}
.svc-side,
.doc-panel {
  position: relative !important;
  top: auto !important;
}

/* Fixed chrome → absolute in page end zone so they still paint without covering content wrongly */
.float-call,
.cookie {
  position: absolute !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
}
.cookie {
  left: 16px !important;
  right: 16px !important;
  bottom: 16px !important;
  width: auto !important;
  max-width: 720px !important;
  margin: 0 auto !important;
  background: #161924 !important;
}
.float-call {
  right: 16px !important;
  bottom: 88px !important;
}

body.is-lock {
  position: static !important;
  overflow: visible !important;
  top: auto !important;
  width: auto !important;
}

/* Masks / filters — kill (invisible to capture) */
.icon-phone {
  display: none !important;
  mask-image: none !important;
  -webkit-mask-image: none !important;
  background: none !important;
}
.icon-phone-svg,
.icon-max-svg {
  display: block !important;
  width: 18px !important;
  height: 18px !important;
  flex-shrink: 0;
  color: #4f84ff;
}
.footer .icon-phone-svg { color: #ffffff; }
.icon-btn .icon-max,
.footer__msg .icon-max,
.footer .icon-max,
.mnav .icon-max {
  filter: none !important;
}
.gallery img,
.cat-card img,
.promo img {
  filter: none !important;
}

/* Marquee: static strip, no fade-mask / motion */
.marquee {
  mask-image: none !important;
  -webkit-mask-image: none !important;
  overflow: hidden !important;
}
.marquee__track {
  animation: none !important;
  transform: none !important;
  display: flex !important;
  width: max-content !important;
}
.marquee__group {
  animation: none !important;
  transform: none !important;
}

/* Pseudo circles: explicit px size (aspect-ratio alone is fragile) */
.hero__visual::before {
  width: 640px !important;
  height: 640px !important;
  aspect-ratio: auto !important;
  background: #ffffff !important;
}
.cta__box::after {
  width: 280px !important;
  height: 280px !important;
  background: rgba(255, 255, 255, 0.12) !important;
  border-radius: 50% !important;
}
.svc li::before,
.doc-body__main li::before,
.info-story__text li::before {
  width: 8px !important;
  height: 8px !important;
  border-radius: 50% !important;
  background: #4f84ff !important;
}

/* Accordion: expand all answers for capture */
.acc__panel {
  display: block !important;
  grid-template-rows: 1fr !important;
  opacity: 1 !important;
  max-height: none !important;
}
.acc__item.is-open .acc__panel {
  display: block !important;
  grid-template-rows: 1fr !important;
  opacity: 1 !important;
  max-height: none !important;
}
.acc__panel > div {
  overflow: visible !important;
}

/* Modal/geo overlays in hard panels — never fixed */
.tofigma-hard-panels .modal,
.tofigma-hard-panels .geo {
  position: relative !important;
  inset: auto !important;
  display: block !important;
  background: transparent !important;
  backdrop-filter: none !important;
  transform: none !important;
  opacity: 1 !important;
  visibility: visible !important;
  padding: 0 !important;
  pointer-events: none !important;
}
.tofigma-hard-panels .modal__box,
.tofigma-hard-panels .geo__box {
  position: relative !important;
  transform: none !important;
  opacity: 1 !important;
  margin: 0 auto 28px !important;
  max-width: 520px !important;
}
.tofigma-card {
  background: #ffffff;
  border-radius: 28px;
  padding: 28px;
  box-shadow: 0 18px 50px rgba(55, 90, 180, 0.08);
  margin: 0 auto 28px;
  max-width: 520px;
}

/* Hover transforms off */
[data-tilt],
.person:hover,
.promo:hover,
.cat-card:hover,
.offer:hover {
  transform: none !important;
}

html, body {
  position: relative !important;
}
.footer {
  position: relative !important;
  padding-bottom: 140px !important;
}
"""

# Visible Figma panels for overlays that normally need interaction
FIGMA_PANELS = f'''
  <section class="wrap tofigma-hard-panels" data-tofigma-hard style="padding:48px 0 64px">
    <h2 class="section-title">UI-оверлеи (для макета)</h2>
    <p style="color:#6b7285;max-width:560px;margin-bottom:28px;font-size:15px">Статичные копии geo и формы записи. На сайте открываются через JS.</p>
    <div class="tofigma-card geo__box">
      <div class="geo__ask">
        <h2>Вы из Омска?</h2>
        <p>Покажем телефон, адрес и условия вашей клиники.</p>
        <div class="geo__actions">
          <button type="button" class="btn btn--blue">Да, я из Омска</button>
          <button type="button" class="btn btn--line">Выбрать другой город</button>
        </div>
      </div>
    </div>
    <div class="tofigma-card geo__box">
      <div class="geo__pick">
        <h2>Выберите город</h2>
        <p>Работаем в Сибири и принимаем пациентов из других регионов.</p>
        <input class="geo__search" type="search" placeholder="Найти город" value="">
        <div class="geo__grid">{GEO_CITIES}</div>
        <button type="button" class="geo__back">Назад</button>
      </div>
    </div>
    <div class="tofigma-card modal__box form">
      <button class="modal__close" type="button" aria-label="Закрыть">×</button>
      <h2>Запись на консультацию</h2>
      <p>Оставьте номер — врач перезвонит в течение 10 минут.</p>
      <div class="form__fields">
        <label>Как к вам обращаться</label>
        <input type="text" placeholder="Имя или псевдоним" value="">
        <label>Телефон</label>
        <input type="tel" placeholder="+7 (" value="">
        <label>Программа</label>
        <select name="program">
          <option>Пока не знаю — подскажет врач</option>
          <option>Детокс</option>
          <option>Запой и капельница</option>
          <option>Психиатрия</option>
          <option>Кодирование</option>
          <option>Реабилитация</option>
          <option>Семейная консультация</option>
          <option>Выезд нарколога</option>
          <option>Лечение алкоголизма</option>
          <option>Лечение наркомании</option>
          <option>Снятие ломки</option>
          <option>Игровая зависимость</option>
          <option>УБОД</option>
          <option>Рассрочка / точный расчёт</option>
        </select>
        <button class="btn btn--blue" type="button">Отправить</button>
      </div>
    </div>
  </section>
'''


def rewrite_asset_urls(html: str) -> str:
    html = re.sub(r'(?<=["\'(])/?(images/)', r"../\1", html)
    html = html.replace("../../images/", "../images/")
    html = re.sub(r'<script\s+src=["\'][^"\']*js/main\.js["\']>\s*</script>', "", html, flags=re.I)
    return html


def inline_css(html: str) -> str:
    style_block = f"<style>\n{CSS}\n{FIGMA_OVERRIDES}\n</style>"
    html = re.sub(r'<link[^>]+href=["\'][^"\']*css/style\.css["\'][^>]*>\s*', "", html, flags=re.I)
    html = re.sub(r"</head>", style_block + "\n</head>", html, count=1, flags=re.I)
    return html


def inject_city_btn(html: str) -> str:
    if 'class="city-btn"' in html:
        return html
    # after logo link inside header__bar
    def after_logo(m):
        return m.group(0) + "\n      " + CITY_BTN

    html2, n = re.subn(
        r'(<header[^>]*>[\s\S]*?<div class="header__bar[^"]*"[^>]*>[\s\S]*?<a class="logo"[^>]*>[\s\S]*?</a>)',
        after_logo,
        html,
        count=1,
    )
    if n:
        html = html2
    # mnav city button at end before </nav>
    if 'data-mnav' in html and 'data-open-city' not in html.split('data-mnav', 1)[-1].split('</nav>', 1)[0]:
        html = re.sub(
            r'(<nav class="mnav"[^>]*>)([\s\S]*?)(</nav>)',
            lambda m: m.group(1) + m.group(2) + "\n    " + CITY_BTN + "\n  " + m.group(3),
            html,
            count=1,
        )
    return html


def enrich_clinic_nav(html: str) -> str:
    if "data-extra-clinic" in html:
        return html

    def repl_clinic(m):
        block = m.group(0)
        if "data-extra-clinic" in block:
            return block
        return block.replace("</div>", CLINIC_EXTRA + "\n          </div>", 1)

    # Find nav drop whose button contains Клиника
    html = re.sub(
        r'<div class="nav__drop">\s*<button class="nav__btn"[^>]*>Клиника[\s\S]*?<div class="nav__menu">[\s\S]*?</div>\s*</div>',
        repl_clinic,
        html,
        count=1,
    )
    return html


def enrich_programs_nav(html: str) -> str:
    if "nav__mega" in html and 'class="nav__menu nav__mega"' in html:
        return html

    # Fix previous broken builds: class="nav__menu" nav__mega"
    html = html.replace('class="nav__menu" nav__mega"', 'class="nav__menu nav__mega"')

    if 'class="nav__menu nav__mega"' in html:
        return html

    pattern = (
        r'(<div class="nav__drop">\s*'
        r'<button class="nav__btn"[^>]*>Программы[\s\S]*?</button>\s*)'
        r'<div class="nav__menu">[\s\S]*?</div>(\s*</div>)'
    )

    def repl(m):
        return (
            m.group(1)
            + '<div class="nav__menu nav__mega">'
            + PROGRAMS_MEGA
            + "\n          </div>"
            + m.group(2)
        )

    html2, n = re.subn(pattern, repl, html, count=1)
    return html2 if n else html


def enrich_mnav(html: str) -> str:
    if "data-extra-mnav" in html:
        return html
    # insert after prices.html link if present
    if 'href="prices.html"' in html and "data-mnav" in html:

        def mnav_repl(m):
            inner = m.group(2)
            if "data-extra-mnav" in inner:
                return m.group(0)
            if 'href="prices.html"' in inner:
                inner = re.sub(
                    r'(<a href="prices\.html">[^<]*</a>)',
                    r"\1\n    " + MNAV_EXTRA,
                    inner,
                    count=1,
                )
            else:
                inner = MNAV_EXTRA + "\n    " + inner
            return m.group(1) + inner + m.group(3)

        html = re.sub(
            r'(<nav class="mnav"[^>]*>)([\s\S]*?)(</nav>)',
            mnav_repl,
            html,
            count=1,
        )
    return html


def enrich_footer(html: str) -> str:
    if "data-footer-services" not in html and 'class="footer"' in html:
        # insert directions after Программы column
        def grid_repl(m):
            grid = m.group(0)
            if "data-extra-foot" in grid:
                return grid
            # after block with h4 Программы
            return re.sub(
                r'(<h4>Программы</h4>[\s\S]*?</div>)',
                r"\1\n" + FOOT_DIRECTIONS,
                grid,
                count=1,
            )

        html = re.sub(
            r'<div class="footer__grid">[\s\S]*?</div>\s*(?=<div class="footer__copy"|<p class="footer__disc"|<div class="footer__services")',
            grid_repl,
            html,
            count=1,
        )
        # if still no directions, try looser
        if "data-extra-foot" not in html:
            html = re.sub(
                r'(<h4>Программы</h4>[\s\S]*?</ul>\s*</div>)',
                r"\1\n" + FOOT_DIRECTIONS,
                html,
                count=1,
            )

        # services + disc before footer__copy
        if "data-footer-services" not in html:
            html = html.replace(
                '<div class="footer__copy">',
                FOOT_SERVICES + "\n      " + FOOT_DISC + '\n      <div class="footer__copy">',
                1,
            )
            # whitespace variants
            if "data-footer-services" not in html:
                html = re.sub(
                    r'(<div class="footer__copy">)',
                    FOOT_SERVICES + "\n      " + FOOT_DISC + "\n      " + r"\1",
                    html,
                    count=1,
                )
    elif "footer__disc" not in html and "footer__copy" in html:
        html = re.sub(
            r'(<div class="footer__copy">)',
            FOOT_DISC + "\n      " + r"\1",
            html,
            count=1,
        )
    return html


def fill_year(html: str) -> str:
    html = re.sub(r'<span data-year></span>', f'<span data-year>{YEAR}</span>', html)
    html = re.sub(r'<span data-year>\s*</span>', f'<span data-year>{YEAR}</span>', html)
    return html


def fill_counters(html: str) -> str:
    def repl(m):
        tag, raw = m.group(1), m.group(2)
        try:
            if "." in raw:
                text = f"{float(raw):.1f}"
            else:
                text = f"{int(float(raw)):,}".replace(",", "\u00a0")
        except ValueError:
            text = raw
        return f'<{tag} data-count="{raw}">{text}</{tag}>'

    return re.sub(
        r'<(span|b)\s+data-count="([^"]+)"[^>]*>\s*[^<]*</\1>',
        repl,
        html,
    )


def fill_calc(html: str) -> str:
    if "data-calc-opts" not in html:
        return html
    html = re.sub(
        r'(<div class="calc__steps" data-calc-dots)\s*>\s*</div>',
        r'\1>' + CALC_DOTS + "</div>",
        html,
    )
    html = re.sub(
        r'(<div class="calc__steps" data-calc-dots></div>)',
        '<div class="calc__steps" data-calc-dots>' + CALC_DOTS + "</div>",
        html,
    )
    html = re.sub(
        r'(<div class="calc-opts" data-calc-opts)\s*>\s*</div>',
        r'\1>' + CALC_OPTS + "</div>",
        html,
    )
    html = re.sub(
        r'(<h3 data-calc-q>)[^<]*(</h3>)',
        r"\1Что сейчас важнее?\2",
        html,
    )
    return html


def duplicate_marquee(html: str) -> str:
    if "marquee__group" not in html:
        return html

    pattern = (
        r'(<div class="marquee__track">\s*)'
        r'(<div class="marquee__group">[\s\S]*?</div>)'
        r'(\s*</div>)'
    )

    def repl(m):
        # already duplicated?
        after = html[m.end() : m.end() + 80]
        if "marquee__group" in m.group(0) and m.group(0).count("marquee__group") >= 2:
            return m.group(0)
        g = m.group(2)
        return m.group(1) + g + "\n        " + g + m.group(3)

    html2, n = re.subn(pattern, repl, html, count=1)
    return html2 if n else html


def enrich_selects(html: str) -> str:
    extras = "".join(f"<option>{t}</option>" for t in SELECT_EXTRA)

    def repl(m):
        block = m.group(0)
        if "Рассрочка" in block:
            return block
        return block.replace("</select>", extras + "</select>", 1)

    html = re.sub(
        r'<select[^>]*name="program"[^>]*>[\s\S]*?</select>',
        repl,
        html,
    )
    return html


def mark_reveals_and_splits(html: str) -> str:
    def add_isin_to_tag(m):
        tag = m.group(1)
        attrs = m.group(2)
        if re.search(r'\bclass="[^"]*\bis-in\b', attrs):
            return m.group(0)
        if 'class="' in attrs:
            attrs = re.sub(r'class="([^"]*)"', r'class="\1 is-in"', attrs, count=1)
        else:
            attrs = attrs + ' class="is-in"'
        return f"<{tag}{attrs}>"

    html = re.sub(
        r"<([a-zA-Z][a-zA-Z0-9]*)([^>]*\bdata-reveal(?:=\"[^\"]*\")?[^>]*)>",
        add_isin_to_tag,
        html,
    )

    def add_split_in(m):
        cls = m.group(1)
        if "is-in" in cls:
            return m.group(0)
        return f'class="{cls} is-in"'

    html = re.sub(r'class="([^"]*\bsplit\b[^"]*)"', add_split_in, html)
    return html


def inject_overlays(html: str) -> str:
    if "data-tofigma-hard" in html and "cookie" in html:
        pass
    chunks = []
    if 'class="cookie"' not in html:
        chunks.append(COOKIE_HTML)
    if 'data-geo' not in html:
        chunks.append(GEO_HTML_CLOSED)
    # hard panels only on index to avoid 126× huge duplicates? User asked all pages.
    # Put panels only on index + presents skip; on other pages cookie+city+footer is enough.
    insert = "\n".join(chunks)
    if insert:
        if re.search(r"</body>", html, re.I):
            html = re.sub(r"</body>", insert + "\n</body>", html, count=1, flags=re.I)
        else:
            html += insert
    return html


def inject_figma_panels(html: str, name: str) -> str:
    # Full overlay panels on key/unique pages only
    if name not in {
        "index.html",
        "about.html",
        "contacts.html",
        "doctors.html",
        "service-detox.html",
        "doctor-volkov.html",
        "404.html",
    }:
        return html
    if "tofigma-hard-panels" in html:
        return html
    html = re.sub(r"</main>", FIGMA_PANELS + "\n  </main>", html, count=1, flags=re.I)
    return html


def figma_tune_html(html: str) -> str:
    """Rewrite markup that html-to-figma cannot capture (mask/filter/lazy)."""
    # Phone icon: mask-based span → real SVG
    html = re.sub(
        r'<span class="icon-phone"[^>]*>\s*</span>',
        PHONE_SVG,
        html,
    )
    html = re.sub(
        r'<span class="icon-phone"[^>]*/>',
        PHONE_SVG,
        html,
    )

    # Max logos: CSS filter ignored → colored SVGs
    def repl_max(m):
        attrs = m.group(0)
        in_footer = False
        # crude: if nearby footer in last 200 chars of preceding context — handled by two passes
        return MAX_SVG_BLUE

    # header / generic Max img
    html = re.sub(
        r'<img class="icon-max"[^>]*>',
        MAX_SVG_BLUE,
        html,
    )
    # footer Max: white (replace again inside footer__msg / footer)
    def footer_max(m):
        block = m.group(0)
        block = block.replace(MAX_SVG_BLUE, MAX_SVG_WHITE)
        return block

    html = re.sub(
        r'<div class="footer__msg">[\s\S]*?</div>',
        footer_max,
        html,
    )

    # Eager images for capture
    html = re.sub(r'\sloading="lazy"', ' loading="eager"', html)
    html = re.sub(r'\sdecoding="async"', ' decoding="sync"', html)
    html = re.sub(
        r'(<img\b(?![^>]*\bloading=)[^>]*?)(/?>)',
        r'\1 loading="eager"\2',
        html,
    )

    # Open all FAQ items so answers are in the capture tree
    html = html.replace('class="acc__item"', 'class="acc__item is-open"')
    html = html.replace("class='acc__item'", "class='acc__item is-open'")

    # Remove empty hidden calc form clutter? keep for completeness

    # data-hidden geo pick: remove hidden attr in closed geo (already display:none whole geo)
    return html


def harden(html: str, name: str) -> str:
    html = inject_city_btn(html)
    html = enrich_clinic_nav(html)
    html = enrich_programs_nav(html)
    html = enrich_mnav(html)
    html = enrich_footer(html)
    html = fill_year(html)
    html = fill_counters(html)
    html = fill_calc(html)
    html = duplicate_marquee(html)
    html = enrich_selects(html)
    html = mark_reveals_and_splits(html)
    html = inject_overlays(html)
    html = inject_figma_panels(html, name)
    html = figma_tune_html(html)
    return html


def process(src: Path) -> str:
    name = src.name
    html = src.read_text(encoding="utf-8")
    if name == "presents.html":
        html = rewrite_asset_urls(html)
        # light capture profile for presents too
        if "</head>" in html:
            html = html.replace(
                "</head>",
                "<style>*,*::before,*::after{animation:none!important;transition:none!important}</style>\n</head>",
                1,
            )
        return html
    html = harden(html, name)
    html = rewrite_asset_urls(html)
    html = inline_css(html)
    return html


def main():
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.html"):
        old.unlink()

    count = 0
    for src in sorted(ROOT.glob("*.html")):
        (OUT / src.name).write_text(process(src), encoding="utf-8")
        count += 1

    (OUT / "README.txt").write_text(
        "HTML+CSS в одном файле для html-to-figma (Playwright DOM capture).\n\n"
        "Картинки: ../images/\n"
        "JS-контент зашит: город, cookie, mega-меню, футер услуг, счётчики, калькулятор.\n\n"
        "Профиль под плагин (shared/capture-script.ts):\n"
        "- нет mask/filter/backdrop-filter/transform\n"
        "- sticky/fixed → relative/absolute\n"
        "- телефон и Max — inline SVG (не CSS mask/filter)\n"
        "- images loading=eager\n"
        "- marquee без анимации\n"
        "- псевдо-круги с явным width/height\n\n"
        "Импорт: npm run server в html-to-figma → плагин → папка tofigma → Desktop 1440.\n"
        "Пересборка: python _build_tofigma.py\n",
        encoding="utf-8",
    )
    print("wrote", count, "files to", OUT)


if __name__ == "__main__":
    main()
