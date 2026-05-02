from __future__ import annotations

from datetime import datetime
from typing import Any
from urllib.parse import parse_qs, urlparse

import requests

from .common import clean_text, html_to_text, safe_markdown_label


def pick_lang(item: dict[str, Any], kr_key: str, en_key: str = "") -> str:
    kr_value = html_to_text(item.get(kr_key, ""))
    if kr_value:
        return kr_value
    if en_key:
        return html_to_text(item.get(en_key, ""))
    return ""


def fmt_datetime(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    try:
        if len(raw) >= 12:
            return datetime.strptime(raw[:12], "%Y%m%d%H%M").strftime("%Y.%m.%d %H:%M")
        if len(raw) >= 8:
            return datetime.strptime(raw[:8], "%Y%m%d").strftime("%Y.%m.%d")
    except ValueError:
        return raw
    return raw


def extract_seqno(url: str) -> str:
    parsed = urlparse(url)
    return str(parse_qs(parsed.query).get("no", [""])[0]).strip()


def build_section(title: str, body: str) -> str:
    clean_body = clean_text(body)
    if not clean_body:
        return ""
    return f"#### {title}\n{clean_body}"


def build_position(item: dict[str, Any]) -> dict[str, str]:
    name = pick_lang(item, "titleKr", "titleEn") or "모집 직무"
    blocks: list[str] = []

    for section_title, key_kr, key_en in [
        ("수행업무", "taskKr", "taskEn"),
        ("지원자격", "qlfctKr", "qlfctEn"),
        ("우대사항", "favorKr", "favorEn"),
        ("직무소개", "explnKr", "explnEn"),
        ("참고사항", "memoKr", "memoEn"),
        ("근무지역", "workPlaceKr", "workPlaceEn"),
    ]:
        section = build_section(section_title, pick_lang(item, key_kr, key_en))
        if section:
            blocks.append(section)

    content = "\n\n".join(blocks).strip() or "- 상세 내용은 채용 홈페이지를 참조하세요."
    return {"name": clean_text(name), "content": content}


def build_common_info(url: str, result: dict[str, Any], add_files: list[dict[str, Any]]) -> str:
    title = safe_markdown_label(str(result.get("title", "") or "SAMSUNG CAREERS"))
    header = f"### [{title}]({url})\n\n---\n"

    meta_lines: list[str] = []
    company = clean_text(str(result.get("cmpNameKr", "") or result.get("cmpNameEn", "") or ""))
    period_start = fmt_datetime(str(result.get("startdate", "") or ""))
    period_end = fmt_datetime(str(result.get("enddate", "") or ""))
    deadline = clean_text(str(result.get("dd", "") or ""))
    email = clean_text(str(result.get("email", "") or ""))
    phone = clean_text(str(result.get("mainTel", "") or ""))
    site_url = clean_text(str(result.get("siteUrl", "") or ""))

    if company:
        meta_lines.append(f"- 회사: {company}")
    if period_start or period_end:
        meta_lines.append(f"- 공고기간: {period_start} ~ {period_end}".strip())
    if deadline:
        meta_lines.append(f"- 마감: D-{deadline}")
    if email:
        meta_lines.append(f"- 문의: {email}")
    if phone:
        meta_lines.append(f"- 연락처: {phone}")
    if site_url:
        meta_lines.append(f"- 기업 사이트: {site_url}")

    sections: list[str] = []
    if meta_lines:
        sections.append("#### 기본 정보\n" + "\n".join(meta_lines))

    for section_title, key_kr, key_en in [
        ("회사 소개", "introKr", "introEn"),
        ("공통지원자격", "qlfctKr", "qlfctEn"),
        ("채용절차", "stepKr", "stepEn"),
        ("지원 안내", "processKr", "processEn"),
        ("제출서류", "docInfoKr", "docInfoEn"),
        ("기타 사항", "etcKr", "etcEn"),
    ]:
        section = build_section(section_title, pick_lang(result, key_kr, key_en))
        if section:
            sections.append(section)

    file_lines = []
    for file_info in add_files:
        label = clean_text(
            str(
                file_info.get("titleKr")
                or file_info.get("titleEn")
                or file_info.get("fileOriginalName")
                or file_info.get("fileName")
                or ""
            )
        )
        if label:
            file_lines.append(f"- {label}")
    if file_lines:
        sections.append("#### 첨부자료\n" + "\n".join(file_lines))

    return header if not sections else f"{header}\n" + "\n\n".join(sections).strip() + "\n"


def build_markdown(common_info: str, positions: list[dict[str, str]]) -> str:
    body: list[str] = []
    for position in positions:
        name = safe_markdown_label(str(position.get("name", "") or "모집 직무"), "모집 직무")
        content = clean_text(str(position.get("content", "") or ""))
        body.append(f"### {name}")
        body.append(content or "- 상세 내용은 채용 홈페이지를 참조하세요.")
        body.append("")
    return common_info if not body else f"{common_info}\n" + "\n".join(body).strip()


def build(url: str) -> dict[str, Any]:
    seqno = extract_seqno(url)
    if not seqno:
        return {"error": "삼성 채용 URL에서 공고 번호(no)를 찾지 못했습니다."}

    api_url = f"https://www.samsungcareers.com/recruit/detail.data?seqno={seqno}&strCode="
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Referer": url,
    }

    response = requests.get(api_url, headers=headers, timeout=20)
    response.raise_for_status()
    payload = response.json()
    if not payload.get("success"):
        return {"error": f"삼성 채용 상세 데이터 조회 실패: {payload.get('message') or 'API 실패'}"}

    data = payload.get("data") or {}
    result = data.get("result") or payload.get("result") or {}
    items = data.get("items") or payload.get("list") or []
    add_files = data.get("addFiles") or []

    positions = [build_position(item) for item in items if isinstance(item, dict)]
    title = safe_markdown_label(str(result.get("title", "") or "SAMSUNG CAREERS"))
    common_info = build_common_info(url, result, add_files)
    markdown = build_markdown(common_info, positions)

    return {
        "raw": markdown,
        "refined": markdown,
        "common_info": common_info,
        "refined_common_info": common_info,
        "positions": positions,
        "strategy_info": "",
        "title": title,
    }
