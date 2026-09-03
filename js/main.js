(() => {
  const doc = document;
  const body = doc.body;
  const KEY = "alba-city";

  const CITIES = [
    { id: "omsk", name: "Омск", prep: "в Омске", phone: "+7 (3812) 90-12-12", tel: "+73812901212", address: "Омск, ул. Красный Путь, 22", extra: "Центр, отдельный вход со двора. Трансфер по городу и области.", license: "ЛО-55-01-002891", map: "https://yandex.ru/map-widget/v1/?ll=73.368584%2C54.989347&z=16&text=%D0%9E%D0%BC%D1%81%D0%BA%2C%20%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B9%20%D0%9F%D1%83%D1%82%D1%8C%2C%2022" },
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
    doc.querySelectorAll("[data-city-wa]").forEach((a) => { a.setAttribute("href", "https://wa.me/" + digits); });
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
    const close = () => {
      burger.classList.remove("is-open");
      nav.classList.remove("is-open");
      body.classList.remove("is-lock");
    };
    burger.addEventListener("click", () => {
      const open = burger.classList.toggle("is-open");
      nav.classList.toggle("is-open", open);
      body.classList.toggle("is-lock", open);
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

  const cookies = () => {
    try { if (localStorage.getItem("alba-cookie")) return; } catch (e) {}
    const bar = doc.createElement("div");
    bar.className = "cookie";
    bar.innerHTML = "<p>Сайт запоминает выбранный город и использует cookie, чтобы показать телефон вашей клиники. Подробнее — в <a href=\"privacy.html\">политике персональных данных</a>.</p><button type=\"button\" class=\"btn btn--blue\">Понятно</button>";
    body.appendChild(bar);
    bar.querySelector("button").addEventListener("click", () => {
      try { localStorage.setItem("alba-cookie", "1"); } catch (e) {}
      bar.remove();
    });
  };

  splitHeadings();
  geo();
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
})();
