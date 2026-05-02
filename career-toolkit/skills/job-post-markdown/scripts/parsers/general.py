from __future__ import annotations

from typing import Any

import requests
from bs4 import BeautifulSoup

from .common import clean_text, safe_markdown_label


NOISE_TAGS = ["nav", "header", "footer", "script", "style", "iframe", "noscript", "svg"]


def extract_content(soup: BeautifulSoup) -> tuple[str, str]:
    for tag in NOISE_TAGS:
        for node in soup.find_all(tag):
            node.decompose()

    title = clean_text(soup.title.get_text(" ", strip=True) if soup.title else "")
    candidates = []
    for selector in ["article", "main", "#content", ".content", ".post-content", "body"]:
        found = soup.select_one(selector)
        if found:
            text = clean_text(found.get_text("\n", strip=True))
            if text:
                candidates.append((selector, text))

    if not candidates:
        return title, ""

    candidates.sort(key=lambda item: len(item[1]), reverse=True)
    return title, candidates[0][1]


def build(url: str) -> dict[str, Any]:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title, content = extract_content(soup)

    safe_title = safe_markdown_label(title, "채용 공고")
    common_info = f"### [{safe_title}]({url})\n\n---\n"
    body = content or "상세 내용을 추출하지 못했습니다. 원문 페이지 확인이 필요합니다."
    markdown = f"{common_info}\n### {safe_title}\n{body}"
    positions = [{"name": safe_title, "content": body}]

    return {
        "raw": markdown,
        "refined": markdown,
        "common_info": common_info,
        "refined_common_info": common_info,
        "positions": positions,
        "strategy_info": "",
        "title": safe_title,
    }
