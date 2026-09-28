# -*- coding: utf-8 -*-
"""Builds Shiloh Ayala's site.

  python3 build.py          (builds both)
  python3 build.py site     (what Cloudflare Pages runs on every change)

Outputs
  site/     the real website, for Netlify / Cloudflare Pages (full HTML documents, YouTube embed)
  preview/  the same pages for the claude.ai artifact preview (index without a document
            skeleton, videos as link cards because the artifact frame blocks iframes)

To add a post or project, edit content.py and run this again.
"""
import html, os, re, shutil
from content import *

SITE_URL = "https://copecoder.com"   # change here if the domain ever changes
ROOT = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(ROOT, "style.css"), encoding="utf-8").read()
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;500;600'
         '&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">')
SITE_DESC = ("Shiloh Ayala, data analysis in mental healthcare. MSc Health Innovation & Data Science student at "
             "emlyon business school, open to data analytics internships in Lyon or Paris from April 2027.")

ICON_MAIL = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"></rect>'
             '<path d="m3 7 9 6 9-6"></path></svg>')
ICON_DL = ('<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11"></path><path d="m7 10 5 5 5-5"></path>'
           '<path d="M5 20h14"></path></svg>')
ICON_PLAY = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"></path></svg>'
ICON_EXT = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7"></path><path d="M8 7h9v9"></path></svg>')

FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#3E1921"/>'
           '<text x="32" y="42" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="26" '
           'font-weight="600" letter-spacing="1" fill="#FFFFFF">SA</text></svg>')

YEAR = 2026


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def attr(s):
    return html.escape(strip_tags(s), quote=True)


# ------------------------------------------------------------------ page shell
def page(mode, depth, title, desc, body, is_index=False, canonical=""):
    up = "../" * depth
    head = [f"<title>{html.escape(title)}</title>"]
    if mode == "site" or not is_index:
        head.insert(0, '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">')
    head.append(f'<meta name="description" content="{attr(desc)}">')
    if mode == "site":
        url = SITE_URL + "/" + canonical
        head += [
            f'<link rel="canonical" href="{url}">',
            '<meta property="og:type" content="website">',
            f'<meta property="og:title" content="{attr(title)}">',
            f'<meta property="og:description" content="{attr(desc)}">',
            f'<meta property="og:url" content="{url}">',
            f'<meta property="og:image" content="{SITE_URL}/assets/portrait.jpg">',
            '<meta name="twitter:card" content="summary">',
            '<meta name="theme-color" content="#3E1921">',
        ]
    head.append(f'<link rel="icon" href="{up}favicon.svg" type="image/svg+xml">')
    head.append(FONTS)
    head.append(f"<style>\n{CSS}\n</style>")
    headhtml = "\n".join(head)
    if mode == "preview" and is_index:
        return headhtml + "\n" + body + "\n"
    return f'<!doctype html>\n<html lang="en">\n<head>\n{headhtml}\n</head>\n<body>\n{body}\n</body>\n</html>\n'


def footer(up):
    return f"""<footer class="site-footer">
<span>© {YEAR} Shiloh Ayala · <span class="email-plain">{EMAIL}</span></span>
<nav aria-label="Elsewhere"><a href="{LINKEDIN}">LinkedIn</a><a href="{GITHUB}">GitHub</a><a href="{up}{CV}" target="_blank" rel="noopener">CV (PDF)</a></nav>
</footer>"""


def bar(up, current):
    def a(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{up}{href}"{cur}>{label}</a>'
    return f"""<header class="bar"><div class="bar-inner">
<a class="bar-name" href="{up}index.html">Shiloh Ayala</a>
<nav aria-label="Main">{a('work.html', 'Work', 'work')}{a('writing.html', 'Writing', 'writing')}<a href="{up}{CV}" target="_blank" rel="noopener">CV</a></nav>
</div></header>"""


# ------------------------------------------------------------------ components
def card(p, up):
    tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
    return f"""<a class="card" href="{up}work/{p['slug']}.html">
<div class="card-head"><span class="card-title">{p['title']}</span><span class="card-meta">{p['meta']}</span></div>
<img class="card-img" src="{up}assets/{p['thumb']}" alt="{attr(p['thumb_alt'])}" style="object-position: {p['thumb_pos']}" loading="lazy">
<span class="card-desc">{p['desc']}</span>
<span class="tags">{tags}</span>
</a>"""


def post_row(p, up):
    return f"""<a class="post" href="{up}writing/{p['slug']}.html">
<span class="post-body">
<span class="post-title">{p['title']}</span>
<img class="post-img" src="{up}assets/{p['img']}" alt="{attr(p['img_alt'])}" loading="lazy">
<span class="post-teaser">{p['teaser']}</span>
</span>
<span class="post-date">{p['date']}</span>
</a>"""


def video(key, mode):
    v = VIDEOS[key]
    if mode == "site" and v["embed"]:
        return f"""<figure class="video-embed">
<div class="frame"><iframe src="{v['embed']}" title="{attr(v['title'])}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>{v['by']}</figcaption>
</figure>"""
    return f"""<a class="video-card" href="{v['url']}">
<span class="play">{ICON_PLAY}</span>
<span class="vc-text"><strong>{v['title']}</strong><span class="vc-by">{v['by']} · watch on {v['site']}</span></span>
</a>"""


def sources_block(items, numbered):
    if not items:
        return ""
    if numbered:
        lis = "".join(f'<li id="ref-{i}">{s} <a class="back" href="#cite-{i}" aria-label="Back to text">↩</a></li>'
                      for i, s in enumerate(items, 1))
        return f'<section class="sources"><h2>Sources</h2><ol>{lis}</ol></section>'
    lis = "".join(f"<li>{s}</li>" for s in items)
    return f'<section class="sources"><h2>Sources</h2><ul>{lis}</ul></section>'


def related_block(rel):
    if not rel:
        return ""
    label, href, title = rel
    return f'<a class="related" href="{href}"><span class="label">{label}</span><span class="related-title">{title} <span class="arrow">→</span></span></a>'


def fill_videos(body, mode):
    return re.sub(r"\{\{VIDEO:(\w+)\}\}", lambda m: video(m.group(1), mode), body)


# ------------------------------------------------------------------ pages
def index_page(mode):
    up = ""
    cards = "\n".join(card(p, up) for p in PROJECTS)
    posts = "\n".join(post_row(p, up) for p in POSTS[:4])
    body = f"""<div class="home">
<aside class="panel">
<nav class="phone-nav only-phone" aria-label="Main"><a href="work.html">Work</a><a href="writing.html">Writing</a><a href="{CV}" target="_blank" rel="noopener">CV</a></nav>
<div class="panel-id">
<img class="portrait" src="assets/portrait.jpg" alt="Portrait of Shiloh Ayala" width="240" height="300">
<div>
<h1 class="name">Shiloh Ayala</h1>
<p class="tagline"><span class="long">{TAGLINE_LONG}</span><span class="short">{TAGLINE_SHORT}</span></p>
</div>
</div>
<div class="pill"><span class="dot" aria-hidden="true"></span>Open to internships · April 2027</div>
<div class="contact">
<a class="btn-primary" href="mailto:{EMAIL}">{ICON_MAIL}Email me</a>
<div class="btn-row">
<a class="btn-outline" href="{LINKEDIN}">LinkedIn</a>
<a class="btn-outline" href="{GITHUB}">GitHub</a>
<a class="btn-outline" href="{CV}" target="_blank" rel="noopener">{ICON_DL}CV</a>
</div>
</div>
<dl class="facts">
<div><dt class="label">Seeking</dt><dd>Data analytics internship, 4+ months</dd></div>
<div><dt class="label">Where</dt><dd>Lyon or Paris, English-speaking team</dd></div>
<div><dt class="label">Available</dt><dd>From 1 April 2027</dd></div>
</dl>
</aside>
<div class="home-main">
<nav class="topnav only-desk" aria-label="Sections"><a href="#about">About</a><a href="work.html">Work</a><a href="writing.html">Writing</a></nav>
<main class="home-content">
<section id="about">
<h2 class="section-title big">About</h2>
<p class="bio"><span class="long">{BIO_LONG}</span><span class="short">{BIO_SHORT}</span></p>
</section>
<section class="tiles" aria-label="Internship details">
<div class="tile"><span class="label">Seeking</span><span>Data analytics, 4+ months</span></div>
<div class="tile"><span class="label">Where</span><span>Lyon or Paris, in English</span></div>
<div class="tile"><span class="label">From</span><span>1 April 2027</span></div>
</section>
<section id="work">
<div class="section-head"><h2 class="section-title">Work</h2><a class="more" href="work.html"><span class="long">All projects</span><span class="short">All</span> <span class="arr">→</span></a></div>
<div class="cards">
{cards}
</div>
</section>
<section id="writing">
<div class="section-head"><h2 class="section-title">Writing</h2><a class="more" href="writing.html"><span class="long">All posts</span><span class="short">All</span> <span class="arr">→</span></a></div>
<div class="posts">
{posts}
</div>
</section>
</main>
{footer(up)}
</div>
</div>"""
    return page(mode, 0, "Shiloh Ayala", SITE_DESC, body, is_index=True, canonical="")


def work_page(mode):
    up = ""
    cards = "\n".join(card(p, up) for p in PROJECTS)
    body = f"""{bar(up, 'work')}
<main class="page wide">
<a class="crumb" href="index.html">← Home</a>
<h1 class="page-title caps-title">Work</h1>
<div class="cards">
{cards}
</div>
</main>
<div class="inner-footer wide">{footer(up)}</div>"""
    return page(mode, 0, "Work · Shiloh Ayala", "Data projects by Shiloh Ayala, newest first.", body, canonical="work.html")


def writing_page(mode):
    up = ""
    posts = "\n".join(post_row(p, up) for p in POSTS)
    body = f"""{bar(up, 'writing')}
<main class="page">
<a class="crumb" href="index.html">← Home</a>
<h1 class="page-title caps-title">Writing</h1>
<div class="posts">
{posts}
</div>
</main>
<div class="inner-footer">{footer(up)}</div>"""
    return page(mode, 0, "Writing · Shiloh Ayala", "Posts by Shiloh Ayala on mental health, data and health systems.", body, canonical="writing.html")


def project_page(p, mode):
    up = "../"
    tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
    cover = ""
    if p.get("cover"):
        img, alt, cap = p["cover"]
        cover = f'<figure class="cover"><img src="{up}assets/{img}" alt="{attr(alt)}"></figure>'
    facts = []
    if p.get("data_note"):
        facts.append(("Data", re.sub(r"^Data: ", "", p["data_note"]).rstrip(".")))
    if p.get("tools"):
        facts.append(("Tools", p["tools"]))
    for label, href in p.get("links", []):
        facts.append(("Code", f'<a href="{href}">{href.replace("https://", "")}</a>'))
    facts_html = ""
    if facts:
        facts_html = '<dl class="proj-facts">' + "".join(
            f'<div><dt class="label">{k}</dt><dd>{v}</dd></div>' for k, v in facts) + "</dl>"
    links = ""
    if p.get("links"):
        links = '<div class="links-row">' + "".join(
            f'<a class="link-btn" href="{h}">{l} {ICON_EXT}</a>' for l, h in p["links"]) + "</div>"
    body = f"""{bar(up, 'work')}
<main class="page">
<a class="crumb" href="{up}work.html">← Work</a>
<h1 class="page-title">{p['title']}</h1>
<div class="page-meta">{p['date']} · {p['context']}</div>
<div class="tags">{tags}</div>
{facts_html}
{cover}
<article class="prose">
{fill_videos(p['body'], mode)}
</article>
{links}
{related_block(p.get('related'))}
{sources_block(p['sources'], numbered=True)}
</main>
<div class="inner-footer">{footer(up)}</div>"""
    return page(mode, 1, f"{strip_tags(p['title'])} · Shiloh Ayala", p["desc"], body, canonical=f"work/{p['slug']}.html")


def post_page(p, mode):
    up = "../"
    cap = f"<figcaption>{p['credit']}</figcaption>" if p.get("credit") else ""
    body = f"""{bar(up, 'writing')}
<main class="page">
<a class="crumb" href="{up}writing.html">← Writing</a>
<h1 class="page-title">{p['title']}</h1>
<div class="page-meta">{p['date']}</div>
<figure class="cover"><img src="{up}assets/{p['img']}" alt="{attr(p['img_alt'])}">{cap}</figure>
<article class="prose">
{fill_videos(p['body'], mode)}
</article>
{related_block(p.get('related'))}
{sources_block(p['sources'], numbered=False)}
</main>
<div class="inner-footer">{footer(up)}</div>"""
    return page(mode, 1, f"{strip_tags(p['title'])} · Shiloh Ayala", strip_tags(p["teaser"]), body,
                canonical=f"writing/{p['slug']}.html")


def not_found():
    body = f"""{bar('/', '')}
<main class="page">
<h1 class="page-title caps-title">Page not found</h1>
<p class="list-intro">This page doesn’t exist, or it moved.</p>
<p><a class="crumb" href="/index.html">← Back to the homepage</a></p>
</main>"""
    return page("site", 0, "Page not found · Shiloh Ayala", SITE_DESC, body, canonical="404.html").replace('href="favicon.svg"', 'href="/favicon.svg"')


# ------------------------------------------------------------------ write
def build(mode):
    out = os.path.join(ROOT, mode)
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(os.path.join(out, "work"))
    os.makedirs(os.path.join(out, "writing"))
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(out, "assets"))
    files = {
        "index.html": index_page(mode),
        "work.html": work_page(mode),
        "writing.html": writing_page(mode),
        "favicon.svg": FAVICON,
    }
    for p in PROJECTS:
        files[f"work/{p['slug']}.html"] = project_page(p, mode)
    for p in POSTS:
        files[f"writing/{p['slug']}.html"] = post_page(p, mode)
    if mode == "site":
        files["404.html"] = not_found()
        urls = [""] + ["work.html", "writing.html"] + [f"work/{p['slug']}.html" for p in PROJECTS] + \
               [f"writing/{p['slug']}.html" for p in POSTS]
        files["sitemap.xml"] = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                + "".join(f"  <url><loc>{SITE_URL}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
        files["robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
    for name, text in files.items():
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(text)
    return sorted(files)


if __name__ == "__main__":
    import sys
    modes = sys.argv[1:] or ["site", "preview"]   # Cloudflare runs: python3 build.py site
    for m in modes:
        print(m, len(build(m)), "files")
