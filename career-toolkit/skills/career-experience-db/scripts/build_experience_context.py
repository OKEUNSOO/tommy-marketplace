#!/usr/bin/env python3
"""Build JD-matched context from local career evidence notes."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_SOURCE_DIRS = ("01_경험", "02_서류", "03_지원")
FIRST_READ_FILES = (
    "01_경험/경험정리_인덱스.md",
    "02_서류/이력서.md",
    "02_서류/포트폴리오.md",
    "02_서류/자소서_소재.md",
)


KEYWORD_PATTERNS = [
    r"퍼[널넬]\s*분석", r"funnel",
    r"리텐션", r"retention", r"이탈[률율]", r"churn",
    r"코호트", r"cohort",
    r"KPI", r"지표\s*설계", r"metric",
    r"세그[맨먼]테이션", r"segmentation", r"RFM",
    r"A/B\s*테스트", r"A/B test",
    r"추천\s*시스템", r"recommendation",
    r"머신러닝", r"machine learning", r"ML",
    r"군집화", r"clustering",
    r"공간\s*데이터", r"geo", r"geospatial",
    r"SQL", r"python", r"tableau", r"streamlit",
    r"대시보드", r"dashboard",
    r"이커머스", r"e-commerce", r"ecommerce",
    r"마케팅\s*분석", r"marketing analytics",
    r"프로덕트\s*분석", r"product analytics",
    r"SaaS", r"플랫폼", r"platform",
    r"EdTech", r"교육", r"오누이", r"onuii",
    r"광고", r"ROI", r"ROAS", r"UTM", r"Meta",
    r"로그\s*데이터", r"사용자\s*행동",
    r"Text-to-SQL", r"LangChain", r"OpenAI",
]

TECH_TERMS = [
    "Python", "SQL", "Pandas", "NumPy", "Scikit-learn", "GeoPandas",
    "Streamlit", "Tableau", "Docker", "AWS", "EC2", "GA4", "GTM",
    "Meta Pixel", "OpenAI API", "LangChain", "n8n", "KMeans", "HDBSCAN",
    "Spectral Clustering", "A/B Test",
]


@dataclass(frozen=True)
class Note:
    path: Path
    rel_path: str
    text: str


@dataclass(frozen=True)
class EvidenceConfig:
    root: Path
    source_dirs: tuple[str, ...]


def clean_text(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text.strip())


def markdown_notes(config: EvidenceConfig) -> list[Note]:
    notes: list[Note] = []
    for directory in config.source_dirs:
        root = config.root / directory
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if any(part.startswith(".") for part in path.relative_to(config.root).parts):
                continue
            rel_path = path.relative_to(config.root).as_posix()
            notes.append(Note(path, rel_path, path.read_text(encoding="utf-8", errors="ignore")))
    return notes


def title_for(note: Note) -> str:
    match = re.search(r"^#\s+(.+)$", note.text, re.MULTILINE)
    return match.group(1).strip() if match else note.path.stem


def jd_patterns(jd_text: str) -> list[str]:
    return [pattern for pattern in KEYWORD_PATTERNS if re.search(pattern, jd_text, re.IGNORECASE)]


def jd_terms(jd_text: str) -> set[str]:
    terms = set(re.findall(r"[A-Za-z][A-Za-z0-9+.#/-]{1,}|[가-힣]{2,}", jd_text))
    stopwords = {"경험", "업무", "분석", "데이터", "있는", "위한", "통해", "관련", "지원", "직무"}
    return {term for term in terms if term not in stopwords}


def score_note(note: Note, patterns: list[str], terms: set[str]) -> int:
    text_lower = note.text.lower()
    score = 0
    for pattern in patterns:
        score += len(re.findall(pattern, note.text, re.IGNORECASE)) * 5
    for term in terms:
        score += text_lower.count(term.lower())
    if note.rel_path.startswith("01_경험/"):
        score += 8
    if note.rel_path in FIRST_READ_FILES:
        score += 12
    return score


def relevant_excerpt(note: Note, patterns: list[str], terms: set[str], limit: int = 10) -> str:
    lines = []
    for raw_line in note.text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("---"):
            continue
        matched_pattern = any(re.search(pattern, line, re.IGNORECASE) for pattern in patterns)
        matched_term = any(term.lower() in line.lower() for term in terms)
        if matched_pattern or matched_term or re.search(r"[%]|수상|달성|감소|증가|절감|개선|구축|설계", line):
            lines.append(line)
        if len(lines) >= limit:
            break
    if not lines:
        lines = [line.strip() for line in note.text.splitlines() if line.strip()][:5]
    return "\n".join(f"- {line}" for line in lines[:limit])


def matched_notes(config: EvidenceConfig, jd_text: str, limit: int = 8) -> list[tuple[int, Note]]:
    patterns = jd_patterns(jd_text)
    terms = jd_terms(jd_text)
    scored = [(score_note(note, patterns, terms), note) for note in markdown_notes(config)]
    return [(score, note) for score, note in sorted(scored, key=lambda item: item[0], reverse=True)[:limit] if score > 0]


def metrics_summary(notes: list[Note], limit: int = 14) -> str:
    metric_lines: list[str] = []
    metric_pattern = re.compile(r"(%|p\b|명|만원|시간|개|수상|달성|감소|증가|절감|개선|배포|구축)")
    for note in notes:
        for raw_line in note.text.splitlines():
            line = raw_line.strip(" -|\t")
            if len(line) < 8:
                continue
            if metric_pattern.search(line):
                metric_lines.append(f"- {title_for(note)}: {line}")
            if len(metric_lines) >= limit:
                return "\n".join(metric_lines)
    return "(정량 근거를 찾지 못함. 원본 노트 확인 필요)"


def tech_summary(notes: list[Note], jd_text: str) -> str:
    corpus = "\n".join(note.text for note in notes) + "\n" + jd_text
    found = [term for term in TECH_TERMS if re.search(re.escape(term), corpus, re.IGNORECASE)]
    return "\n".join(f"- {term}" for term in found) if found else "(JD와 노트에서 직접 감지된 기술 스택 없음)"


def full_context(config: EvidenceConfig) -> str:
    sections = []
    for rel_path in FIRST_READ_FILES:
        path = config.root / rel_path
        if path.exists():
            sections.append(f"## {rel_path}\n{path.read_text(encoding='utf-8', errors='ignore')}")
    notes = markdown_notes(config)
    experience_index = "\n".join(f"- {note.rel_path}" for note in notes if note.rel_path.startswith("01_경험/"))
    return f"""=== 지원자 전체 경험 데이터: Career Evidence ===

[Evidence Root]
{config.root}

[우선 읽을 문서]
{clean_text(chr(10).join(sections))}

[경험 노트 목록]
{experience_index}

=== 경험 데이터 끝 ==="""


def build_context(config: EvidenceConfig, jd_text: str) -> str:
    patterns = jd_patterns(jd_text)
    terms = jd_terms(jd_text)
    matches = matched_notes(config, jd_text)
    notes = [note for _, note in matches]
    keyword_text = ", ".join(patterns) or "직접 감지된 키워드 없음"
    note_sections = "\n\n".join(
        f"## {title_for(note)}\npath: {note.rel_path}\nscore: {score}\n{relevant_excerpt(note, patterns, terms)}"
        for score, note in matches
    )

    return f"""=== 지원자 경험 데이터: Career Evidence ===

[Evidence Root]
{config.root}

[JD 감지 키워드]
{keyword_text}

[매칭된 경험/서류 노트]
{note_sections if note_sections else "관련 노트 없음"}

[정량 성과 후보]
{metrics_summary(notes)}

[기술 스택 후보]
{tech_summary(notes, jd_text)}

=== 경험 데이터 끝 ==="""


def read_jd(args: argparse.Namespace) -> str:
    if args.stdin:
        return sys.stdin.read()
    if args.jd_file:
        return Path(args.jd_file).read_text(encoding="utf-8")
    if args.jd_text:
        return args.jd_text
    raise SystemExit("Provide --stdin, --jd-file, or --jd-text.")


def resolve_config(args: argparse.Namespace) -> EvidenceConfig:
    root = Path(args.evidence_root).expanduser().resolve() if args.evidence_root else Path.cwd().resolve()
    source_dirs = tuple(part.strip() for part in args.source_dirs.split(",") if part.strip())
    return EvidenceConfig(root=root, source_dirs=source_dirs or DEFAULT_SOURCE_DIRS)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build career context from local career evidence notes.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--stdin", action="store_true", help="Read JD text from stdin.")
    source.add_argument("--jd-file", help="Read JD text from a file.")
    source.add_argument("--jd-text", help="Use this JD text directly.")
    parser.add_argument("--full", action="store_true", help="Print evidence orientation context.")
    parser.add_argument("--evidence-root", default=None, help="Root directory that contains career evidence folders.")
    parser.add_argument(
        "--source-dirs",
        default=",".join(DEFAULT_SOURCE_DIRS),
        help="Comma-separated source folders under the evidence root.",
    )
    args = parser.parse_args()

    config = resolve_config(args)
    if not config.root.exists():
        raise SystemExit(f"Evidence root not found: {config.root}")

    print(full_context(config) if args.full else build_context(config, read_jd(args)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
