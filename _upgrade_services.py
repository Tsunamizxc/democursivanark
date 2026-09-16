# -*- coding: utf-8 -*-
"""Inject marketing upgrade blocks into root service-*.html pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

UPGRADE_HTML = """
    <section class="svc-upgrade wrap" data-svc-upgrade data-reveal>
      <div class="svc-benefits">
        <article>
          <h3>Анонимно</h3>
          <p>Обращение и лечение без уведомлений третьим лицам. Можно начать с псевдонима.</p>
        </article>
        <article>
          <h3>24/7</h3>
          <p>Дежурный специалист на связи круглосуточно — дом или стационар по показаниям.</p>
        </article>
        <article>
          <h3>Два формата</h3>
          <p>Выезд на дом или палата. Формат выбираем после оценки состояния, не «с порога».</p>
        </article>
        <article>
          <h3>План для семьи</h3>
          <p>Объясняем родственникам, что делать дальше — без давления и обещаний «навсегда».</p>
        </article>
      </div>

      <div class="svc-when">
        <h2>Когда стоит обратиться</h2>
        <ul>
          <li>Срыв или запой, который не удаётся остановить самостоятельно</li>
          <li>Нужна стабилизация дома или решение о госпитализации</li>
          <li>Семья не знает, с чего начать разговор о помощи</li>
          <li>После детокса нужен понятный следующий шаг</li>
          <li>Важны анонимность и добровольный формат (18+)</li>
          <li>Нужен ориентир по стоимости до выезда врача</li>
        </ul>
      </div>

      <div class="svc-why">
        <article>
          <b>Только добровольно</b>
          <p>Плановое лечение — с информированным согласием пациента.</p>
        </article>
        <article>
          <b>Без «укола с порога»</b>
          <p>Кодирование и жёсткие методы — только после осмотра и стабилизации.</p>
        </article>
        <article>
          <b>Лицензия и протоколы</b>
          <p>Медицинская организация с понятным маршрутом помощи.</p>
        </article>
        <article>
          <b>Один контакт 24/7</b>
          <p>Телефон, Max и Telegram — дежурный подскажет формат.</p>
        </article>
      </div>

      <div class="svc-docs-teaser">
        <div>
          <h2>Врачи на маршруте помощи</h2>
          <p>Наркологи, психиатры и психотерапевты — можно выбрать специалиста до визита.</p>
        </div>
        <a class="btn btn--light" href="doctors.html">Смотреть команду</a>
      </div>
    </section>
"""


def upgrade(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    if "data-svc-upgrade" in html:
        return False
    if "<main" not in html:
        return False

    block = UPGRADE_HTML
    # Prefer after .svc section closing, else before .steps / .faq / </main>
    patterns = [
        (r'(</section>\s*)(?=\s*<section class="[^"]*\bsteps\b)', 1),
        (r'(</section>\s*)(?=\s*<section class="[^"]*\bfaq\b)', 1),
        (r'(</section>\s*)(?=\s*<section class="cta\b)', 1),
        (r'(</section>\s*)(?=\s*</main>)', 1),
    ]

    # Try insert after section.svc specifically
    m = re.search(
        r'(<section class="svc\b[\s\S]*?</section>)',
        html,
        flags=re.I,
    )
    if m:
        insert_at = m.end()
        html = html[:insert_at] + "\n" + block + html[insert_at:]
        path.write_text(html, encoding="utf-8")
        return True

    for pat, _ in patterns:
        html2, n = re.subn(pat, r"\1" + block, html, count=1, flags=re.I)
        if n:
            path.write_text(html2, encoding="utf-8")
            return True

    html = html.replace("</main>", block + "\n  </main>", 1)
    path.write_text(html, encoding="utf-8")
    return True


def main():
    files = sorted(ROOT.glob("service-*.html"))
    done = 0
    skipped = 0
    for f in files:
        if upgrade(f):
            done += 1
            print("upgraded", f.name)
        else:
            skipped += 1
    print(f"done={done} skipped={skipped} total={len(files)}")


if __name__ == "__main__":
    main()
