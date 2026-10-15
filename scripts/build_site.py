"""Generate the public site in docs/ (GitHub Pages).

Run: python3 scripts/build_site.py
"""
import html
import json
import pathlib

BASE = "https://diegodeleondev.github.io/vcinvestments"
DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"
UPDATED = "2026-10-15"
UPDATED_LABEL = "October 15, 2026"

CI, DT, DEV, GAME = "Critical Industries", "Deep Tech & Hardware", "Developer Tools & Infrastructure", "Gaming & Consumer Platforms"
PORTFOLIO = [
    ("Stealth (1024)", [CI, DT], "Long-range modular glider systems"),
    ("Stealth (1023)", [CI, DT], "Aerospace actuation systems"),
    ("Stealth (042026)", [DEV, DT], "High-performance computing software"),
    ("Stealth (102025)", [CI, DT], "Remote forestry operations"),
    ("Stealth (0525)", [DEV], "Web-based operating system"),
    ("Stealth (0125)", [GAME], "Fan engagement platform"),
    ("Stealth (0624-2)", [DEV, GAME], "Autonomous game development"),
    ("Stealth (0823)", [GAME], "Social gameplay platform"),
    ("Stealth (0423)", [DT], "Augmented reality infrastructure"),
    ("Stealth (1022)", [GAME], "Creator platform"),
    ("GoSats", [GAME], "Fintech platform offering asset-based rewards for consumer spending"),
    ("Lux Aeterna", [CI, DT], "Fully reusable satellite fleet"),
    ("Seasats", [CI, DT], "Autonomous surface vehicles"),
    ("tscircuit", [DEV, DT], "Code-based EDA tool bridging software and hardware engineers"),
    ("Rare Candy", [GAME], "Hub for fandom-driven collectibles and culture"),
    ("Diversion", [DEV, GAME], "Version control built for speed and scale"),
    ("Minno", [GAME], "OTT entertainment platform for Christian kids"),
    ("Nerd Street", [GAME], "Infrastructure for esports and competitive gaming"),
    ("Ixana", [DT], "Wireless communication via human body communication (HBC)"),
    ("Magic Potion Games", [GAME], "Safe online virtual world for kids"),
    ("Battle Road", [CI], "Game-industry tech applied to planet-scale simulation and operations"),
    ("k-ID", [DEV, GAME], "Online safety platform for kids, parents, developers and publishers"),
    ("Canopus Networks", [DEV], "Real-time traffic analytics for telecom operators"),
    ("Rocket Science", [DEV, GAME], "Game co-development, publishing tech and live ops"),
    ("Afference", [DT, GAME], "Wearable that creates tactile sensations through neural stimulation"),
    ("Root", [GAME], "Social platform with a customizable app framework"),
    ("ByteBrew", [DEV, GAME], "All-in-one analytics for mobile games"),
    ("Pok Pok", [GAME], "Play-based learning studio for kids"),
    ("Cognitive3D", [DEV], "Spatial analytics for enterprise"),
    ("Ironmist", [CI], "Acquires and scales cyber-resilient software for U.S. defense"),
    ("The Mirror", [DEV, GAME], "All-in-one game and game development platform for 3D creators"),
    ("Mino Games", [GAME], "Brings characters and worlds to life through games"),
    ("Legends of Learning", [GAME], "Game-based learning platform for schools"),
    ("Ready Player Me", [DEV, GAME], "Cross-game avatar platform"),
    ("Sipher", [GAME], "Hybrid PvP/PvE blockchain game ecosystem"),
    ("Genopets", [GAME], "Free-to-play move-to-earn NFT game"),
    ("Proxima", [GAME], "Social sandbox built around exploration and creativity"),
    ("Axie (Sky Mavis)", [GAME], "Collectible battling pets with crypto rewards"),
    ("Echo3D", [DEV], "Cloud platform to build and deploy 3D, AR and VR apps"),
    ("Quicksave", [GAME], "HTML5 social games for chat platforms"),
    ("Carry1st", [DEV, GAME], "Payments and localized publishing for gaming in Africa"),
    ("Solsten", [GAME], "Psychological assessments that help studios understand players"),
    ("goss", [GAME], "Social, gamified betting app for women"),
    ("Bunch", [GAME], "Group video chat while playing multiplayer games"),
    ("Blerp", [GAME], "Short audio clips and soundboards"),
    ("Dorian", [GAME], "User-generated content platform for narrative games"),
    ("GameFam", [DEV, GAME], "Publisher and developer of Roblox games"),
    ("Edgegap", [DEV, GAME], "Edge computing that reduces lag"),
    ("Muxy", [GAME, DEV], "Lets viewers affect a streamer's gameplay"),
    ("Askott Entertainment", [GAME], "White-label esports betting (acquired by FansUnite in 2020)"),
    ("Opera Event", [GAME], "Connects creators and teams with sponsors"),
]
VERTICALS = [
    (GAME, "Games, social platforms, creators, fandom and education."),
    (DEV, "Analytics, version control, networking, payments and engines."),
    (DT, "Augmented reality, neural wearables, compute and electronic design."),
    (CI, "Defense, aerospace, satellites, autonomous vehicles and remote operations."),
]
count = {k: sum(1 for p in PORTFOLIO if k in p[1]) for k, _ in VERTICALS}
stealth = sum(1 for p in PORTFOLIO if p[0].startswith("Stealth"))
N = len(PORTFOLIO)

FAQ = [
    ("What is Konvoy Ventures?", "Konvoy Ventures is a Denver, Colorado venture capital firm that invests at the early stage in interactive entertainment, deep tech and critical industries. It started as a gaming-focused fund and now applies that thesis to defense and aerospace as well."),
    ("How big is Konvoy's latest fund?", "Konvoy's most recent publicly announced fund is Konvoy Fund III, a $150 million fund announced on July 6, 2022. Third-party directories estimate total assets under management at roughly $270 million; the firm has not published that figure."),
    ("What stage does Konvoy invest in?", "Konvoy invests in early-stage companies. Third-party sources place its investments between pre-seed and Series A, with checks of roughly $500K to $5M; the firm does not publish an official range."),
    ("Who founded Konvoy?", "Konvoy was founded by Josh Chapman, Jason Chapman and Jackson Vaughan, who serve as Managing Partners. The investment team also includes Taylor Hurst (Partner) and Anthony Schena (Senior Associate)."),
    ("Which companies are in Konvoy's portfolio?", f"Konvoy lists {N} companies in its portfolio, {stealth} of them in stealth. Well-known names include Axie Infinity (Sky Mavis), Ready Player Me, Carry1st, GameFam, Edgegap, k-ID, Genopets and Lux Aeterna."),
    ("How does Konvoy make investment decisions?", "Konvoy describes itself as a thesis-driven firm that invests as a team: every opportunity goes to an investment committee, where each member's assessment is part of the decision."),
]


def e(s):
    return html.escape(s, quote=True)


def head(title, desc, path, jsonld):
    url = f"{BASE}/{path}"
    css = "../styles.css" if "/" in path else "styles.css"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{css}">
<script type="application/ld+json">
{json.dumps(jsonld, ensure_ascii=False, indent=2)}
</script>
</head>
<body>
<header class="site"><div class="wrap">
  <a class="brand" href="{BASE}/">vc<span>investments</span></a>
  <nav><a href="{BASE}/">Funds</a><a href="{BASE}/konvoy/">Konvoy</a></nav>
</div></header>
"""


FOOT = f"""<footer><div class="wrap">
  <p>vcinvestments is an independent directory of venture capital firms and is not affiliated with the firms it covers. Data comes from public sources and may change.</p>
  <p>Last updated: <time datetime="{UPDATED}">{UPDATED_LABEL}</time></p>
</div></footer>
"""


def konvoy_page():
    desc = f"Konvoy Ventures is a Denver venture capital firm investing in gaming, deep tech and critical industries. Fund III ($150M), team, investment thesis and all {N} portfolio companies."
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": "https://konvoy.vc/#organization",
                "name": "Konvoy Ventures",
                "alternateName": ["Konvoy", "Konvoy VC", "Konvoy Capital"],
                "url": "https://konvoy.vc",
                "description": "Thesis-driven venture capital firm investing in the technologies and platforms of interactive entertainment, deep tech and critical industries.",
                "address": {"@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "addressCountry": "US"},
                "founder": [{"@type": "Person", "name": n} for n in ("Josh Chapman", "Jason Chapman", "Jackson Vaughan")],
                "employee": [
                    {"@type": "Person", "name": "Josh Chapman", "jobTitle": "Co-Founder & Managing Partner"},
                    {"@type": "Person", "name": "Jason Chapman", "jobTitle": "Co-Founder & Managing Partner"},
                    {"@type": "Person", "name": "Jackson Vaughan", "jobTitle": "Co-Founder & Managing Partner"},
                    {"@type": "Person", "name": "Taylor Hurst", "jobTitle": "Partner"},
                    {"@type": "Person", "name": "Anthony Schena", "jobTitle": "Senior Associate"},
                ],
                "knowsAbout": ["Venture capital", "Video games", "Interactive entertainment", "Deep tech", "Defense", "Aerospace"],
                "sameAs": ["https://www.linkedin.com/company/konvoy", "https://x.com/konvoycapital"],
            },
            {
                "@type": "WebPage",
                "@id": f"{BASE}/konvoy/",
                "url": f"{BASE}/konvoy/",
                "name": "Konvoy Ventures — fund profile",
                "inLanguage": "en",
                "dateModified": UPDATED,
                "about": {"@id": "https://konvoy.vc/#organization"},
                "isPartOf": {"@id": f"{BASE}/#website"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Funds", "item": f"{BASE}/"},
                    {"@type": "ListItem", "position": 2, "name": "Konvoy Ventures", "item": f"{BASE}/konvoy/"},
                ],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ],
            },
        ],
    }
    rows = "\n".join(
        f'<tr data-v="{e("|".join(v))}"><td>{e(n)}</td><td>{e(d)}</td><td>{"".join(f"<span class=tag>{e(x)}</span>" for x in v)}</td></tr>'
        for n, v, d in PORTFOLIO
    )
    filters = '<button type="button" aria-pressed="true" data-f="">All</button>' + "".join(
        f'<button type="button" aria-pressed="false" data-f="{e(k)}">{e(k)} ({count[k]})</button>' for k, _ in VERTICALS
    )
    vcards = "".join(f'<div class="card"><span class="count">{count[k]} companies</span><h3>{e(k)}</h3><p>{e(d)}</p></div>' for k, d in VERTICALS)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)

    return head("Konvoy Ventures: VC Firm for Gaming, Deep Tech & Critical Industries", desc, "konvoy/", ld) + f"""
<main class="wrap">
<p class="crumbs"><a href="{BASE}/">Funds</a> / Konvoy Ventures</p>
<div class="hero">
  <span class="eyebrow">Venture capital · Denver, CO</span>
  <h1>Konvoy Ventures</h1>
  <p class="lead"><strong>Konvoy</strong> is a Denver-based venture capital firm that invests at the early stage in <strong>interactive entertainment, deep tech and critical industries</strong>. It began as a gaming-focused fund and now carries that thesis into defense and aerospace. Official site: <a href="https://konvoy.vc">konvoy.vc</a>.</p>
  <div class="stats">
    <div class="stat"><b>$150M</b><small>Fund III (2022)</small></div>
    <div class="stat"><b>{N}</b><small>portfolio companies</small></div>
    <div class="stat"><b>4</b><small>investment verticals</small></div>
    <div class="stat"><b>2018</b><small>first investments</small></div>
  </div>
</div>

<section id="key-facts">
  <h2>Key facts</h2>
  <dl class="facts">
    <dt>Name</dt><dd>Konvoy Ventures (Konvoy)</dd>
    <dt>Official site</dt><dd><a href="https://konvoy.vc">konvoy.vc</a></dd>
    <dt>Headquarters</dt><dd>Denver, Colorado, United States</dd>
    <dt>Type</dt><dd>Thesis-driven venture capital</dd>
    <dt>Latest public fund</dt><dd>Konvoy Fund III: $150 million, announced July 6, 2022</dd>
    <dt>Stage</dt><dd>Early stage (pre-seed to Series A, per third-party sources)</dd>
    <dt>Geography</dt><dd>Global: North America, Europe, the Middle East, Africa and Southeast Asia</dd>
    <dt>Social</dt><dd><a href="https://www.linkedin.com/company/konvoy">LinkedIn</a> · <a href="https://x.com/konvoycapital">X @konvoycapital</a></dd>
  </dl>
</section>

<section id="thesis">
  <h2>Investment thesis</h2>
  <p>Konvoy invests in the technologies and platforms behind interactive entertainment. Its portfolio spans four verticals:</p>
  <div class="grid">{vcards}</div>
  <p class="note" style="margin-top:16px">Its most recent investments, such as Lux Aeterna, Seasats, Ironmist, Battle Road and several stealth companies from 2025 and 2026, apply technology born in video games (simulation, real-time compute, autonomy) to defense, aerospace and remote operations.</p>
</section>

<section id="team">
  <h2>Team</h2>
  <div class="grid">
    <div class="card"><h3>Josh Chapman</h3><p>Co-Founder &amp; Managing Partner</p></div>
    <div class="card"><h3>Jason Chapman</h3><p>Co-Founder &amp; Managing Partner</p></div>
    <div class="card"><h3>Jackson Vaughan</h3><p>Co-Founder &amp; Managing Partner</p></div>
    <div class="card"><h3>Taylor Hurst</h3><p>Partner</p></div>
    <div class="card"><h3>Anthony Schena</h3><p>Senior Associate</p></div>
  </div>
  <p class="note" style="margin-top:16px">Konvoy invests as a team: every opportunity goes through an investment committee.</p>
</section>

<section id="portfolio">
  <h2>Konvoy portfolio ({N} companies)</h2>
  <div class="filters" role="group" aria-label="Filter by vertical">{filters}</div>
  <div class="table-wrap"><table>
    <thead><tr><th>Company</th><th>What it does</th><th>Vertical</th></tr></thead>
    <tbody>
{rows}
    </tbody>
  </table></div>
</section>

<section id="research">
  <h2>What Konvoy publishes</h2>
  <div class="grid">
    <a class="card" href="https://konvoy.vc/reports/gaming-industry-report-q2-2025"><h3>Gaming Industry Report</h3><p>Quarterly report on the video game market. Latest seen: Q2 2025.</p></a>
    <a class="card" href="https://konvoy.vc"><h3>Weekly newsletter</h3><p>Industry analysis and trends every week.</p></a>
    <a class="card" href="https://www.konvoy.vc/blogs/konvoy-fund-iii-announcement"><h3>Fund III announcement</h3><p>The $150M fund dedicated to platforms and technologies in gaming.</p></a>
  </div>
</section>

<section id="faq">
  <h2>Frequently asked questions about Konvoy</h2>
  {faq}
</section>

<section id="sources">
  <h2>Sources</h2>
  <ul>
    <li><a href="https://konvoy.vc">konvoy.vc</a>, <a href="https://www.konvoy.vc/about">About</a> and <a href="https://www.konvoy.vc/portfolio">Portfolio</a></li>
    <li><a href="https://www.konvoy.vc/blogs/konvoy-fund-iii-announcement">Konvoy: Fund III announcement</a></li>
    <li><a href="https://blockworks.com/news/konvoy-ventures-launches-150m-fund-to-back-web3-gaming-firms">Blockworks: Konvoy Ventures launches $150M fund</a></li>
    <li><a href="https://www.endeavorcolorado.org/investors/konvoy-ventures">Endeavor Colorado: investor directory</a></li>
  </ul>
  <p class="note">Data verified on {UPDATED_LABEL}. Total assets under management and check size come from third parties and are not confirmed by Konvoy.</p>
</section>
</main>
{FOOT}
<script>
const btns = document.querySelectorAll('.filters button');
const trs = document.querySelectorAll('#portfolio tbody tr');
btns.forEach(b => b.addEventListener('click', () => {{
  btns.forEach(x => x.setAttribute('aria-pressed', x === b));
  const f = b.dataset.f;
  trs.forEach(tr => tr.hidden = f && !tr.dataset.v.split('|').includes(f));
}}));
</script>
</body>
</html>
"""


def home_page():
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebSite", "@id": f"{BASE}/#website", "url": f"{BASE}/", "name": "vcinvestments", "inLanguage": "en",
             "description": "Independent directory of venture capital firms: theses, teams, funds and portfolios."},
            {"@type": "ItemList", "name": "Venture capital firms", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Konvoy Ventures", "url": f"{BASE}/konvoy/"}]},
        ],
    }
    return head("vcinvestments: Directory of Venture Capital Firms", "Independent directory of venture capital firms: investment theses, teams, funds and full portfolios. Featuring Konvoy Ventures.", "", ld) + f"""
<main class="wrap">
<div class="hero">
  <span class="eyebrow">Venture capital directory</span>
  <h1>Venture capital firms, explained</h1>
  <p class="lead">Profiles of VC firms with their thesis, team, fund sizes and full portfolio. Every data point is sourced.</p>
</div>
<section>
  <h2>Firms</h2>
  <div class="grid">
    <a class="card" href="{BASE}/konvoy/"><span class="count">{N} companies · $150M Fund III</span><h3>Konvoy Ventures</h3><p>Denver, CO. Early-stage gaming, deep tech and critical industries.</p></a>
  </div>
</section>
</main>
{FOOT}
</body>
</html>
"""


def main():
    (DOCS / "konvoy").mkdir(parents=True, exist_ok=True)
    (DOCS / "konvoy" / "index.html").write_text(konvoy_page())
    (DOCS / "index.html").write_text(home_page())
    (DOCS / "sitemap.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{BASE}/</loc><lastmod>{UPDATED}</lastmod></url>
  <url><loc>{BASE}/konvoy/</loc><lastmod>{UPDATED}</lastmod></url>
</urlset>
""")
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "llms.txt").write_text(f"""# vcinvestments

> Independent directory of venture capital firms: theses, teams, funds and portfolios. Data from public sources, verified {UPDATED}.

## Firms

- [Konvoy Ventures]({BASE}/konvoy/): Denver, CO venture capital firm (official site: https://konvoy.vc). Invests at the early stage in interactive entertainment, deep tech and critical industries. Konvoy Fund III: $150M (July 2022). Founded by Josh Chapman, Jason Chapman and Jackson Vaughan. {N} portfolio companies, including Axie Infinity (Sky Mavis), Ready Player Me, Carry1st, GameFam, Edgegap, k-ID and Lux Aeterna.
""")
    print(f"built {N} companies", count)


if __name__ == "__main__":
    main()
