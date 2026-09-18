# -*- coding: utf-8 -*-
"""Generate concrete alcoholism / zapoy stationary programs + inject hub blocks."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ARR = (
    '<span class="arr"><svg viewBox="0 0 14 14" fill="none">'
    '<path d="M3 7h8M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.7" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
)

PROGRAMS = [
    {
        "file": "service-zapoy-1day.html",
        "days": 1,
        "title": "Вывод из запоя 1 день в стационаре",
        "h1": "Вывод из запоя<br>1 день в стационаре",
        "price": "от 8 900 ₽",
        "lead": "Сутки наблюдения: осмотр, утренняя и вечерняя капельница, контроль давления и пост медсестры.",
        "for_whom": "Короткий запой, относительно стабильное состояние, нужна быстрая детоксикация под контролем.",
        "schedule": [
            {
                "title": "День 1 — стабилизация",
                "morning": [
                    "Госпитализация, осмотр нарколога, измерение давления и пульса",
                    "При необходимости ЭКГ и экспресс-оценка соматики",
                    "Утренняя капельница: детоксикация, электролиты, витамины группы B",
                    "Препараты от тошноты, тревоги и головной боли — по показаниям",
                ],
                "day": [
                    "Наблюдение на посту медсестры",
                    "Питьё, щадящее питание по состоянию",
                    "Коррекция терапии после повторного осмотра",
                ],
                "evening": [
                    "Вечерняя капельница: поддержка печени, восстановление жидкости, седация по показаниям",
                    "Подготовка ко сну, контроль ночных показателей",
                    "План на выписку или продление курса, если состояние требует",
                ],
            }
        ],
    },
    {
        "file": "service-zapoy-2days.html",
        "days": 2,
        "title": "Вывод из запоя — курс 2 дня",
        "h1": "Вывод из запоя<br>курс 2 дня",
        "price": "от 16 900 ₽",
        "lead": "Двое суток в палате: две капельницы в день, наблюдение 24/7 и понятный план для семьи.",
        "for_whom": "Запой несколько суток, выраженная слабость, давление «скачет», дома оставаться рискованно.",
        "schedule": [
            {
                "title": "День 1 — снятие острой интоксикации",
                "morning": [
                    "Осмотр, размещение в палате, тонометрия",
                    "Утренняя капельница детоксикации",
                    "Купирование абстинентных симптомов по протоколу врача",
                ],
                "day": [
                    "Контроль самочувствия, сон по возможности",
                    "Инъекции / таблетированная поддержка по показаниям",
                ],
                "evening": [
                    "Вечерняя капельница",
                    "Нормализация сна, ночное наблюдение",
                ],
            },
            {
                "title": "День 2 — закрепление и выписка",
                "morning": [
                    "Утренний обход, повторные показатели",
                    "Утренняя капельница с гепатопротекцией и витаминами",
                ],
                "day": [
                    "Оценка готовности к выписке",
                    "Разговор о следующем шаге: кодирование только после стабилизации",
                ],
                "evening": [
                    "Вечерняя капельница при необходимости или поддерживающая терапия",
                    "Рекомендации семье, контакт дежурного 24/7",
                ],
            },
        ],
    },
    {
        "file": "service-zapoy-3days.html",
        "days": 3,
        "title": "Вывод из запоя — курс 3 дня",
        "h1": "Вывод из запоя<br>курс 3 дня",
        "price": "от 24 900 ₽",
        "lead": "Стандартный стационарный курс: утро и вечер капельница, восстановление сна и давления.",
        "for_whom": "Запой средней тяжести, нужна полноценная детоксикация без спешки «за один вечер».",
        "schedule": [
            {
                "title": "День 1 — детокс и безопасность",
                "morning": [
                    "Госпитализация, осмотр, тонометр, при необходимости ЭКГ",
                    "Утренняя капельница (детокс + электролиты + витамины B)",
                ],
                "day": [
                    "Наблюдение, симптоматическая терапия",
                    "Щадящий режим, контроль питья",
                ],
                "evening": [
                    "Вечерняя капельница",
                    "Седация и сон по показаниям, пост 24/7",
                ],
            },
            {
                "title": "День 2 — восстановление органов и нервной системы",
                "morning": [
                    "Обход врача, коррекция схемы",
                    "Утренняя капельница: гепатопротекция, кардиоподдержка по показаниям",
                ],
                "day": [
                    "Снижение тревоги и тремора",
                    "Питание, отдых, повторные измерения давления",
                ],
                "evening": [
                    "Вечерняя капельница",
                    "Работа со сном, ночное наблюдение",
                ],
            },
            {
                "title": "День 3 — стабилизация и план дальше",
                "morning": [
                    "Утренняя капельница поддерживающего состава",
                    "Оценка динамики: давление, сознание, сон, аппетит",
                ],
                "day": [
                    "Консультация о следующем этапе (амбулаторно / кодирование / семья)",
                    "Выписка при стабильных показателях",
                ],
                "evening": [
                    "При продлении — вечерняя инфузия; иначе — рекомендации и связь с дежурным",
                ],
            },
        ],
    },
    {
        "file": "service-zapoy-5days.html",
        "days": 5,
        "title": "Вывод из запоя — курс 5 дней",
        "h1": "Вывод из запоя<br>курс 5 дней",
        "price": "от 39 900 ₽",
        "lead": "Расширенный детокс: интенсивные первые сутки, затем поддержка и восстановление режима.",
        "for_whom": "Длительный запой, соматические жалобы, нужна пауза от триггеров дома.",
        "schedule": [
            {
                "title": "Дни 1–2 — интенсивная детоксикация",
                "morning": [
                    "Ежедневный обход, контроль давления и пульса",
                    "Утренняя капельница усиленного состава",
                ],
                "day": [
                    "Купирование абстиненции, защита печени и сердца по показаниям",
                    "Пост медсестры, помощь с питанием и режимом",
                ],
                "evening": [
                    "Вечерняя капельница",
                    "Нормализация сна, ночной мониторинг",
                ],
            },
            {
                "title": "Дни 3–4 — восстановление",
                "morning": [
                    "Утренняя капельница поддерживающего объёма",
                    "Коррекция витаминов, электролитов, седации",
                ],
                "day": [
                    "Стабилизация давления и самочувствия",
                    "Короткая мотивационная беседа / план для семьи по согласию",
                ],
                "evening": [
                    "Вечерняя капельница или таблетированная поддержка — по динамике",
                ],
            },
            {
                "title": "День 5 — выписка и маршрут дальше",
                "morning": [
                    "Финальный осмотр, утренняя поддержка по показаниям",
                ],
                "day": [
                    "Рекомендации после выписки, контакт 24/7",
                    "Обсуждение кодирования только при стабильном состоянии",
                ],
                "evening": [
                    "Выписка в светлое время или продление курса при необходимости",
                ],
            },
        ],
    },
    {
        "file": "service-zapoy-7days.html",
        "days": 7,
        "title": "Вывод из запоя — курс 7 дней",
        "h1": "Вывод из запоя<br>курс 7 дней",
        "price": "от 54 900 ₽",
        "lead": "Полная неделя в стационаре: детокс, восстановление, наблюдение и спокойный выход без срыва в первые сутки дома.",
        "for_whom": "Тяжёлый или повторный запой, сопутствующие риски, нужна длительная стабилизация.",
        "schedule": [
            {
                "title": "Дни 1–3 — активный детокс",
                "morning": [
                    "Обход нарколога, тонометрия",
                    "Утренняя капельница (детокс, электролиты, витамины B)",
                ],
                "day": [
                    "Симптоматическая терапия, контроль осложнений",
                    "Режим палаты, пост 24/7",
                ],
                "evening": [
                    "Вечерняя капельница",
                    "Сон и ночное наблюдение",
                ],
            },
            {
                "title": "Дни 4–5 — поддержка и восстановление",
                "morning": [
                    "Утренняя капельница мягче по объёму — по самочувствию",
                    "Гепато- и кардиоподдержка по показаниям",
                ],
                "day": [
                    "Стабилизация сна, аппетита, давления",
                    "Разговор о триггерах срыва и поддержке семьи",
                ],
                "evening": [
                    "Вечерняя инфузия или пероральная схема",
                ],
            },
            {
                "title": "Дни 6–7 — закрепление и выписка",
                "morning": [
                    "Контрольный осмотр, утренняя поддержка при необходимости",
                ],
                "day": [
                    "План после выписки: амбулаторно, кодирование, реабилитация — без давления",
                    "Инструктаж близким",
                ],
                "evening": [
                    "Выписка при стабильных показателях или продление по решению врача",
                ],
            },
        ],
    },
]


def li(items: list[str]) -> str:
    return "".join(f"<li>{x}</li>" for x in items)


def schedule_html(schedule: list[dict]) -> str:
    parts = []
    for day in schedule:
        parts.append(
            f'<article class="prog-day">'
            f'<h3>{day["title"]}</h3>'
            f'<div class="prog-day__cols">'
            f'<div><h4>Утро</h4><ul>{li(day["morning"])}</ul></div>'
            f'<div><h4>День</h4><ul>{li(day["day"])}</ul></div>'
            f'<div><h4>Вечер</h4><ul>{li(day["evening"])}</ul></div>'
            f"</div></article>"
        )
    return "\n          ".join(parts)


WARD_FUND = f"""
    <section class="ward-fund wrap" data-reveal id="ward-fund">
      <div class="ward-fund__head">
        <h2 class="section-title">Палатный фонд<br>клиники</h2>
        <p>В стационаре 5 двухместных палат и 1 палата премиум. Размещение 1–2 места, круглосуточный пост медсестры.</p>
      </div>
      <div class="ward-fund__grid">
        <article>
          <span class="ward-fund__badge">5 палат</span>
          <h3>Двухместные палаты</h3>
          <ul>
            <li>5 двухместных палат в отделении</li>
            <li>Возможно 1–2 местное размещение</li>
            <li>Спокойный режим, без «проходного» коридора</li>
          </ul>
        </article>
        <article class="ward-fund__feat">
          <span class="ward-fund__badge">Премиум</span>
          <h3>1 палата премиум</h3>
          <ul>
            <li>Собственный санузел</li>
            <li>Душ и раковина в палате</li>
            <li>Больше приватности для пациента и сопровождающего</li>
          </ul>
        </article>
        <article>
          <span class="ward-fund__badge">В каждой</span>
          <h3>Оснащение палаты</h3>
          <ul>
            <li>Кондиционер</li>
            <li>Тонометр для контроля давления</li>
            <li>1–2 местное размещение по согласованию</li>
            <li>Мебель и условия для отдыха после капельницы</li>
          </ul>
        </article>
        <article>
          <span class="ward-fund__badge">24/7</span>
          <h3>Пост и сервис</h3>
          <ul>
            <li>Пост медицинской сестры круглосуточно</li>
            <li>Обходы врача-нарколога</li>
            <li>Питание и помощь с режимом дня</li>
            <li>Анонимное оформление, 18+, добровольно</li>
          </ul>
        </article>
      </div>
      <div class="ward-fund__cta">
        <a class="btn btn--blue" href="#" data-open-modal>Забронировать палату {ARR}</a>
        <a class="btn btn--line" href="tel:+78001001212" data-city-tel>Позвонить: <span data-city-phone>8 800 100-12-12</span></a>
      </div>
    </section>
"""

HUB_PROGRAMS = """
    <section class="alko-progs wrap" data-reveal id="alko-programs">
      <div class="alko-progs__head">
        <h2 class="section-title">Программы помощи<br>при алкоголизме</h2>
        <p>Конкретные курсы вывода из запоя в стационаре. У каждой программы — расписание по дням: утренняя и вечерняя капельница, осмотры и пост медсестры.</p>
      </div>
      <div class="alko-progs__grid">
        <a class="alko-prog" href="service-zapoy-1day.html">
          <em>1 день</em>
          <h3>Вывод из запоя 1 день в стационаре</h3>
          <p>Сутки наблюдения, утренняя и вечерняя капельница.</p>
          <b>от 8 900 ₽</b>
          <span class="more">Смотреть по часам</span>
        </a>
        <a class="alko-prog" href="service-zapoy-2days.html">
          <em>2 дня</em>
          <h3>Вывод из запоя — курс 2 дня</h3>
          <p>Двое суток детокса с двумя инфузиями в день.</p>
          <b>от 16 900 ₽</b>
          <span class="more">Смотреть по дням</span>
        </a>
        <a class="alko-prog alko-prog--feat" href="service-zapoy-3days.html">
          <em>3 дня</em>
          <h3>Вывод из запоя — курс 3 дня</h3>
          <p>Стандартный курс: утро/вечер капельница и восстановление сна.</p>
          <b>от 24 900 ₽</b>
          <span class="more">Смотреть программу</span>
        </a>
        <a class="alko-prog" href="service-zapoy-5days.html">
          <em>5 дней</em>
          <h3>Вывод из запоя — курс 5 дней</h3>
          <p>Расширенный детокс при длительном запое.</p>
          <b>от 39 900 ₽</b>
          <span class="more">Смотреть программу</span>
        </a>
        <a class="alko-prog" href="service-zapoy-7days.html">
          <em>7 дней</em>
          <h3>Вывод из запоя — курс 7 дней</h3>
          <p>Полная неделя стабилизации и спокойный выход домой.</p>
          <b>от 54 900 ₽</b>
          <span class="more">Смотреть программу</span>
        </a>
      </div>
    </section>
"""


def page_html(p: dict) -> str:
    others = "".join(
        f'<a class="svc-related__item" href="{x["file"]}"><span>{x["title"]}</span><b>{x["price"]}</b></a>'
        for x in PROGRAMS
        if x["file"] != p["file"]
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p["title"]} — Альба</title>
  <meta name="description" content="{p["title"]} в клинике Альба: расписание по дням, утренняя и вечерняя капельница, палата, пост медсестры. 18+, добровольно.">
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
            <a href="service-zapoy.html">Запой и капельница</a>
            <a href="service-alcohol.html">Лечение алкоголизма</a>
            <a href="service-zapoy.html#alko-programs">Курсы 1–7 дней</a>
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
        <a class="btn btn--dark" href="#" data-open-modal>Записаться {ARR}</a>
        <button class="burger" type="button" data-burger aria-label="Открыть меню"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>
  <nav class="mnav" data-mnav>
    <a href="about.html">О нас</a>
    <a href="programs.html">Программы</a>
    <a href="service-zapoy.html">Запой</a>
    <a href="doctors.html">Врачи</a>
    <a href="contacts.html">Контакты</a>
  </nav>

  <main>
    <section class="page-hero wrap">
      <div class="page-hero__box">
        <div>
          <div class="crumb"><a href="index.html">Главная</a> / <a href="service-zapoy.html">Запой</a> / <a href="service-zapoy.html#alko-programs">Программы</a> / {p["days"]} дн.</div>
          <h1 class="split">{p["h1"]}</h1>
        </div>
        <p>{p["lead"]}</p>
      </div>
    </section>

    <section class="svc wrap">
      <div data-reveal>
        <img class="article-cover" src="images/clinic-room.jpg" alt="" loading="lazy">
        <p>{p["lead"]} Состав капельниц и препаратов врач подбирает после осмотра — ниже типовое расписание курса.</p>
        <div class="svc-help" data-svc-help>
          <p class="svc-help__title">Вам поможет</p>
          <div class="svc-help__card">
            <img class="svc-help__photo" src="images/help-doctor-male-1.png" alt="Морозов Павел Игоревич" width="144" height="144" loading="lazy" decoding="async">
            <div>
              <p class="svc-help__name">Морозов Павел Игоревич</p>
              <p class="svc-help__role">Врач-нарколог</p>
            </div>
          </div>
          <a class="btn btn--blue" href="#" data-open-modal>Оставить заявку {ARR}</a>
        </div>
        <h2>Что входит</h2>
        <ul>
          <li>Размещение в палате стационара ({p["days"]} {"день" if p["days"]==1 else "дня" if p["days"] in (2,3,4) else "дней"})</li>
          <li>Осмотры нарколога и круглосуточный пост медсестры</li>
          <li>Утренняя и вечерняя капельница по схеме курса</li>
          <li>Контроль давления (тонометр), симптоматическая терапия</li>
          <li>Питание и рекомендации семье при выписке</li>
        </ul>
        <p><b>Кому подходит:</b> {p["for_whom"]}</p>
      </div>
      <aside class="svc-side" data-reveal>
        <span>Стоимость курса</span>
        <b>{p["price"]}</b>
        <em>{p["days"]} {"сутки" if p["days"]==1 else "суток"} в стационаре</em>
        <a class="btn btn--dark" href="#" data-open-modal>Записаться {ARR}</a>
        <a class="btn btn--line" href="tel:+78001001212" data-city-tel>Позвонить: <span data-city-phone>8 800 100-12-12</span></a>
        <p>18+. Добровольно. Имеются противопоказания. Схему корректирует врач.</p>
      </aside>
    </section>

    <section class="prog-schedule wrap" data-reveal>
      <div class="prog-schedule__head">
        <h2 class="section-title">Что входит<br>по дням</h2>
        <p>Типовой план. Утро — осмотр и капельница, вечер — повторная инфузия и сон. Точный состав препаратов зависит от состояния.</p>
      </div>
      <div class="prog-schedule__list">
          {schedule_html(p["schedule"])}
      </div>
      <p class="prog-schedule__note">Имеются противопоказания. При угрозе жизни вызывайте 103. Кодирование не проводят в остром запое.</p>
    </section>

{WARD_FUND}

    <section class="wrap" data-reveal>
      <h2 class="section-title">Другие курсы</h2>
      <div class="svc-related" style="display:grid;gap:10px;margin-top:18px">{others}</div>
    </section>

    <section class="cta wrap">
      <div class="cta__box" data-reveal="scale">
        <div><h2>Подберём курс под состояние</h2><p>Скажите, сколько длится запой — дежурный предложит 1, 2, 3, 5 или 7 дней.</p></div>
        <div class="cta__actions">
          <a class="btn btn--light" href="#" data-open-modal>Оставить заявку {ARR}</a>
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
            <li><a href="prices.html">Цены</a></li>
            <li><a href="doctors.html">Врачи</a></li>
          </ul>
        </div>
        <div>
          <h4>Программы</h4>
          <ul>
            <li><a href="service-zapoy.html#alko-programs">Курсы вывода из запоя</a></li>
            <li><a href="service-zapoy-1day.html">1 день</a></li>
            <li><a href="service-zapoy-3days.html">3 дня</a></li>
            <li><a href="service-zapoy-7days.html">7 дней</a></li>
          </ul>
        </div>
        <div><h4>Связь 24/7</h4><a class="footer__phone" href="tel:+78001001212" data-city-tel><span data-city-phone>8 800 100-12-12</span></a>
          <p><span data-city-address>Омск, ул. Ленина, 12</span><br>Лицензия <span data-city-license>ЛО-55-01-002891</span></p>
        </div>
      </div>
      <div class="footer__copy">
        <span>© <span data-year></span> ООО «Альба Медикал». 18+. Имеются противопоказания.</span>
      </div>
    </div>
  </footer>
  <div class="modal" data-modal>
    <div class="modal__box form">
      <button class="modal__close" type="button" data-close-modal aria-label="Закрыть">×</button>
      <h2>Запись на курс</h2>
      <p>Оставьте номер — подскажем, подходит ли курс {p["days"]} дн. и есть ли место в палате.</p>
      <form data-form>
        <div class="form__fields">
          <label for="m-name">Как к вам обращаться</label>
          <input id="m-name" name="name" type="text" placeholder="Имя или псевдоним" autocomplete="name">
          <label for="m-phone">Телефон</label>
          <input id="m-phone" name="phone" type="tel" placeholder="+7 (" required autocomplete="tel">
          <label for="m-prog">Программа</label>
          <select id="m-prog" name="program">
            <option selected>{p["title"]}</option>
            <option>Вывод из запоя 1 день</option>
            <option>Вывод из запоя 2 дня</option>
            <option>Вывод из запоя 3 дня</option>
            <option>Вывод из запоя 5 дней</option>
            <option>Вывод из запоя 7 дней</option>
          </select>
          <button class="btn btn--blue" type="submit">Жду звонка {ARR}</button>
        </div>
        <div class="form__ok">Заявка принята. Дежурный врач перезвонит с номера клиники.</div>
      </form>
    </div>
  </div>
  <script src="js/main.js"></script>
</body>
</html>
"""


def inject_after_svc(html: str, block: str) -> str:
    if "id=\"alko-programs\"" in html or "alko-progs" in html:
        return html
    import re
    m = re.search(r'(<section class="svc\b[\s\S]*?</section>)', html, flags=re.I)
    if not m:
        return html.replace("</main>", block + "\n  </main>", 1)
    return html[: m.end()] + "\n" + block + html[m.end() :]


def inject_ward(html: str) -> str:
    if 'id="ward-fund"' in html or "ward-fund" in html:
        return html
    import re
    # Prefer after alko-progs or after svc-tariffs or before faq/cta
    for marker in (
        r'(</section>\s*)(?=\s*<section class="[^"]*\bfaq\b)',
        r'(</section>\s*)(?=\s*<section class="cta\b)',
        r'(</div>\s*)(?=\s*<section class="faq\b)',
    ):
        html2, n = re.subn(marker, r"\1" + WARD_FUND + "\n", html, count=1, flags=re.I)
        if n:
            return html2
    return html.replace("</main>", WARD_FUND + "\n  </main>", 1)


def main() -> None:
    for p in PROGRAMS:
        path = ROOT / p["file"]
        path.write_text(page_html(p), encoding="utf-8")
        print("wrote", p["file"])

    for name in ("service-zapoy.html", "service-alcohol.html", "programs.html"):
        path = ROOT / name
        html = path.read_text(encoding="utf-8")
        if name != "programs.html":
            html = inject_after_svc(html, HUB_PROGRAMS)
        else:
            # programs: insert hub near top of catalog area if missing
            if "alko-progs" not in html:
                html = html.replace(
                    '<div class="catalog">',
                    HUB_PROGRAMS + '\n      <div class="catalog">',
                    1,
                )
        html = inject_ward(html)
        path.write_text(html, encoding="utf-8")
        print("updated", name)

    # index: update rooms copy + offer dirs + inject ward near rooms
    index = ROOT / "index.html"
    html = index.read_text(encoding="utf-8")
    if "ward-fund" not in html:
        html = html.replace(
            '<section class="rooms wrap" data-rooms>',
            WARD_FUND + '\n    <section class="rooms wrap" data-rooms>',
            1,
        )
    # enrich offer-dirs zapoy list
    old = (
        '<div class="offer-dirs__list"><a href="service-zapoy.html"><span>Вывод из запоя</span><em>от 2 500 ₽</em></a>'
        '<a href="service-alcohol-hangover.html"><span>Капельница от похмелья</span><em>от 2 500 ₽</em></a>'
    )
    new = (
        '<div class="offer-dirs__list">'
        '<a href="service-zapoy-1day.html"><span>Вывод из запоя 1 день</span><em>от 8 900 ₽</em></a>'
        '<a href="service-zapoy-3days.html"><span>Курс 3 дня</span><em>от 24 900 ₽</em></a>'
        '<a href="service-zapoy-5days.html"><span>Курс 5 дней</span><em>от 39 900 ₽</em></a>'
        '<a href="service-zapoy-7days.html"><span>Курс 7 дней</span><em>от 54 900 ₽</em></a>'
        '<a href="service-zapoy.html"><span>Вывод из запоя</span><em>от 2 500 ₽</em></a>'
        '<a href="service-alcohol-hangover.html"><span>Капельница от похмелья</span><em>от 2 500 ₽</em></a>'
    )
    if old in html:
        html = html.replace(old, new, 1)
    index.write_text(html, encoding="utf-8")
    print("updated index.html")


if __name__ == "__main__":
    main()
