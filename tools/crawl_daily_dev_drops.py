#!/usr/bin/env python3
"""Browser-backed route discovery and Markdown export for Daily Dev Drops.

Run on your own computer with internet access:
    python -m pip install playwright
    python -m playwright install chromium
    python crawl_daily_dev_drops.py

Uses only public pages, rate limits crawling, never logs in or changes data.
Produces: devdailydrops_browser_crawl.md and devdailydrops_browser_crawl.json
"""

import asyncio, json, re, time
from collections import deque
from pathlib import Path
from xml.etree import ElementTree as ET
from urllib.parse import urljoin, urlsplit, urlunsplit
from playwright.async_api import async_playwright

BASE = "https://devdailydrops.pages.dev"
SEEDS = ["/", "/repos", "/plugins", "/secure", "/unmac", "/hosting", "/design", "/crew", "/fix", "/launch", "/unslop"]
SKIP_PREFIXES = ("/_", "/assets/", "/images/", "/static/", "/cdn-cgi/", "/api/")
OUTPUT_MD = "devdailydrops_browser_crawl.md"
OUTPUT_JSON = "devdailydrops_browser_crawl.json"
MAX_PAGES = 150


def internal_path(url):
    try:
        s = urlsplit(url)
        if s.netloc.lower() not in ("", "devdailydrops.pages.dev"):
            return None
        if s.scheme and s.scheme not in ("https", "http"):
            return None
        p = s.path or "/"
        if not p.startswith("/") or p.startswith(SKIP_PREFIXES):
            return None
        if re.search(r"\.(?:js|css|png|jpe?g|svg|woff2?|ico|pdf|json|webp|txt|xml)$", p, re.I):
            return None
        return p.rstrip("/") or "/"
    except Exception:
        return None


def markdown_safe(text):
    return str(text).replace("|", "\\|").replace("\r", " ").strip()


async def main():
    queue = deque(SEEDS)
    seen, results, script_urls = set(), [], set()
    discovered_from_js = set()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (compatible; PersonalResearchCrawler/1.0)")
        page = await context.new_page()
        # Discover additional routes from public sitemap(s) when available.
        sitemap_urls = {BASE + "/sitemap.xml"}
        try:
            rr = await context.request.get(BASE + "/robots.txt", timeout=10000)
            if rr.ok:
                for ln in (await rr.text()).splitlines():
                    if ln.lower().strip().startswith("sitemap:"):
                        sitemap_urls.add(ln.split(":", 1)[1].strip())
        except Exception:
            pass
        for sitemap_url in list(sitemap_urls)[:5]:
            try:
                sr = await context.request.get(sitemap_url, timeout=10000)
                if sr.ok:
                    root = ET.fromstring(await sr.text())
                    for el in root.iter():
                        if el.tag.endswith("loc") and el.text:
                            path = internal_path(el.text.strip())
                            if path and path not in queue:
                                queue.append(path)
            except Exception:
                pass
        while queue and len(seen) < MAX_PAGES:
            path = queue.popleft()
            if path in seen:
                continue
            seen.add(path)
            url = BASE + (path if path != "/" else "/")
            rec = {"path": path, "url": url, "status": None, "title": "", "text": "", "links": [], "github_links": [], "error": None}
            print(f"[{len(seen)}] {url}")
            try:
                response = await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                await page.wait_for_timeout(750)
                rec["status"] = response.status if response else None
                rec["title"] = await page.title()
                rec["text"] = (await page.locator("body").inner_text(timeout=10000))[:150000]
                links = await page.locator("a[href]").evaluate_all("els => els.map(a => a.href)")
                rec["links"] = sorted(set(links))
                rec["github_links"] = sorted(set(u for u in links if u.startswith("https://github.com/")))
                for u in links:
                    sub = internal_path(u)
                    if sub and sub not in seen and sub not in queue:
                        queue.append(sub)
                scripts = await page.locator("script[src]").evaluate_all("els => els.map(s => s.src)")
                script_urls.update(u for u in scripts if u.startswith(BASE))
            except Exception as e:
                rec["error"] = f"{type(e).__name__}: {e}"
            results.append(rec)
            await page.wait_for_timeout(250)

        # Scan same-origin JS assets for explicitly embedded route strings.
        route_regex = re.compile(r"[\"'`](/(?:[a-z][a-z0-9_-]*)(?:/[a-z0-9_-]+){0,3})[\"'`]", re.I)
        for url in sorted(script_urls):
            try:
                response = await context.request.get(url, timeout=20000)
                if response.ok:
                    js = (await response.text())[:3_000_000]
                    for m in route_regex.finditer(js):
                        path = internal_path(m.group(1))
                        if path and not path.startswith(SKIP_PREFIXES):
                            discovered_from_js.add(path)
            except Exception:
                pass
        for path in sorted(discovered_from_js - seen):
            if len(seen) >= MAX_PAGES:
                break
            seen.add(path)
            rec = {"path": path, "url": BASE + path, "status": None, "title": "", "text": "", "links": [], "github_links": [], "error": None}
            try:
                response = await page.goto(BASE + path, wait_until="domcontentloaded", timeout=30000)
                rec["status"] = response.status if response else None
                rec["title"] = await page.title()
                rec["text"] = (await page.locator("body").inner_text(timeout=10000))[:150000]
                links = await page.locator("a[href]").evaluate_all("els => els.map(a => a.href)")
                rec["links"] = sorted(set(links))
                rec["github_links"] = sorted(set(u for u in links if u.startswith("https://github.com/")))
            except Exception as e:
                rec["error"] = f"{type(e).__name__}: {e}"
            results.append(rec)
        await browser.close()

    result = {"site": BASE, "crawl_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "pages": results, "js_route_candidates": sorted(discovered_from_js)}
    Path(OUTPUT_JSON).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    repo_links = sorted(set(u for r in results for u in r["github_links"]))
    lines = ["# Daily Dev Drops — Browser crawl", "", f"Crawled: {result['crawl_timestamp']}", "", f"Visited paths: {len(results)}", f"GitHub URLs: {len(repo_links)}", "", "## Internal pages", "", "| Route | HTTP | Title | GitHub links |", "|---|---|---|---:|"]
    for r in results:
        lines.append(f"| [{markdown_safe(r['path'])}]({r['url']}) | {r['status'] or 'ERROR'} | {markdown_safe(r['title'])} | {len(r['github_links'])} |")
    lines += ["", "## All GitHub links", ""] + [f"- {u}" for u in repo_links]
    for r in results:
        lines += ["", "---", "", f"## {r['path']}", "", f"URL: {r['url']}  ", f"HTTP: {r['status']}  ", f"Error: {r['error'] or 'None'}", "", "### Content", "", "```text", r["text"].replace("```", "` ` `"), "```", "", "### External GitHub links", ""] + [f"- {u}" for u in r["github_links"]]
    Path(OUTPUT_MD).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Created {OUTPUT_MD} and {OUTPUT_JSON} with {len(results)} paths and {len(repo_links)} GitHub links")


if __name__ == "__main__":
    asyncio.run(main())
