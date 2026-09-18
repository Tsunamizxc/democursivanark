# -*- coding: utf-8 -*-
"""Batch upgrades: help doctor, FAQ×20, CTA call btn, phone label, SEO pad, new pages."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOCTORS = [
    {
        "name": "Морозов Павел Игоревич",
        "role": "Врач-нарколог",
        "photo": "images/help-doctor-male-1.png",
        "keys": ("visit", "ambulance", "zapoy", "withdrawal", "ubod", "sober", "detox", "help", "toxicologist", "drugtest"),
    },
    {
        "name": "Волков Андрей Сергеевич",
        "role": "Врач-нарколог",
        "photo": "images/help-doctor-male-2.png",
        "keys": ("alcohol", "code", "decode", "drugs"),
    },
    {
        "name": "Сафонова Елена Викторовна",
        "role": "Психиатр-нарколог, к.м.н.",
        "photo": "images/help-doctor-female-1.png",
        "keys": ("psychiatry", "psy-", "dementia", "alzheimer"),
    },
    {
        "name": "Орлова Мария Дмитриевна",
        "role": "Психотерапевт",
        "photo": "images/help-doctor-female-2.png",
        "keys": ("rehab", "family", "gambling", "betting", "consult", "check"),
    },
]

ARR = '<span class="arr"><svg viewBox="0 0 14 14" fill="none"><path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'

PHONE_BTN = (
    '<a class="btn btn--line" href="tel:+78001001212" data-city-tel>'
    'Позвонить: <span data-city-phone>8 800 100-12-12</span></a>'
)

CTA_CALL = (
    f'<a class="btn btn--ghost-light" href="tel:+78001001212" data-city-tel>'
    f'Позвонить: <span data-city-phone>8 800 100-12-12</span></a>'
)


def pick_doctor(filename: str) -> dict:
    stem = filename.replace(".html", "").lower()
    for d in DOCTORS:
        for key in d["keys"]:
            if key in stem:
                return d
    # stable fallback by hash
    idx = int(hashlib.md5(stem.encode()).hexdigest(), 16) % len(DOCTORS)
    return DOCTORS[idx]


def help_block(doc: dict) -> str:
    return (
        '<div class="svc-help" data-svc-help>\n'
        '          <p class="svc-help__title">Вам поможет</p>\n'
        '          <div class="svc-help__card">\n'
        f'            <img class="svc-help__photo" src="{doc["photo"]}" alt="{doc["name"]}" width="144" height="144" loading="lazy" decoding="async">\n'
        "            <div>\n"
        f'              <p class="svc-help__name">{doc["name"]}</p>\n'
        f'              <p class="svc-help__role">{doc["role"]}</p>\n'
        "            </div>\n"
        "          </div>\n"
        f'          <a class="btn btn--blue" href="#" data-open-modal>Оставить заявку {ARR}</a>\n'
        "        </div>\n        "
    )


def page_topic(html: str, filename: str) -> str:
    m = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", html, re.I)
    if m:
        t = re.sub(r"<[^>]+>", " ", m.group(1))
        t = re.sub(r"\s+", " ", t).strip()
        if t:
            return t
    title = re.search(r"<title>([^<]+)</title>", html, re.I)
    if title:
        return title.group(1).replace("— Альба", "").replace("| Альба", "").strip()
    return filename.replace("service-", "").replace(".html", "").replace("-", " ")


def faq_items(topic: str) -> list[tuple[str, str]]:
    t = topic
    return [
        (f"Что входит в программу «{t}»?", f"Состав зависит от состояния: осмотр, план помощи, медикаментозная поддержка по показаниям и понятный следующий шаг. Точный объём для «{t}» врач называет после консультации."),
        (f"Сколько стоит «{t}»?", "На сайте указана ориентировочная стоимость. Итоговая цена зависит от формата (дом, приём, стационар), длительности и объёма процедур — после оценки состояния."),
        ("Это анонимно?", "Да. Обращение добровольное, 18+. Можно начать с псевдонима. Без постановки на диспансерный учёт в частном формате."),
        ("Можно ли вызвать врача на дом?", "Да, при показаниях организуем выезд. Если безопаснее стационар — скажем прямо и поможем с маршрутом."),
        ("Работаете круглосуточно?", "Дежурная линия 24/7. Срочные форматы доступны ночью и в выходные; плановые приёмы — по записи."),
        ("Нужно ли направление?", "Нет. Можно позвонить или оставить заявку. Для части процедур нужен осмотр и согласие пациента."),
        ("Что взять с собой в клинику?", "Документ, список лекарств, контакты близких по желанию. Подробный чек-лист подскажет администратор."),
        ("Можно ли лечиться без родственников?", "Да. Родственников подключаем только с согласия пациента, кроме ситуаций угрозы жизни."),
        ("Есть ли противопоказания?", "Да. Имеются противопоказания. Часть методов нельзя начинать при остром опьянении, тяжёлой соматике или без согласия."),
        ("Это скорая помощь?", "Нет, это частная медицинская помощь. При угрозе жизни вызывайте 103."),
        (f"Чем «{t}» отличается от детокса?", "Детокс — стабилизация острого состояния. Программа «{t}» может включать детокс, но фокус — на маршруте помощи под задачу страницы."),
        ("Сколько длится лечение?", "От нескольких часов (выезд/капельница) до недель в стационаре/реабилитации. Срок подбирают после осмотра."),
        ("Можно ли оплатить частями?", "Условия оплаты уточняйте у администратора. Иногда доступна поэтапная оплата по этапам помощи."),
        ("Выдаёте ли справки?", "При необходимости — медицинские документы по факту оказанной помощи. Условия сообщим на консультации."),
        ("Можно ли совмещать с работой?", "Амбулаторный формат часто совместим. При стационаре нужен перерыв — врач оценит риски."),
        ("Как подготовить человека к разговору?", "Без ультиматумов и ярлыков. Дежурный подскажет, как говорить спокойно и какой формат возможен добровольно."),
        ("Есть ли женские/мужские программы?", "Маршрут индивидуальный. При необходимости учитываем особенности и запрос семьи."),
        ("Что после выписки?", "План наблюдения, контакты дежурного, рекомендации по срыву и поддержке. Следующий шаг — по готовности человека."),
        ("Можно ли пройти онлайн-консультацию?", "Для части запросов — да, как первый ориентир. Острый риск и процедуры требуют очного осмотра."),
        ("Как быстро перезвоните?", "Обычно в ближайшие минуты в рабочем контуре дежурного. Оставьте номер — перезвоним сами."),
    ]


def render_faq(topic: str) -> str:
    items = faq_items(topic)
    parts = []
    for i, (q, a) in enumerate(items):
        open_cls = " is-open" if i == 0 else ""
        parts.append(
            f'<article class="acc__item{open_cls}">'
            f'<button class="acc__btn" type="button">{q}<i>+</i></button>'
            f'<div class="acc__panel"><div><p>{a}</p></div></div>'
            f"</article>"
        )
    body = "".join(parts)
    return (
        '<section class="faq wrap" data-page-faq>\n'
        '      <div data-reveal><h2 class="section-title">Часто задаваемые<br>вопросы</h2>'
        f"<p>Ответы по теме «{topic}». Если остались сомнения — позвоните дежурному.</p></div>\n"
        f'      <div class="acc" data-acc data-reveal>{body}</div>\n'
        "    </section>\n"
    )


def ensure_help(html: str, filename: str) -> str:
    if "data-svc-help" in html:
        return html
    doc = pick_doctor(filename)
    block = help_block(doc)
    # Insert before <h2>Что входит</h2>
    html2, n = re.subn(
        r"(<h2>\s*Что входит\s*</h2>)",
        block + r"\1",
        html,
        count=1,
        flags=re.I,
    )
    if n:
        return html2
    return html


def ensure_phone_btns(html: str) -> str:
    # svc-side / sticky phone buttons
    html = re.sub(
        r'<a class="btn btn--line" href="tel:\+78001001212"[^>]*>\s*Позвонить(?:\s*:?\s*<span[^>]*>[^<]*</span>)?\s*</a>',
        PHONE_BTN,
        html,
        flags=re.I,
    )
    html = re.sub(
        r'(<a class="btn btn--line" href="tel:\+78001001212"[^>]*>)\s*Позвонить\s*(</a>)',
        r"\1Позвонить: <span data-city-phone>8 800 100-12-12</span>\2",
        html,
        flags=re.I,
    )
    return html


def ensure_cta_call(html: str) -> str:
    # Wrap CTA primary button + add call if missing
    def repl_box(m: re.Match) -> str:
        box = m.group(0)
        if "cta__actions" in box:
            if "btn--ghost-light" in box or "Позвонить:" in box:
                return box
            # already wrapped but no call
            return box.replace(
                "</div>\n    </section>",
                CTA_CALL + "</div>\n    </section>",
                1,
            ) if False else box

        # Find last btn in cta__box (primary action)
        btn_pat = re.compile(
            r'(<a class="btn btn--(?:light|blue|dark)"[^>]*>[\s\S]*?</a>)',
            re.I,
        )
        btns = list(btn_pat.finditer(box))
        if not btns:
            return box
        last = btns[-1]
        btn_html = last.group(1)
        # Normalize label to Оставить заявку when it's Записаться in CTA
        btn_html2 = re.sub(
            r"(>)\s*Записаться\s*",
            r"\1Оставить заявку ",
            btn_html,
            count=1,
        )
        actions = f'<div class="cta__actions">{btn_html2}{CTA_CALL}</div>'
        new_box = box[: last.start()] + actions + box[last.end() :]
        return new_box

    return re.sub(
        r'<div class="cta__box"[^>]*>[\s\S]*?</div>\s*(?=</section>)',
        repl_box,
        html,
        flags=re.I,
    )


def ensure_faq(html: str, topic: str) -> str:
    block = render_faq(topic)
    if 'data-page-faq' in html or re.search(r'class="faq\b', html):
        # replace existing faq section
        html2, n = re.subn(
            r'<section class="faq\b[\s\S]*?</section>',
            block.strip(),
            html,
            count=1,
            flags=re.I,
        )
        if n:
            return html2
    # insert before CTA or before </main>
    m = re.search(r'<section class="cta\b', html, re.I)
    if m:
        return html[: m.start()] + block + html[m.start() :]
    return html.replace("</main>", block + "  </main>", 1)


def article_plain_len(html: str) -> int:
    m = re.search(r'<div class="svc-article">([\s\S]*?)</div>\s*<aside', html)
    if not m:
        return -1
    text = re.sub(r"<[^>]+>", " ", m.group(1))
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def pad_article(html: str, topic: str) -> str:
    length = article_plain_len(html)
    if length < 0:
        return html
    if length >= 1000:
        return html
    need = 1000 - length + 80
    seo = (
        f"<p>Страница «{topic}» в клинике Альба — ориентир для семьи и пациента: добровольно, 18+, без обещаний «навсегда». "
        f"Мы разбираем, когда нужна срочная стабилизация, когда достаточно амбулаторного приёма и когда безопаснее палата. "
        f"В разговоре о «{topic}» важны симптомы, срок проблемы, сопутствующие болезни и согласие человека. "
        "Стоимость на сайте ориентировочная: точный объём процедур и формат помощи врач называет после осмотра. "
        "Анонимность сохраняем в частном контуре; при угрозе жизни направляем в экстренную службу 103. "
        "После острого этапа фиксируем план: куда звонить при ухудшении, какие шаги разумны через несколько дней, "
        "нужны ли детокс, психотерапия, семейная встреча или стационарное наблюдение. "
        "Имеются противопоказания — часть методов нельзя начинать без стабилизации и информированного согласия.</p>"
    )
    # trim/extend roughly
    while len(re.sub(r"<[^>]+>", " ", seo)) < need:
        seo += (
            f"<p>Если сомневаетесь, подходит ли «{topic}», начните с короткого звонка дежурному: "
            "подскажем формат, подготовку и ориентир по цене без давления.</p>"
        )
    html2, n = re.subn(
        r'(<div class="svc-article">)',
        r"\1\n" + seo + "\n",
        html,
        count=1,
    )
    return html2 if n else html


def process_service(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    topic = page_topic(html, path.name)
    before = html
    html = ensure_help(html, path.name)
    html = ensure_phone_btns(html)
    html = ensure_cta_call(html)
    html = ensure_faq(html, topic)
    html = pad_article(html, topic)
    changed = html != before
    if changed:
        path.write_text(html, encoding="utf-8")
    return {
        "file": path.name,
        "changed": changed,
        "chars": article_plain_len(html),
        "faq": len(re.findall(r"acc__item", html)),
        "help": "data-svc-help" in html,
    }


def process_simple_faq_cta(path: Path, topic: str | None = None) -> dict:
    html = path.read_text(encoding="utf-8")
    before = html
    if topic is None:
        topic = page_topic(html, path.name)
    html = ensure_cta_call(html)
    html = ensure_faq(html, topic)
    changed = html != before
    if changed:
        path.write_text(html, encoding="utf-8")
    return {"file": path.name, "changed": changed, "faq": len(re.findall(r"acc__item", html))}


TEMPLATE_EXTRA = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__TITLE__ — Альба</title>
  <meta name="description" content="__DESC__">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><path fill='%234f84ff' d='M16 1.8c1.7 5.6 5.8 9.7 11.4 11.4C21.8 15 17.7 19.1 16 24.7 14.3 19.1 10.2 15 4.6 13.2 10.2 11.5 14.3 7.4 16 1.8Z'/></svg>">
</head>
<body>
  <div class="preloader" aria-hidden="true"><div class="preloader__inner"><svg class="logo__mark" viewBox="0 0 32 32"><path fill="currentColor" d="M16 1.8c1.7 5.6 5.8 9.7 11.4 11.4C21.8 15 17.7 19.1 16 24.7 14.3 19.1 10.2 15 4.6 13.2 10.2 11.5 14.3 7.4 16 1.8Z"/></svg><div class="preloader__bar"><span></span></div></div></div>
  <header class="header" data-header>
    <div class="header__bar wrap">
      <a class="logo" href="index.html"><svg class="logo__mark" viewBox="0 0 32 32"><path fill="currentColor" d="M16 1.8c1.7 5.6 5.8 9.7 11.4 11.4C21.8 15 17.7 19.1 16 24.7 14.3 19.1 10.2 15 4.6 13.2 10.2 11.5 14.3 7.4 16 1.8Z"/></svg><span class="logo__text">Альба</span></a>
      <nav class="nav" aria-label="Основное меню">
        <div class="nav__drop">
          <button class="nav__btn" type="button">Клиника <svg viewBox="0 0 12 12" fill="none"><path d="M2 4.5 6 8.5 10 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button>
          <div class="nav__menu">
            <a href="about.html">О нас</a>
            <a href="gallery.html">Галерея</a>
            <a href="links.html">Полезные ссылки</a>
            <a href="licenses.html">Лицензии</a>
            <a href="prices.html">Цены</a>
            <a href="about.html#anon">Анонимность</a>
          </div>
        </div>
        <div class="nav__drop">
          <button class="nav__btn" type="button">Программы <svg viewBox="0 0 12 12" fill="none"><path d="M2 4.5 6 8.5 10 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button>
          <div class="nav__menu">
            <a class="nav__catalog" href="programs.html">Весь каталог</a>
            <a href="service-psychiatry.html">Психиатрия</a>
            <a href="service-dementia.html">Лечение деменции</a>
            <a href="service-alzheimer.html">Лечение альцгеймера</a>
          </div>
        </div>
        <a href="doctors.html">Врачи</a>
        <a href="articles.html">Статьи</a>
        <a href="contacts.html">Контакты</a>
      </nav>
      <div class="header__actions">
        <a class="icon-btn icon-btn--msg" href="https://max.ru/" data-city-max target="_blank" rel="noopener" aria-label="Max"><img class="icon-max" src="images/Max_logo.svg" alt="" width="18" height="18" decoding="async"></a>
        <a class="icon-btn icon-btn--msg" href="https://t.me/+78001001212" data-city-tg target="_blank" rel="noopener" aria-label="Telegram"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.43 4.53 3.87 11.32c-1.2.47-1.19 1.13-.22 1.43l4.5 1.4 10.45-6.59c.5-.3.95-.13.58.18l-8.46 7.63-.33 4.72c.48 0 .69-.22.96-.48l2.3-2.24 4.78 3.53c.88.48 1.51.23 1.73-.81l3.13-14.74c.32-1.28-.49-1.86-1.36-1.42Z"/></svg></a>
        <a class="icon-btn" href="tel:+78001001212" data-city-tel aria-label="Позвонить"><span class="icon-phone" aria-hidden="true"></span></a>
        <a class="btn btn--dark" href="#" data-open-modal>Записаться <span class="arr"><svg viewBox="0 0 14 14" fill="none"><path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>
        <button class="burger" type="button" data-burger aria-label="Открыть меню"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
  <nav class="mnav" data-mnav>
    <a href="about.html">О нас</a>
    <a href="gallery.html">Галерея</a>
    <a href="links.html">Полезные ссылки</a>
    <a href="licenses.html">Лицензии</a>
    <a href="prices.html">Цены</a>
    <a href="programs.html">Программы</a>
    <a href="about.html#anon">Анонимность</a>
    <a href="doctors.html">Врачи</a>
    <a href="articles.html">Статьи</a>
    <a href="contacts.html">Контакты</a>
  </nav>

  <main>
    <section class="page-hero wrap">
      <div class="page-hero__box">
        <div>
          <div class="crumb"><a href="index.html">Главная</a> / <a href="service-psychiatry.html">Психиатрия</a> / __CRUMB__</div>
          <h1 class="split">__H1__</h1>
        </div>
        <p>__LEAD__</p>
      </div>
    </section>
    <section class="svc wrap">
      <div data-reveal>
        <img class="article-cover" src="images/clinic-consult.jpg" alt="" loading="lazy">
        <p>__INTRO__</p>
        <div class="svc-help" data-svc-help>
          <p class="svc-help__title">Вам поможет</p>
          <div class="svc-help__card">
            <img class="svc-help__photo" src="images/help-doctor-female-1.png" alt="Сафонова Елена Викторовна" width="144" height="144" loading="lazy" decoding="async">
            <div>
              <p class="svc-help__name">Сафонова Елена Викторовна</p>
              <p class="svc-help__role">Психиатр-нарколог, к.м.н.</p>
            </div>
          </div>
          <a class="btn btn--blue" href="#" data-open-modal>Оставить заявку <span class="arr"><svg viewBox="0 0 14 14" fill="none"><path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>
        </div>
        <h2>Что входит</h2>
        <ul><li>Консультация психиатра</li><li>Оценка когнитивного статуса и безопасности</li><li>План наблюдения для семьи</li><li>Связка с неврологом по показаниям</li><li>18+, добровольно</li></ul>
      </div>
      <aside class="svc-side" data-reveal>
        <span>Стоимость</span>
        <b>от 4 900 ₽</b>
        <em>консультация</em>
        <a class="btn btn--dark" href="#" data-open-modal>Записаться <span class="arr"><svg viewBox="0 0 14 14" fill="none"><path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>
        <a class="btn btn--line" href="tel:+78001001212" data-city-tel>Позвонить: <span data-city-phone>8 800 100-12-12</span></a>
        <p>Имеются противопоказания. Нужна консультация врача.</p>
      </aside>
    </section>

    <section class="svc-layout wrap" data-reveal>
      <div class="svc-article">
        <p>__SEO__</p>
        <h2>Когда стоит обратиться</h2>
        <p>Имеет смысл звонить, если появились забывчивость с риском для безопасности, спутанность, ночные блуждания, отказ от еды или лекарств, сильная нагрузка на семью. Мы не обещаем «вылечить навсегда» — помогаем оценить состояние и выбрать безопасный формат помощи.</p>
        <ul>
          <li>Нужен ориентир по формату и стоимости до визита</li>
          <li>Важны анонимность и добровольный формат (18+)</li>
          <li>Семья не знает, как организовать уход без давления</li>
          <li>После острого эпизода нужен понятный следующий шаг</li>
        </ul>
        <h2>Как проходит помощь</h2>
        <h3>Оценка состояния</h3>
        <p>Врач уточняет жалобы, динамику памяти и поведения, соматику, лекарства и согласие. Без осмотра не назначаем «универсальные схемы».</p>
        <h3>План для пациента и семьи</h3>
        <p>Фиксируем, что делать при ухудшении, как снизить риски дома, когда нужен стационар или узкий специалист.</p>
        <h3>Наблюдение</h3>
        <p>По показаниям — повторные консультации, коррекция терапии, связь с неврологом и поддержка родственников.</p>
        <h2>Противопоказания</h2>
        <p>Имеются противопоказания. Часть вмешательств нельзя начинать при остром психозе без оценки, тяжёлой соматике или без согласия законного представителя, когда это требуется по ситуации. Точные ограничения называет врач.</p>
        <h2>После консультации</h2>
        <p>Сохраняйте контакт дежурного. Если усилились спутанность, агрессия, падения или отказ от помощи — лучше позвонить рано. Следующим шагом могут быть наблюдение, семейная встреча или маршрутизация в профильный стационар.</p>
      </div>
      <aside class="svc-sticky">
        <div class="svc-sticky__card">
          <h3>Нужна помощь семье?</h3>
          <p>Дежурный подскажет, с чего начать разговор и какой формат возможен добровольно.</p>
          <a class="btn btn--blue" href="#" data-open-modal>Получить совет <span class="arr"><svg viewBox="0 0 14 14" fill="none"><path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>
        </div>
      </aside>
    </section>

    <section class="cta wrap">
      <div class="cta__box" data-reveal="scale">
        <div><h2>Подскажем формат помощи</h2><p>Дежурный врач на связи 24/7. Можно не называть имя.</p></div>
        <div class="cta__actions">
          <a class="btn btn--light" href="#" data-open-modal>Оставить заявку <span class="arr"><svg viewBox="0 0 14 14" fill="none"><path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>
          <a class="btn btn--ghost-light" href="tel:+78001001212" data-city-tel>Позвонить: <span data-city-phone>8 800 100-12-12</span></a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="wrap">
      <div class="footer__grid">
        <div>
          <a class="logo" href="index.html"><svg class="logo__mark" viewBox="0 0 32 32"><path fill="currentColor" d="M16 1.8c1.7 5.6 5.8 9.7 11.4 11.4C21.8 15 17.7 19.1 16 24.7 14.3 19.1 10.2 15 4.6 13.2 10.2 11.5 14.3 7.4 16 1.8Z"/></svg><span class="logo__text">Альба</span></a>
          <p>Премиальная наркологическая клиника. Анонимное лечение зависимостей <span data-city-prep>в Омске</span>.</p>
        </div>
        <div>
          <h4>Клиника</h4>
          <ul>
            <li><a href="about.html">О нас</a></li>
            <li><a href="gallery.html">Галерея</a></li>
            <li><a href="links.html">Полезные ссылки</a></li>
            <li><a href="licenses.html">Лицензии</a></li>
            <li><a href="prices.html">Цены</a></li>
            <li><a href="doctors.html">Врачи</a></li>
            <li><a href="articles.html">Статьи</a></li>
          </ul>
        </div>
        <div>
          <h4>Программы</h4>
          <ul>
            <li><a href="programs.html">Каталог</a></li>
            <li><a href="service-psychiatry.html">Психиатрия</a></li>
            <li><a href="service-dementia.html">Лечение деменции</a></li>
            <li><a href="service-alzheimer.html">Лечение альцгеймера</a></li>
          </ul>
        </div>
        <div><h4>Связь 24/7</h4><a class="footer__phone" href="tel:+78001001212" data-city-tel><span data-city-phone>8 800 100-12-12</span></a>
          <div class="footer__msg">
            <a href="https://max.ru/" data-city-max target="_blank" rel="noopener" aria-label="Max"><img class="icon-max" src="images/Max_logo.svg" alt="" width="18" height="18" decoding="async"></a>
            <a href="https://t.me/+78001001212" data-city-tg target="_blank" rel="noopener" aria-label="Telegram"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.43 4.53 3.87 11.32c-1.2.47-1.19 1.13-.22 1.43l4.5 1.4 10.45-6.59c.5-.3.95-.13.58.18l-8.46 7.63-.33 4.72c.48 0 .69-.22.96-.48l2.3-2.24 4.78 3.53c.88.48 1.51.23 1.73-.81l3.13-14.74c.32-1.28-.49-1.86-1.36-1.42Z"/></svg></a>
          </div>
          <p><span data-city-address>Омск, ул. Ленина, 12</span><br>Лицензия <span data-city-license>ЛО-55-01-002891</span></p>
        </div>
      </div>
      <div class="footer__copy">
        <a class="footer__made" href="https://cursiva.ru/" target="_blank" rel="noopener" aria-label="Создание сайта — веб-студия Cursiva">Создание сайта - <img src="images/cursiva-logo-white.png" alt="Cursiva" width="92" height="28" decoding="async"></a>
        <span>© <span data-year></span> ООО «Альба Медикал». 18+. Имеются противопоказания. Необходима консультация специалиста.</span>
        <span class="footer__legal">
          <a href="privacy.html">Политика ПДн</a>
          <a href="consent.html">Согласие</a>
          <a href="terms.html">Условия</a>
          <a href="legal.html">Реквизиты</a>
          <a href="links.html">Полезные ссылки</a>
          <a href="sitemap.html">Карта сайта</a>
        </span>
      </div>
    </div>
  </footer>
  <div class="modal" data-modal>
    <div class="modal__box form">
      <button class="modal__close" type="button" data-close-modal aria-label="Закрыть">×</button>
      <h2>Запись на консультацию</h2>
      <p>Оставьте номер — перезвоним за 2 минуты. Имя можно не указывать.</p>
      <form data-form>
        <div class="form__fields">
          <label for="m-name">Как к вам обращаться</label>
          <input id="m-name" name="name" type="text" placeholder="Имя или псевдоним" autocomplete="name">
          <label for="m-phone">Телефон</label>
          <input id="m-phone" name="phone" type="tel" placeholder="+7 (" required autocomplete="tel">
          <label for="m-prog">Программа</label>
          <select id="m-prog" name="program">
            <option>Пока не знаю — подскажет врач</option>
            <option>Лечение деменции</option>
            <option>Лечение альцгеймера</option>
            <option>Психиатрия</option>
          </select>
          <button class="btn btn--blue" type="submit">Жду звонка <span class="arr"><svg viewBox="0 0 14 14" fill="none"><path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button>
        </div>
        <div class="form__ok">Заявка принята. Дежурный врач перезвонит с номера клиники.</div>
      </form>
    </div>
  </div>
  <script src="js/main.js"></script>
</body>
</html>
"""


def write_new_service(filename: str, meta: dict) -> None:
    html = TEMPLATE_EXTRA
    for k, v in meta.items():
        html = html.replace(f"__{k}__", v)
    path = ROOT / filename
    path.write_text(html, encoding="utf-8")
    # ensure FAQ via processor
    process_service(path)


def main() -> None:
    write_new_service(
        "service-dementia.html",
        {
            "TITLE": "Лечение деменции",
            "DESC": "Лечение и сопровождение при деменции в клинике Альба: оценка состояния, безопасность дома, план для семьи. 18+, добровольно.",
            "CRUMB": "Лечение деменции",
            "H1": "Лечение деменции:<br>сначала безопасность",
            "LEAD": "Оцениваем когнитивное состояние, риски дома и нагрузку на семью. Без обещаний «вернуть память навсегда».",
            "INTRO": "Лечение деменции в Альбе — это не «укол с порога», а спокойная оценка памяти, поведения, соматики и безопасности. Помогаем семье понять, что делать сегодня и какой формат наблюдения уместен.",
            "SEO": "Лечение деменции в частной клинике Альба направлено на безопасность пациента и поддержку семьи. На консультации разбираем забывчивость, спутанность, нарушения сна, отказ от помощи и риски падений. Врач уточняет лекарства, сопутствующие болезни и согласие на помощь. Мы не обещаем чудесного восстановления памяти: задача — снизить риски, подобрать наблюдение и объяснить родственникам понятный маршрут. Формат может быть амбулаторным или стационарным по показаниям. Стоимость ориентировочная, точный объём называется после осмотра. Обращение добровольное, 18+. Имеются противопоказания. При угрозе жизни вызывайте 103.",
        },
    )
    write_new_service(
        "service-alzheimer.html",
        {
            "TITLE": "Лечение альцгеймера",
            "DESC": "Лечение болезни Альцгеймера в клинике Альба: диагностика состояния, план наблюдения, поддержка семьи. 18+, добровольно.",
            "CRUMB": "Лечение альцгеймера",
            "H1": "Лечение альцгеймера:<br>маршрут без давления",
            "LEAD": "Помогаем оценить симптомы, безопасность и уход. Честно говорим о возможностях терапии и роли семьи.",
            "INTRO": "Лечение болезни Альцгеймера в Альбе начинается с бережной оценки: память, ориентация, поведение, сон и риски дома. Вместе с семьёй собираем план наблюдения и решаем, нужен ли узкий специалист или стационар.",
            "SEO": "Лечение альцгеймера в клинике Альба — консультативная и сопровождающая помощь для взрослых пациентов и их близких. На приёме обсуждаем ранние и поздние проявления, безопасность быта, лекарственную нагрузку и признаки ухудшения, при которых нельзя ждать. Мы не подменяем неврологический маршрут рекламными обещаниями: объясняем, что можно сделать сейчас, какие обследования разумны и как снизить конфликт дома. Помощь добровольная, 18+. Стоимость консультации ориентировочная. Имеются противопоказания. Экстренные состояния — повод вызвать 103.",
        },
    )

    results = []
    for path in sorted(ROOT.glob("service-*.html")):
        results.append(process_service(path))

    results.append(process_simple_faq_cta(ROOT / "programs.html", "программы клиники Альба"))
    results.append(process_simple_faq_cta(ROOT / "index.html", "лечение зависимостей в Альбе"))

    changed = sum(1 for r in results if r.get("changed"))
    helps = sum(1 for r in results if r.get("help"))
    short = [r for r in results if r.get("chars", 9999) >= 0 and r.get("chars", 9999) < 1000]
    print(f"processed={len(results)} changed={changed} with_help={helps} short_articles={len(short)}")
    if short:
        print("short:", short[:10])


if __name__ == "__main__":
    main()
