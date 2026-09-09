HTML+CSS в одном файле для html-to-figma (Playwright DOM capture).

Картинки: ../images/
JS-контент зашит: город, cookie, mega-меню, футер услуг, счётчики, калькулятор.

Профиль под плагин (shared/capture-script.ts):
- нет mask/filter/backdrop-filter/transform
- sticky/fixed → relative/absolute
- телефон и Max — inline SVG (не CSS mask/filter)
- images loading=eager
- marquee без анимации
- псевдо-круги с явным width/height

Импорт: npm run server в html-to-figma → плагин → папка tofigma → Desktop 1440.
Пересборка: python _build_tofigma.py
