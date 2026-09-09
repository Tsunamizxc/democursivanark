(() => {
  const doc = document;
  const body = doc.body;
  const KEY = "alba-city";

  const CITIES = [
    { id: "omsk", name: "Омск", prep: "в Омске", phone: "+7 (3812) 90-12-12", tel: "+73812901212", address: "Омск, ул. Ленина, 12", extra: "Отдельный вход. Трансфер по городу и области.", license: "ЛО-55-01-002891", map: "https://yandex.ru/map-widget/v1/?ll=73.368227%2C54.989342&z=16&text=%D0%9E%D0%BC%D1%81%D0%BA%2C%20%D1%83%D0%BB.%20%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B0%2C%2012" },
    { id: "nsk", name: "Новосибирск", prep: "в Новосибирске", phone: "+7 (383) 209-12-12", tel: "+73832091212", address: "Новосибирск, Красный проспект, 52", extra: "Отдельный вход, закрытая парковка.", license: "ЛО-54-01-005412", map: "https://yandex.ru/map-widget/v1/?ll=82.920430%2C55.030204&z=16&text=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%2C%20%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D1%81%D0%BF%D0%B5%D0%BA%D1%82%2C%2052" },
    { id: "tomsk", name: "Томск", prep: "в Томске", phone: "+7 (3822) 90-12-12", tel: "+73822901212", address: "Томск, пр. Ленина, 54", extra: "Тихий двор, трансфер по городу.", license: "ЛО-70-01-001904", map: "https://yandex.ru/map-widget/v1/?ll=84.948227%2C56.484640&z=16&text=%D0%A2%D0%BE%D0%BC%D1%81%D0%BA%2C%20%D0%BF%D1%80%D0%BE%D1%81%D0%BF%D0%B5%D0%BA%D1%82%20%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B0%2C%2054" },
    { id: "tyumen", name: "Тюмень", prep: "в Тюмени", phone: "+7 (3452) 90-12-12", tel: "+73452901212", address: "Тюмень, ул. Республики, 83", extra: "Центр, анонимный подъезд.", license: "ЛО-72-01-003215", map: "https://yandex.ru/map-widget/v1/?ll=65.534328%2C57.152974&z=16&text=%D0%A2%D1%8E%D0%BC%D0%B5%D0%BD%D1%8C%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%A0%D0%B5%D1%81%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B8%2C%2083" },
    { id: "barnaul", name: "Барнаул", prep: "в Барнауле", phone: "+7 (3852) 90-12-12", tel: "+73852901212", address: "Барнаул, пр. Ленина, 24", extra: "Отдельный вход со двора.", license: "ЛО-22-01-004118", map: "https://yandex.ru/map-widget/v1/?ll=83.779861%2C53.347847&z=16&text=%D0%91%D0%B0%D1%80%D0%BD%D0%B0%D1%83%D0%BB%2C%20%D0%BF%D1%80%D0%BE%D1%81%D0%BF%D0%B5%D0%BA%D1%82%20%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B0%2C%2024" },
    { id: "kemerovo", name: "Кемерово", prep: "в Кемерове", phone: "+7 (3842) 90-12-12", tel: "+73842901212", address: "Кемерово, пр. Советский, 54", extra: "Стационар 24/7, трансфер.", license: "ЛО-42-01-002671", map: "https://yandex.ru/map-widget/v1/?ll=86.087314%2C55.354968&z=16&text=%D0%9A%D0%B5%D0%BC%D0%B5%D1%80%D0%BE%D0%B2%D0%BE%2C%20%D0%A1%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%81%D0%BF%D0%B5%D0%BA%D1%82%2C%2054" },
    { id: "nkz", name: "Новокузнецк", prep: "в Новокузнецке", phone: "+7 (3843) 90-12-12", tel: "+73843901212", address: "Новокузнецк, пр. Металлургов, 19", extra: "Закрытая территория.", license: "ЛО-42-01-002688", map: "https://yandex.ru/map-widget/v1/?ll=87.136047%2C53.757547&z=16&text=%D0%9D%D0%BE%D0%B2%D0%BE%D0%BA%D1%83%D0%B7%D0%BD%D0%B5%D1%86%D0%BA%2C%20%D0%9C%D0%B5%D1%82%D0%B0%D0%BB%D0%BB%D1%83%D1%80%D0%B3%D0%BE%D0%B2%2C%2019" },
    { id: "krsk", name: "Красноярск", prep: "в Красноярске", phone: "+7 (391) 209-12-12", tel: "+73912091212", address: "Красноярск, ул. Карла Маркса, 78", extra: "Центр, анонимный въезд.", license: "ЛО-24-01-003901", map: "https://yandex.ru/map-widget/v1/?ll=92.852576%2C56.010569&z=16&text=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA%2C%20%D0%9A%D0%B0%D1%80%D0%BB%D0%B0%20%D0%9C%D0%B0%D1%80%D0%BA%D1%81%D0%B0%2C%2078" },
    { id: "surgut", name: "Сургут", prep: "в Сургуте", phone: "+7 (3462) 90-12-12", tel: "+73462901212", address: "Сургут, ул. Энтузиастов, 8", extra: "Круглосуточный приём.", license: "ЛО-86-01-001744", map: "https://yandex.ru/map-widget/v1/?ll=73.396713%2C61.254035&z=16&text=%D0%A1%D1%83%D1%80%D0%B3%D1%83%D1%82%2C%20%D0%AD%D0%BD%D1%82%D1%83%D0%B7%D0%B8%D0%B0%D1%81%D1%82%D0%BE%D0%B2%2C%208" },
    { id: "moscow", name: "Москва", prep: "в Москве", phone: "+7 (495) 122-08-08", tel: "+74951220808", address: "Москва, Пресненская наб., 10с2", extra: "Внутренний двор, закрытая парковка.", license: "ЛО-77-01-021458", map: "https://yandex.ru/map-widget/v1/?ll=37.539139%2C55.747231&z=16&text=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%9F%D1%80%D0%B5%D1%81%D0%BD%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BD%D0%B0%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%BD%D0%B0%D1%8F%2C%2010" },
    { id: "spb", name: "Санкт-Петербург", prep: "в Санкт-Петербурге", phone: "+7 (812) 309-12-12", tel: "+78123091212", address: "Санкт-Петербург, Невский пр., 88", extra: "Отдельный вход со двора.", license: "ЛО-78-01-011203", map: "https://yandex.ru/map-widget/v1/?ll=30.360909%2C59.931058&z=16&text=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%2C%20%D0%9D%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%81%D0%BF%D0%B5%D0%BA%D1%82%2C%2088" }
  ];

  const byId = Object.fromEntries(CITIES.map((c) => [c.id, c]));

  const applyCity = (city) => {
    try { localStorage.setItem(KEY, city.id); } catch (e) {}
    doc.querySelectorAll("[data-city-name]").forEach((n) => { n.textContent = city.name; });
    doc.querySelectorAll("[data-city-prep]").forEach((n) => { n.textContent = city.prep; });
    doc.querySelectorAll("[data-city-phone]").forEach((n) => { n.textContent = city.phone; });
    doc.querySelectorAll("[data-city-address]").forEach((n) => { n.textContent = city.address; });
    doc.querySelectorAll("[data-city-extra]").forEach((n) => { n.textContent = city.extra; });
    doc.querySelectorAll("[data-city-license]").forEach((n) => { n.textContent = city.license; });
    doc.querySelectorAll("[data-city-tel]").forEach((a) => { a.setAttribute("href", "tel:" + city.tel); });
    const digits = city.tel.replace(/\D/g, "");
    doc.querySelectorAll("[data-city-max]").forEach((a) => { a.setAttribute("href", "https://max.ru/"); });
    doc.querySelectorAll("[data-city-tg]").forEach((a) => { a.setAttribute("href", "https://t.me/+" + digits); });
    const map = doc.querySelector("[data-city-map]");
    if (map && city.map) map.src = city.map;
  };

  const geo = () => {
    const header = doc.querySelector(".header__bar");
    if (header && !doc.querySelector(".city-btn")) {
      const btn = doc.createElement("button");
      btn.type = "button";
      btn.className = "city-btn";
      btn.setAttribute("data-open-city", "");
      btn.innerHTML = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M10 18s6-5.2 6-10a6 6 0 1 0-12 0c0 4.8 6 10 6 10Z" stroke="currentColor" stroke-width="1.6"/><circle cx="10" cy="8" r="2.1" stroke="currentColor" stroke-width="1.6"/></svg><span data-city-name>Омск</span>';
      const logo = header.querySelector(".logo");
      if (logo && logo.nextSibling) header.insertBefore(btn, logo.nextSibling);
      else header.appendChild(btn);
    }

    const mnav = doc.querySelector("[data-mnav]");
    if (mnav && !mnav.querySelector("[data-open-city]")) {
      const mb = doc.createElement("button");
      mb.type = "button";
      mb.className = "city-btn";
      mb.setAttribute("data-open-city", "");
      mb.innerHTML = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M10 18s6-5.2 6-10a6 6 0 1 0-12 0c0 4.8 6 10 6 10Z" stroke="currentColor" stroke-width="1.6"/><circle cx="10" cy="8" r="2.1" stroke="currentColor" stroke-width="1.6"/></svg><span data-city-name>Омск</span>';
      mnav.appendChild(mb);
    }

    const wrap = doc.createElement("div");
    wrap.className = "geo";
    wrap.setAttribute("data-geo", "");
    wrap.innerHTML = '<div class="geo__box" role="dialog" aria-modal="true" aria-labelledby="geo-title">' +
      '<div class="geo__ask" data-geo-ask>' +
      '<h2 id="geo-title">Вы из Омска?</h2>' +
      '<p>Покажем телефон, адрес и условия вашей клиники.</p>' +
      '<div class="geo__actions">' +
      '<button type="button" class="btn btn--blue" data-geo-yes>Да, я из Омска</button>' +
      '<button type="button" class="btn btn--line" data-geo-other>Выбрать другой город</button>' +
      '</div></div>' +
      '<div class="geo__pick" data-geo-pick hidden>' +
      '<h2>Выберите город</h2>' +
      '<p>Работаем в Сибири и принимаем пациентов из других регионов.</p>' +
      '<input class="geo__search" type="search" placeholder="Найти город" data-geo-search>' +
      '<div class="geo__grid" data-geo-grid></div>' +
      '<button type="button" class="geo__back" data-geo-back>Назад</button>' +
      '</div></div>';
    body.appendChild(wrap);

    const ask = wrap.querySelector("[data-geo-ask]");
    const pick = wrap.querySelector("[data-geo-pick]");
    const grid = wrap.querySelector("[data-geo-grid]");
    const search = wrap.querySelector("[data-geo-search]");

    const renderGrid = (q) => {
      const query = (q || "").trim().toLowerCase();
      grid.innerHTML = CITIES.filter((c) => !query || c.name.toLowerCase().includes(query)).map((c) =>
        '<button type="button" class="geo__city" data-city-id="' + c.id + '">' + c.name + "</button>"
      ).join("") || '<p>Город не найден. Оставьте Омск или позвоните нам.</p>';
    };
    renderGrid("");

    const openGeo = (mode) => {
      wrap.classList.add("is-open");
      body.classList.add("is-lock");
      if (mode === "pick") {
        ask.hidden = true;
        pick.hidden = false;
      } else {
        ask.hidden = false;
        pick.hidden = true;
      }
    };
    const closeGeo = () => {
      wrap.classList.remove("is-open");
      body.classList.remove("is-lock");
    };
    const choose = (city) => {
      applyCity(city);
      closeGeo();
    };

    wrap.querySelector("[data-geo-yes]").addEventListener("click", () => choose(byId.omsk));
    wrap.querySelector("[data-geo-other]").addEventListener("click", () => {
      ask.hidden = true;
      pick.hidden = false;
      search.focus();
    });
    wrap.querySelector("[data-geo-back]").addEventListener("click", () => {
      pick.hidden = true;
      ask.hidden = false;
    });
    grid.addEventListener("click", (e) => {
      const b = e.target.closest("[data-city-id]");
      if (b) choose(byId[b.getAttribute("data-city-id")]);
    });
    search.addEventListener("input", () => renderGrid(search.value));
    wrap.addEventListener("click", (e) => {
      if (e.target === wrap && localStorage.getItem(KEY)) closeGeo();
    });
    doc.addEventListener("click", (e) => {
      if (e.target.closest("[data-open-city]")) {
        e.preventDefault();
        openGeo("pick");
      }
    });

    let saved = null;
    try { saved = localStorage.getItem(KEY); } catch (e) {}
    if (saved && byId[saved]) applyCity(byId[saved]);
    else setTimeout(() => openGeo("ask"), 1100);
  };

  const preload = () => {
    const el = doc.querySelector(".preloader");
    if (!el) return;
    let finished = false;
    const done = () => {
      if (finished) return;
      finished = true;
      el.classList.add("is-done");
      body.classList.remove("is-lock");
      doc.querySelectorAll(".split").forEach((n, i) => {
        setTimeout(() => n.classList.add("is-in"), 40 + i * 50);
      });
      doc.querySelectorAll(".hero [data-reveal]").forEach((n, i) => {
        setTimeout(() => n.classList.add("is-in"), 120 + i * 70);
      });
    };
    body.classList.add("is-lock");
    window.addEventListener("load", () => setTimeout(done, 400));
    setTimeout(done, 1200);
  };

  const splitHeadings = () => {
    doc.querySelectorAll(".split").forEach((el) => {
      const html = el.innerHTML.trim();
      const parts = html.split(/<br\s*\/?>/i);
      el.innerHTML = parts.map((line) =>
        line.trim().split(/\s+/).map((w) => "<span><em>" + w + "&nbsp;</em></span>").join("")
      ).join("<br>");
    });
  };

  const tilt = () => {
    if (matchMedia("(pointer: coarse)").matches) return;
    doc.querySelectorAll("[data-tilt]").forEach((card) => {
      card.addEventListener("mousemove", (e) => {
        const r = card.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width;
        const py = (e.clientY - r.top) / r.height;
        card.style.transform = "perspective(800px) rotateX(" + ((0.5 - py) * 6) + "deg) rotateY(" + ((px - 0.5) * 8) + "deg) translateY(-4px)";
      });
      card.addEventListener("mouseleave", () => { card.style.transform = ""; });
    });
  };

  const header = () => {
    const el = doc.querySelector("[data-header]");
    if (!el) return;
    const onScroll = () => el.classList.toggle("is-scrolled", scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  };

  const mobileNav = () => {
    const burger = doc.querySelector("[data-burger]");
    const nav = doc.querySelector("[data-mnav]");
    if (!burger || !nav) return;
    let lockY = 0;
    const html = doc.documentElement;
    const lock = () => {
      lockY = window.scrollY;
      html.classList.add("is-lock");
      body.classList.add("is-lock");
      body.style.top = "-" + lockY + "px";
    };
    const unlock = () => {
      html.classList.remove("is-lock");
      body.classList.remove("is-lock");
      body.style.top = "";
      window.scrollTo(0, lockY);
    };
    const close = () => {
      burger.classList.remove("is-open");
      nav.classList.remove("is-open");
      unlock();
    };
    burger.addEventListener("click", () => {
      const open = burger.classList.toggle("is-open");
      nav.classList.toggle("is-open", open);
      if (open) lock();
      else unlock();
    });
    nav.querySelectorAll("a").forEach((a) => a.addEventListener("click", close));
  };

  const reveals = () => {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        const delay = Number(en.target.dataset.delay || 0);
        setTimeout(() => en.target.classList.add("is-in"), delay);
        io.unobserve(en.target);
      });
    }, { threshold: 0.14, rootMargin: "0px 0px -6% 0px" });
    doc.querySelectorAll("[data-reveal]").forEach((n) => io.observe(n));
  };

  const counters = () => {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        const el = en.target;
        const to = parseFloat(el.dataset.count);
        const dec = String(to).includes(".") ? 1 : 0;
        const t0 = performance.now();
        const tick = (now) => {
          const p = Math.min(1, (now - t0) / 1200);
          const val = to * (1 - Math.pow(1 - p, 3));
          el.textContent = dec ? val.toFixed(1) : Math.round(val).toLocaleString("ru-RU");
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        io.unobserve(el);
      });
    });
    doc.querySelectorAll("[data-count]").forEach((n) => io.observe(n));
  };

  const accordion = () => {
    doc.querySelectorAll("[data-acc]").forEach((root) => {
      root.querySelectorAll(".acc__item").forEach((item) => {
        item.querySelector(".acc__btn").addEventListener("click", () => {
          const open = item.classList.contains("is-open");
          root.querySelectorAll(".acc__item").forEach((i) => i.classList.remove("is-open"));
          if (!open) item.classList.add("is-open");
        });
      });
    });
  };

  const modal = () => {
    const el = doc.querySelector("[data-modal]");
    if (!el) return;
    const box = el.querySelector(".modal__box");
    const open = () => { el.classList.add("is-open"); body.classList.add("is-lock"); };
    const close = () => { el.classList.remove("is-open"); body.classList.remove("is-lock"); };
    doc.querySelectorAll("[data-open-modal]").forEach((b) => b.addEventListener("click", (e) => {
      e.preventDefault();
      open();
    }));
    el.addEventListener("click", (e) => { if (e.target === el) close(); });
    el.querySelectorAll("[data-close-modal]").forEach((b) => b.addEventListener("click", close));
    doc.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
    if (box) box.addEventListener("click", (e) => e.stopPropagation());
  };

  const forms = () => {
    doc.querySelectorAll("form[data-form]").forEach((form) => {
      if (form.closest("[data-calc-form]")) return;
      form.addEventListener("submit", (e) => {
        e.preventDefault();
        const wrap = form.closest(".form") || form;
        wrap.classList.add("is-sent");
      });
    });
  };

  const year = () => {
    doc.querySelectorAll("[data-year]").forEach((n) => {
      n.textContent = String(new Date().getFullYear());
    });
  };

  const marquee = () => {
    const root = doc.querySelector(".marquee");
    const track = root && root.querySelector(".marquee__track");
    const source = track && track.querySelector(".marquee__group");
    if (!root || !track || !source) return;
    const original = source.innerHTML;

    const build = () => {
      source.innerHTML = original;
      const minW = Math.max(root.clientWidth, 1);
      let guard = 0;
      while (source.scrollWidth < minW && guard < 12) {
        source.insertAdjacentHTML("beforeend", original);
        guard += 1;
        if (!source.scrollWidth) break;
      }
      const live = doc.querySelector(".footer [data-city-license]");
      if (live) {
        source.querySelectorAll("[data-city-license]").forEach((n) => {
          n.textContent = live.textContent;
        });
      }
      track.querySelectorAll(".marquee__group").forEach((g, i) => {
        if (i) g.remove();
      });
      track.appendChild(source.cloneNode(true));
      const dist = source.offsetWidth || minW;
      track.style.setProperty("--marquee-duration", Math.max(18, dist / 42).toFixed(1) + "s");
      track.style.animation = "none";
      void track.offsetWidth;
      track.style.animation = "";
    };

    const start = () => build();
    if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(start);
    else start();
    let timer = 0;
    window.addEventListener("resize", () => {
      window.clearTimeout(timer);
      timer = window.setTimeout(build, 160);
    });
  };

  const cookies = () => {
    try { if (localStorage.getItem("alba-cookie")) return; } catch (e) {}
    const bar = doc.createElement("div");
    bar.className = "cookie";
    bar.innerHTML = "<p>Сайт запоминает выбранный город и использует cookie. К страницам может быть подключена аналитика. Подробнее — в <a href=\"privacy.html\">политике ПДн</a> и <a href=\"consent.html\">согласии</a>.</p><button type=\"button\" class=\"btn btn--blue\">Понятно</button>";
    body.appendChild(bar);
    bar.querySelector("button").addEventListener("click", () => {
      try { localStorage.setItem("alba-cookie", "1"); } catch (e) {}
      bar.remove();
    });
  };

  const catalogNav = () => {
    const drops = [...doc.querySelectorAll(".nav__drop")];
    const clinic = drops.find((d) => d.querySelector(".nav__btn")?.textContent.includes("Клиника"));
    const programs = drops.find((d) => d.querySelector(".nav__btn")?.textContent.includes("Программы"));
    if (clinic) {
      const menu = clinic.querySelector(".nav__menu");
      if (menu && !menu.querySelector("[data-extra-clinic]")) {
        menu.insertAdjacentHTML("beforeend",
          '<a data-extra-clinic href="reviews.html">Отзывы</a>' +
          '<a data-extra-clinic href="methods.html">Методы помощи</a>' +
          '<a data-extra-clinic href="sitemap.html">Карта сайта</a>');
      }
    }
    if (programs) {
      const menu = programs.querySelector(".nav__menu");
      if (menu && !menu.classList.contains("nav__mega")) {
        menu.classList.add("nav__mega");
        menu.innerHTML =
          '<div class="nav__col"><b>Срочно</b>' +
          '<a href="service-zapoy.html">Запой и капельница</a>' +
          '<a href="service-visit.html">Выезд нарколога</a>' +
          '<a href="service-ambulance.html">Наркологическая скорая</a>' +
          '<a href="service-withdrawal.html">Снятие ломки</a>' +
          '<a href="service-ubod.html">УБОД</a></div>' +
          '<div class="nav__col"><b>Лечение</b>' +
          '<a href="service-alcohol.html">Алкоголизм</a>' +
          '<a href="service-drugs.html">Наркомания</a>' +
          '<a href="service-gambling.html">Игровая зависимость</a>' +
          '<a href="service-code.html">Кодирование</a>' +
          '<a href="service-rehab.html">Реабилитация</a></div>' +
          '<div class="nav__col"><b>Клиника</b>' +
          '<a href="service-detox.html">Детокс 24/7</a>' +
          '<a href="service-psychiatry.html">Психиатрия</a>' +
          '<a href="service-consult.html">Консультация</a>' +
          '<a href="service-check.html">Диагностика</a>' +
          '<a href="service-family.html">Семья</a></div>' +
          '<div class="nav__col"><b>Ещё</b>' +
          '<a href="service-help.html">Наркологическая помощь</a>' +
          '<a href="methods.html">Методы</a>' +
          '<a href="prices.html">Цены</a>' +
          '<a href="programs.html">Весь каталог</a></div>';
      }
    }

    const mnav = doc.querySelector("[data-mnav]");
    if (mnav && !mnav.querySelector("[data-extra-mnav]")) {
      const extra = [
        ["service-alcohol.html", "Алкоголизм"],
        ["service-drugs.html", "Наркомания"],
        ["service-code.html", "Кодирование"],
        ["service-help.html", "Наркологическая помощь"],
        ["service-gambling.html", "Игровая зависимость"],
        ["reviews.html", "Отзывы"],
        ["methods.html", "Методы"],
        ["sitemap.html", "Карта сайта"]
      ].map(([h, t]) => '<a data-extra-mnav href="' + h + '">' + t + "</a>").join("");
      const prices = [...mnav.querySelectorAll("a")].find((a) => a.getAttribute("href") === "prices.html");
      if (prices) prices.insertAdjacentHTML("afterend", extra);
      else mnav.insertAdjacentHTML("afterbegin", extra);
    }

    const foot = doc.querySelector(".footer__grid");
    if (foot && !foot.querySelector("[data-extra-foot]")) {
      const col = doc.createElement("div");
      col.setAttribute("data-extra-foot", "");
      col.innerHTML = "<h4>Направления</h4><ul>" +
        "<li><a href=\"service-alcohol.html\">Алкоголизм</a></li>" +
        "<li><a href=\"service-drugs.html\">Наркомания</a></li>" +
        "<li><a href=\"service-code.html\">Кодирование</a></li>" +
        "<li><a href=\"service-gambling.html\">Игровая зависимость</a></li>" +
        "<li><a href=\"service-help.html\">Помощь 24/7</a></li>" +
        "</ul>";
      const programsCol = [...foot.children].find((n) => n.querySelector("h4")?.textContent.includes("Программы"));
      if (programsCol) programsCol.after(col);
      else foot.appendChild(col);
    }

    const footWrap = doc.querySelector(".footer > .wrap");
    if (footWrap && !footWrap.querySelector("[data-footer-services]")) {
      const services = doc.createElement("div");
      services.className = "footer__services";
      services.setAttribute("data-footer-services", "");
      services.innerHTML =
        "<h4>Все услуги</h4>" +
        '<div class="footer__services-grid">' +
        "<div><b>Срочная помощь</b><ul>" +
        '<li><a href="service-zapoy.html">Запой и капельница</a></li>' +
        '<li><a href="service-visit.html">Выезд нарколога</a></li>' +
        '<li><a href="service-ambulance.html">Наркологическая скорая</a></li>' +
        '<li><a href="service-withdrawal.html">Снятие ломки</a></li>' +
        '<li><a href="service-ubod.html">УБОД</a></li>' +
        '<li><a href="service-sober.html">Частный вытрезвитель</a></li>' +
        '<li><a href="service-detox.html">Детокс 24/7</a></li>' +
        '<li><a href="service-drugtest.html">Тест на наркотики</a></li>' +
        '<li><a href="service-toxicologist.html">Токсиколог</a></li>' +
        '<li><a href="service-help.html">Наркологическая помощь</a></li>' +
        "</ul></div>" +
        "<div><b>Алкоголизм</b><ul>" +
        '<li><a href="service-alcohol.html">Лечение алкоголизма</a></li>' +
        '<li><a href="service-alcohol-women.html">Женский алкоголизм</a></li>' +
        '<li><a href="service-alcohol-men.html">Мужской алкоголизм</a></li>' +
        '<li><a href="service-alcohol-beer.html">Пивной</a></li>' +
        '<li><a href="service-alcohol-wine.html">Винный</a></li>' +
        '<li><a href="service-alcohol-elderly.html">Старческий</a></li>' +
        '<li><a href="service-alcohol-home.html">На дому</a></li>' +
        '<li><a href="service-alcohol-hangover.html">Похмелье</a></li>' +
        '<li><a href="service-alcohol-shot.html">Укол от алкоголизма</a></li>' +
        '<li><a href="service-alcohol-shichko.html">Метод Шичко</a></li>' +
        "</ul></div>" +
        "<div><b>Кодирование</b><ul>" +
        '<li><a href="service-code.html">Кодирование</a></li>' +
        '<li><a href="service-code-dovzhenko.html">По Довженко</a></li>' +
        '<li><a href="service-code-hypnosis.html">Гипноз</a></li>' +
        '<li><a href="service-code-implant.html">Вшивание ампулы</a></li>' +
        '<li><a href="service-code-torpedo.html">Торпедо</a></li>' +
        '<li><a href="service-code-esperal.html">Эспераль</a></li>' +
        '<li><a href="service-code-double.html">Двойной блок</a></li>' +
        '<li><a href="service-code-shot.html">Укол</a></li>' +
        '<li><a href="service-code-needle.html">Иглоукалывание</a></li>' +
        '<li><a href="service-code-aquilong.html">Аквилонг</a></li>' +
        '<li><a href="service-code-vivitrol.html">Вивитрол</a></li>' +
        '<li><a href="service-code-naltrexone.html">Налтрексон</a></li>' +
        '<li><a href="service-code-disulfiram.html">Дисульфирам</a></li>' +
        '<li><a href="service-code-algominal.html">Алгоминал</a></li>' +
        '<li><a href="service-code-sit.html">SIT</a></li>' +
        '<li><a href="service-code-home.html">На дому</a></li>' +
        '<li><a href="service-decode.html">Раскодирование</a></li>' +
        "</ul></div>" +
        "<div><b>Наркомания</b><ul>" +
        '<li><a href="service-drugs.html">Лечение наркомании</a></li>' +
        '<li><a href="service-drugs-code.html">Кодировка от наркозависимости</a></li>' +
        '<li><a href="service-drugs-heroin.html">Героин</a></li>' +
        '<li><a href="service-drugs-methadone.html">Метадон</a></li>' +
        '<li><a href="service-drugs-mephedrone.html">Мефедрон</a></li>' +
        '<li><a href="service-drugs-salts.html">Соли</a></li>' +
        '<li><a href="service-drugs-spice.html">Спайс</a></li>' +
        '<li><a href="service-drugs-cocaine.html">Кокаин</a></li>' +
        '<li><a href="service-drugs-amphetamine.html">Амфетамин</a></li>' +
        '<li><a href="service-drugs-cannabis.html">Марихуана</a></li>' +
        '<li><a href="service-drugs-toxico.html">Токсикомания</a></li>' +
        '<li><a href="service-drugs-butyrate.html">Бутират</a></li>' +
        '<li><a href="service-drugs-ephedrine.html">Эфедрин</a></li>' +
        "</ul></div>" +
        "<div><b>Реабилитация и семья</b><ul>" +
        '<li><a href="service-rehab.html">Реабилитация</a></li>' +
        '<li><a href="service-rehab-alcohol.html">Реабилитация алкозависимости</a></li>' +
        '<li><a href="service-rehab-12.html">12 шагов</a></li>' +
        '<li><a href="service-rehab-daytop.html">Day Top</a></li>' +
        '<li><a href="service-family.html">Семейная программа</a></li>' +
        '<li><a href="service-consult.html">Консультация</a></li>' +
        '<li><a href="service-check.html">Диагностика</a></li>' +
        '<li><a href="service-gambling.html">Игровая зависимость</a></li>' +
        '<li><a href="service-betting.html">Ставки на спорт</a></li>' +
        "</ul></div>" +
        "<div><b>Психиатрия</b><ul>" +
        '<li><a href="service-psychiatry.html">Психиатрия</a></li>' +
        '<li><a href="service-psy-home.html">Психиатр на дом</a></li>' +
        '<li><a href="service-psy-psychologist.html">Клинический психолог</a></li>' +
        '<li><a href="service-psy-therapist.html">Психотерапевт</a></li>' +
        '<li><a href="service-psy-neurologist.html">Невролог</a></li>' +
        '<li><a href="service-psy-depression.html">Депрессия</a></li>' +
        '<li><a href="service-psy-psychosis.html">Психоз</a></li>' +
        '<li><a href="service-psy-delirium.html">Белая горячка</a></li>' +
        '<li><a href="service-psy-panic.html">Панические атаки</a></li>' +
        '<li><a href="service-psy-anxiety.html">Тревожное расстройство</a></li>' +
        '<li><a href="service-psy-insomnia.html">Бессонница</a></li>' +
        '<li><a href="service-psy-sleep.html">Нарушения сна</a></li>' +
        '<li><a href="service-psy-meds.html">Лекарственная зависимость</a></li>' +
        '<li><a href="service-psy-ocd.html">ОКР</a></li>' +
        '<li><a href="service-psy-ptsd.html">ПТСР</a></li>' +
        '<li><a href="service-psy-bipolar.html">Биполярное</a></li>' +
        '<li><a href="service-psy-schizophrenia.html">Шизофрения</a></li>' +
        '<li><a href="service-psy-adhd.html">СДВГ</a></li>' +
        '<li><a href="service-psy-bpd.html">ПРЛ</a></li>' +
        '<li><a href="service-psy-tad.html">Тревожно-депрессивное</a></li>' +
        '<li><a href="service-psy-gad.html">ГТР</a></li>' +
        '<li><a href="service-psy-stress.html">Стресс</a></li>' +
        '<li><a href="service-psy-neurosis.html">Неврозы</a></li>' +
        '<li><a href="service-psy-paranoia.html">Паранойя</a></li>' +
        '<li><a href="service-psy-dementia.html">Деменция</a></li>' +
        '<li><a href="service-psy-anorexia.html">Анорексия</a></li>' +
        '<li><a href="service-psy-bulimia.html">Булимия</a></li>' +
        '<li><a href="service-psy-dysmorpho.html">Дисморфофобия</a></li>' +
        '<li><a href="service-psy-asthenia.html">Астения</a></li>' +
        '<li><a href="service-psy-apathy.html">Апатия</a></li>' +
        '<li><a href="service-psy-kleptomania.html">Клептомания</a></li>' +
        '<li><a href="service-psy-narcolepsy.html">Нарколепсия</a></li>' +
        '<li><a href="service-psy-tourette.html">Синдром Туретта</a></li>' +
        '<li><a href="service-psy-sociopathy.html">Социопатия</a></li>' +
        '<li><a href="service-psy-somnolence.html">Сонливость</a></li>' +
        '<li><a href="service-psy-hypochondria.html">Ипохондрия</a></li>' +
        '<li><a href="service-psy-autoaggression.html">Аутоагрессия</a></li>' +
        '<li><a href="service-psy-neurasthenia.html">Неврастения</a></li>' +
        '<li><a href="service-psy-autophobia.html">Аутофобия</a></li>' +
        '<li><a href="service-psy-cyclothymia.html">Циклотимия</a></li>' +
        "</ul></div>" +
        "</div>";
      const copy = footWrap.querySelector(".footer__copy");
      if (copy) copy.before(services);
      else footWrap.appendChild(services);
    }

    if (footWrap && !footWrap.querySelector(".footer__disc")) {
      const copy = footWrap.querySelector(".footer__copy");
      if (copy) {
        const disc = doc.createElement("p");
        disc.className = "footer__disc";
        disc.innerHTML = "Медицинские услуги оказываются совершеннолетним пациентам добровольно, по адресу клиники или на дому по месту вызова. Телефонная консультация носит информационный характер и не заменяет осмотр. Сайт не является публичной офертой. 18+. Имеются противопоказания.";
        copy.before(disc);
      }
    }

    doc.querySelectorAll("a[data-city-max]").forEach((a) => {
      if (a.querySelector(".icon-max")) return;
      const icon = doc.createElement("img");
      icon.className = "icon-max";
      icon.src = "images/Max_logo.svg";
      icon.alt = "";
      icon.width = 18;
      icon.height = 18;
      icon.setAttribute("decoding", "async");
      a.prepend(icon);
      if (!a.getAttribute("aria-label")) a.setAttribute("aria-label", "Max");
    });

    doc.querySelectorAll("select[name=\"program\"]").forEach((sel) => {
      if (sel.dataset.enriched) return;
      sel.dataset.enriched = "1";
      const extra = ["Лечение алкоголизма", "Лечение наркомании", "Снятие ломки", "Игровая зависимость", "УБОД", "Рассрочка / точный расчёт"];
      extra.forEach((t) => {
        if ([...sel.options].some((o) => o.textContent === t)) return;
        const o = doc.createElement("option");
        o.textContent = t;
        sel.appendChild(o);
      });
    });
  };

  const calc = () => {
    const root = doc.querySelector("[data-calc]");
    if (!root) return;
    const steps = [
      { q: "Что сейчас важнее?", short: "Запрос", opts: ["Алкоголизм", "Наркомания", "Игровая зависимость", "Токсикомания", "Срочный запой"] },
      { q: "Какой горизонт нужен?", short: "Цель", opts: ["Снять острое состояние", "Закрепить результат кодированием", "Полная реабилитация"] },
      { q: "Кому нужна помощь?", short: "Кому", opts: ["Мне", "Мужу или жене", "Сыну или дочери 18+", "Близкому"] },
      { q: "Человек готов разговаривать с врачом?", short: "Готовность", opts: ["Да, сам просит помощи", "Сомневается", "Пока отказывается"] }
    ];
    let i = 0;
    let busy = false;
    const picks = [];
    const panel = root.querySelector("[data-calc-panel]");
    const q = root.querySelector("[data-calc-q]");
    const opts = root.querySelector("[data-calc-opts]");
    const summary = root.querySelector("[data-calc-summary]");
    const dots = root.querySelector("[data-calc-dots]");
    const back = root.querySelector("[data-calc-back]");
    const form = root.querySelector("[data-calc-form]");

    const renderSummary = () => {
      if (!summary) return;
      summary.innerHTML =
        "<p class=\"calc-summary__title\">Краткое резюме</p><ul>" +
        steps.map((step, n) =>
          "<li><span>" + step.short + "</span><b>" + (picks[n] || "—") + "</b></li>"
        ).join("") +
        "</ul><p class=\"calc-summary__note\">Оставьте телефон — врач подтвердит программу и ориентир по стоимости.</p>";
    };

    const fill = () => {
      dots.innerHTML = steps.map((_, n) => {
        const on = i >= steps.length || n <= i;
        return "<i class=\"" + (on ? "is-on" : "") + "\"></i>";
      }).join("");

      if (i >= steps.length) {
        q.textContent = "Расчёт почти готов";
        opts.hidden = true;
        opts.innerHTML = "";
        renderSummary();
        if (summary) summary.hidden = false;
        form.hidden = false;
        back.hidden = false;
        return;
      }

      form.hidden = true;
      if (summary) {
        summary.hidden = true;
        summary.innerHTML = "";
      }
      opts.hidden = false;
      q.textContent = steps[i].q;
      opts.innerHTML = steps[i].opts.map((t) => "<button type=\"button\">" + t + "</button>").join("");
      back.hidden = i === 0;
    };

    const paint = (dir = 0) => {
      if (!panel || !dir) {
        fill();
        if (panel) panel.classList.add("is-ready");
        return;
      }
      if (busy) return;
      busy = true;
      panel.classList.remove("is-ready");
      panel.classList.add(dir > 0 ? "is-leave-next" : "is-leave-back");
      window.setTimeout(() => {
        fill();
        panel.classList.remove("is-leave-next", "is-leave-back");
        panel.classList.add(dir > 0 ? "is-enter-next" : "is-enter-back");
        window.requestAnimationFrame(() => {
          window.requestAnimationFrame(() => {
            panel.classList.remove("is-enter-next", "is-enter-back");
            panel.classList.add("is-ready");
            busy = false;
          });
        });
      }, 240);
    };

    opts.addEventListener("click", (e) => {
      const b = e.target.closest("button");
      if (!b || opts.hidden || busy) return;
      picks[i] = b.textContent.trim();
      b.classList.add("is-on");
      i += 1;
      paint(1);
    });
    back.addEventListener("click", (e) => {
      e.preventDefault();
      if (i <= 0 || busy) return;
      i -= 1;
      paint(-1);
    });

    const formEl = form && form.querySelector("form[data-form]");
    if (formEl) {
      formEl.addEventListener("submit", (e) => {
        e.preventDefault();
        if (busy) return;
        form.classList.add("is-sent");
        if (summary) summary.hidden = true;
        q.textContent = "Заявка отправлена";
        back.hidden = true;
        busy = true;
        window.setTimeout(() => {
          form.classList.remove("is-sent");
          formEl.reset();
          picks.length = 0;
          i = 0;
          busy = false;
          paint(1);
        }, 3400);
      });
    }

    fill();
    if (panel) panel.classList.add("is-ready");
  };

  const stickyLead = () => {
    doc.querySelectorAll(".float-call").forEach((n) => n.remove());
    if (doc.querySelector("[data-sticky-lead]")) {
      body.classList.add("has-sticky-lead");
      return;
    }

    const bar = doc.createElement("div");
    bar.className = "sticky-lead";
    bar.setAttribute("data-sticky-lead", "");
    bar.innerHTML =
      '<div class="sticky-lead__inner">' +
        '<a class="sticky-lead__call" href="tel:+73812901212" data-city-tel>' +
          '<span class="sticky-lead__label">Вызов врача</span>' +
          '<strong class="sticky-lead__phone" data-city-phone>+7 (3812) 90-12-12</strong>' +
        "</a>" +
        '<div class="sticky-lead__actions">' +
          '<a class="sticky-lead__btn sticky-lead__btn--max" href="https://max.ru/" data-city-max target="_blank" rel="noopener" aria-label="Max">' +
            '<span class="sticky-lead__ico"><img class="icon-max" src="images/Max_logo.svg" alt="" width="15" height="15" decoding="async"></span>' +
            "<span>Max</span>" +
          "</a>" +
          '<a class="sticky-lead__btn sticky-lead__btn--tg" href="https://t.me/+73812901212" data-city-tg target="_blank" rel="noopener" aria-label="Telegram">' +
            '<span class="sticky-lead__ico"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.43 4.53 3.87 11.32c-1.2.47-1.19 1.13-.22 1.43l4.5 1.4 10.45-6.59c.5-.3.95-.13.58.18l-8.46 7.63-.33 4.72c.48 0 .69-.22.96-.48l2.3-2.24 4.78 3.53c.88.48 1.51.23 1.73-.81l3.13-14.74c.32-1.28-.49-1.86-1.36-1.42Z"/></svg></span>' +
            "<span>Telegram</span>" +
          "</a>" +
          '<a class="sticky-lead__btn sticky-lead__btn--phone" href="tel:+73812901212" data-city-tel aria-label="Позвонить">' +
            '<span class="sticky-lead__ico"><span class="icon-phone" aria-hidden="true"></span></span>' +
            "<span>Звонок</span>" +
          "</a>" +
        "</div>" +
      "</div>";
    body.appendChild(bar);
    body.classList.add("has-sticky-lead");
  };

  stickyLead();
  splitHeadings();
  geo();
  catalogNav();
  preload();
  tilt();
  header();
  mobileNav();
  reveals();
  counters();
  accordion();
  modal();
  forms();
  year();
  cookies();
  marquee();
  calc();
})();
