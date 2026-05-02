from __future__ import annotations

from typing import Any

from bs4 import BeautifulSoup

from .browser import all_texts, close_context, open_context, safe_text
from .common import clean_text, html_to_text, safe_markdown_label


def section(title: str, body: str) -> str:
    clean_body = clean_text(body)
    return f"#### {title}\n{clean_body}" if clean_body else ""


def result(url: str, title: str, company: str, body_parts: list[str]) -> dict[str, Any]:
    safe_title = safe_markdown_label(title, "채용 공고")
    safe_company = clean_text(company)
    label = f"{safe_company} | {safe_title}" if safe_company else safe_title
    common_info = f"### [{label}]({url})\n\n---\n"
    body = "\n\n".join(part for part in body_parts if clean_text(part)).strip()
    if not body:
        body = "상세 내용을 추출하지 못했습니다. 원문 페이지 확인이 필요합니다."
    markdown = f"{common_info}\n{body}"
    return {
        "raw": markdown,
        "refined": markdown,
        "common_info": common_info,
        "refined_common_info": common_info,
        "positions": [{"name": safe_title, "content": body}],
        "strategy_info": "",
        "title": f"({safe_company}) {safe_title}" if safe_company else safe_title,
    }


def body_text_page(url: str, wait_ms: int = 2500) -> tuple[str, str]:
    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(wait_ms)
        return page.title(), page.locator("body").inner_text().strip()
    finally:
        close_context(playwright, browser, context)


def build_jumpit(url: str) -> dict[str, Any]:
    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2500)
        try:
            page.keyboard.press("End")
            page.wait_for_timeout(800)
            page.keyboard.press("Home")
            page.wait_for_timeout(800)
        except Exception:
            pass
        try:
            button = page.locator("button:has-text('더보기'), button:has-text('더 보기')").first
            if button.count() > 0 and button.is_visible():
                button.click()
                page.wait_for_timeout(500)
        except Exception:
            pass

        company = safe_text(page, ".name")
        title = safe_text(page, "h1")
        body_parts: list[str] = []
        if tech := " / ".join(all_texts(page, "[class*='tech'], [class*='stack']")):
            body_parts.append(section("기술스택", tech))
        try:
            html = page.locator("[class*='position_info']").first.inner_html()
            soup = BeautifulSoup(html, "html.parser")
            for dl in soup.find_all("dl"):
                dt = dl.find("dt")
                dd = dl.find("dd")
                if dt and dd:
                    body_parts.append(section(dt.get_text(" ", strip=True), dd.get_text("\n", strip=True)))
        except Exception:
            body_parts.append(section("본문", page.locator("body").inner_text()))
        return result(url, title, company, body_parts)
    finally:
        close_context(playwright, browser, context)


def build_rallit(url: str) -> dict[str, Any]:
    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2000)
        company = safe_text(page, "a[href*='/companies/']") or safe_text(page, "h2")
        title = safe_text(page, "h1")
        body_parts: list[str] = []
        extras = " | ".join(all_texts(page, ".css-1385rv7"))
        if extras:
            body_parts.append(section("부가 정보", extras))
        main_texts = all_texts(page, ".css-1xr2pwg")
        if main_texts:
            body_parts.extend(main_texts)
        else:
            body_parts.append(section("본문", page.locator("body").inner_text()))
        return result(url, title, company, body_parts)
    finally:
        close_context(playwright, browser, context)


def build_zighang(url: str) -> dict[str, Any]:
    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2500)
        company = safe_text(page, "[class*='underline']")
        title = safe_text(page, "[class*='typo-heading'], h1")
        body_parts: list[str] = []
        summary = safe_text(page, ".bg-subtle.grid")
        if summary:
            body_parts.append(section("공고 요약", summary))
        html = ""
        try:
            html = page.locator(".tiptap.ProseMirror").first.inner_html()
        except Exception:
            pass
        if html:
            body_parts.append(html_to_text(html))
        else:
            body_parts.append(section("본문", page.locator("body").inner_text()))
        return result(url, title, company, body_parts)
    finally:
        close_context(playwright, browser, context)


def build_wanted(url: str) -> dict[str, Any]:
    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)
        try:
            button = page.locator('button:has-text("상세 정보 더 보기")').first
            if button.count() > 0 and button.is_visible():
                button.click()
                page.wait_for_timeout(800)
        except Exception:
            pass
        company = safe_text(page, "[class*='Company__Link'], a[href*='/company/']")
        title = safe_text(page, "h1") or safe_text(page, "[class*='wds-58fmok']")
        body_parts: list[str] = []
        description = safe_text(page, "[class*='JobDescription'], section")
        if description:
            body_parts.append(description)
        for label, selector in [
            ("마감일", "[class*='JobDueTime']"),
            ("근무지역", "[class*='JobWorkPlace']"),
            ("태그", "[class*='CompanyTags']"),
        ]:
            text = safe_text(page, selector)
            if text:
                body_parts.append(section(label, text))
        if not body_parts:
            body_parts.append(section("본문", page.locator("body").inner_text()))
        return result(url, title, company, body_parts)
    finally:
        close_context(playwright, browser, context)


def build_groupby(url: str) -> dict[str, Any]:
    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)
        try:
            page.keyboard.press("End")
            page.wait_for_timeout(700)
            page.keyboard.press("Home")
        except Exception:
            pass
        company = safe_text(page, 'xpath=//*[@id="main"]/div[2]/a/div/div/div[1]/div[2]/div/span[1]')
        title = safe_text(page, 'xpath=//*[@id="main"]/div[2]/div[1]/div/div[1]//span') or safe_text(page, "h1")
        body_parts = []
        meta = safe_text(page, 'xpath=//*[@id="main"]/div[2]/div[1]/div/div[1]/div[2]')
        if meta:
            body_parts.append(section("공고 요약", meta))
        content = safe_text(page, 'xpath=//*[@id="main"]/div[2]/div[1]/div/div[2]')
        if content:
            body_parts.append(content)
        else:
            body_parts.append(section("본문", page.locator("body").inner_text()))
        return result(url, title, company, body_parts)
    finally:
        close_context(playwright, browser, context)


def build_jasoseol(url: str) -> dict[str, Any]:
    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            page.wait_for_load_state("networkidle", timeout=10000)
        except Exception:
            page.wait_for_timeout(2500)
        title = page.title().replace(" - 자소설닷컴", "").strip()
        body = ""
        for selector in [".recruit-content", ".employment-notice-content", "div[class*='recruit']", "main", "body"]:
            text = safe_text(page, selector)
            if len(text) > len(body):
                body = text
        return result(url, title, "자소설닷컴", [section("본문", body)])
    finally:
        close_context(playwright, browser, context)


def build_browser_generic(url: str) -> dict[str, Any]:
    title, body = body_text_page(url)
    return result(url, title, "", [section("본문", body)])
