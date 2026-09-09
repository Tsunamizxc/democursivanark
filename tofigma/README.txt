HTML+CSS в одном файле для html-to-figma (Playwright DOM capture).

Картинки: ../images/
JS-контент зашит: город, cookie, mega-меню, футер услуг, счётчики,
калькулятор, sticky-lead (Max / Telegram / Звонок).

Профиль под плагин (shared/capture-script.ts + prepareStaticPage):
- нет mask/filter/backdrop-filter/transform/clip-path
- sticky/fixed → relative/absolute
- header relative, body без padding-top
- sticky-lead absolute снизу, без blur
- hero__orbit заморожен, диск с явным width/height
- телефон и Max — inline SVG (не CSS mask/filter)
- images loading=eager, FAQ раскрыт
- marquee без анимации

Импорт: npm run server в html-to-figma → плагин → папка tofigma → Desktop 1440.
Пересборка: python _build_tofigma.py
