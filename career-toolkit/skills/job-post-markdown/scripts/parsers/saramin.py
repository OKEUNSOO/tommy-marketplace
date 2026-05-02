from __future__ import annotations

from typing import Any

import requests
from bs4 import BeautifulSoup

from .browser import close_context, open_context, safe_text
from .common import clean_text
from .dynamic import result, section


def build_from_html(url: str) -> dict[str, Any]:
    response = requests.get(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
        },
        timeout=20,
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    company_node = soup.select_one("a.company, .company_name, .corp_name")
    title_node = soup.select_one(".tit_job, h1")
    company = clean_text(company_node.get_text(" ", strip=True) if company_node else "")
    title = clean_text(title_node.get_text(" ", strip=True) if title_node else soup.title.get_text(" ", strip=True) if soup.title else "")

    body_parts: list[str] = []
    summary_node = soup.select_one(".jv_cont.jv_summary, .jv_header")
    if summary_node:
        body_parts.append(section("공고 요약", summary_node.get_text("\n", strip=True)))

    content_node = soup.select_one("#iframe_content_0, .user_content, .job-content, .jv_cont.jv_detail")
    if not content_node:
        # Many Saramin postings inline the full content later in the page.
        content_node = soup.select_one("body")
    body_parts.append(section("본문", content_node.get_text("\n", strip=True) if content_node else ""))
    return result(url, title, company, body_parts)


def build(url: str) -> dict[str, Any]:
    try:
        html_result = build_from_html(url)
        content = html_result.get("refined", "")
        if isinstance(content, str) and len(content) > 500:
            return html_result
    except Exception:
        pass

    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2500)

        company = safe_text(page, "a.company") or safe_text(page, ".company_name") or safe_text(page, ".corp_name")
        title = safe_text(page, ".tit_job") or safe_text(page, "h1") or page.title()

        body_parts: list[str] = []
        summary = safe_text(page, ".jv_cont.jv_summary, .jv_header")
        if summary:
            body_parts.append(section("공고 요약", summary))

        content = ""
        try:
            iframe_body = page.frame_locator("#iframe_content_0").locator("body")
            iframe_body.wait_for(timeout=3000)
            content = iframe_body.inner_text().strip()
        except Exception:
            pass
        if not content:
            for selector in [".user_content", ".job-content", ".jv_cont.jv_detail", "main", "body"]:
                text = safe_text(page, selector)
                if text and len(text) > len(content):
                    content = text
        body_parts.append(section("본문", content))

        return result(url, title, company, body_parts)
    finally:
        close_context(playwright, browser, context)
