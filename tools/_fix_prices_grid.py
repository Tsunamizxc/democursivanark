# -*- coding: utf-8 -*-
from pathlib import Path
import re

path = Path(__file__).resolve().parent.parent / "prices.html"
html = path.read_text(encoding="utf-8")
m = re.search(
    r'(<section class="wrap price-block">)([\s\S]*?)(</section>\s*<section class="cta)',
    html,
)
if not m:
    raise SystemExit("block not found")

body = m.group(2)
chunks = re.split(r'(?=<h2>|<p class="price-note")', body)
out = ["\n      <div class=\"price-block__grid\">\n"]
for chunk in chunks:
    chunk = chunk.strip()
    if not chunk:
        continue
    if chunk.startswith('<p class="price-note"'):
        out.append("        " + chunk + "\n")
        continue
    if chunk.startswith("<h2>"):
        hm = re.match(
            r'(<h2>[\s\S]*?</h2>)\s*(<div class="price-wrap"[\s\S]*?</div>)',
            chunk,
        )
        if not hm:
            raise SystemExit("failed to parse chunk: " + chunk[:80])
        h2, wrap = hm.group(1), hm.group(2)
        out.append(
            "        <article class=\"price-card\">\n"
            f"          {h2}\n"
            f"          {wrap}\n"
            "        </article>\n"
        )

out.append("      </div>\n    ")
new_html = html[: m.start()] + m.group(1) + "".join(out) + m.group(3) + html[m.end() :]
path.write_text(new_html, encoding="utf-8")
print("price-card count:", new_html.count("price-card"))
