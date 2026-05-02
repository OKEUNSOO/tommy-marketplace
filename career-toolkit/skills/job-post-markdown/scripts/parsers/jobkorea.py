from __future__ import annotations

from typing import Any

from .browser import close_context, open_context, safe_text
from .dynamic import result, section


def build(url: str) -> dict[str, Any]:
    playwright, browser, context = open_context(headless=True)
    try:
        page = context.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2500)

        company = (
            safe_text(page, "a[href*='/company/']")
            or safe_text(page, ".coName")
            or safe_text(page, ".corp-name")
        )
        title = safe_text(page, "h1") or safe_text(page, ".tit_job") or page.title()

        body_parts: list[str] = []
        summary = safe_text(page, ".tbList, .artReadJobSum, .recruit-summary")
        if summary:
            body_parts.append(section("공고 요약", summary))

        for selector in [
            "#GI_Read_Comt_Ifrm",
            ".artReadJobDetail",
            ".tbRow",
            ".job-detail",
            "main",
            "body",
        ]:
            text = safe_text(page, selector)
            if text and len(text) > 300:
                body_parts.append(text)
                break

        return result(url, title, company, body_parts)
    finally:
        close_context(playwright, browser, context)
