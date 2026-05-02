from __future__ import annotations

import re
from typing import Any

from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    if not text:
        return ""
    normalized = text.replace("\xa0", " ")
    normalized = normalized.replace("\r\n", "\n").replace("\r", "\n")
    normalized = re.sub(r"[ \t]+\n", "\n", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def html_to_text(value: Any) -> str:
    if value is None:
        return ""
    text = BeautifulSoup(str(value), "html.parser").get_text("\n", strip=True)
    return clean_text(text)


def safe_markdown_label(value: str, fallback: str = "채용 공고") -> str:
    label = clean_text(value) or fallback
    return label.replace("[", "(").replace("]", ")")
