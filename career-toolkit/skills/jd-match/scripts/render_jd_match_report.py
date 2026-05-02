#!/usr/bin/env python3
"""Render a deterministic JD match report scaffold from JD text."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
CONTEXT_SCRIPT = PROJECT_ROOT / "skills" / "career-experience-db" / "scripts" / "build_experience_context.py"


def read_jd(args: argparse.Namespace) -> str:
    if args.stdin:
        return sys.stdin.read()
    if args.jd_file:
        return Path(args.jd_file).read_text(encoding="utf-8")
    if args.jd_text:
        return args.jd_text
    raise SystemExit("Provide --stdin, --jd-file, or --jd-text.")


def build_context(jd_text: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(CONTEXT_SCRIPT), "--jd-text", jd_text],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a JD match report scaffold.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--stdin", action="store_true")
    source.add_argument("--jd-file")
    source.add_argument("--jd-text")
    parser.add_argument("--company", default="확인 필요")
    parser.add_argument("--role", default="확인 필요")
    args = parser.parse_args()

    jd_text = read_jd(args)
    context = build_context(jd_text)

    print(f"""# JD Match Report

## 대상
- 회사: {args.company}
- 직무: {args.role}

## 적합도 요약
- 핵심 적합 근거: 보강 필요
- 가장 강한 경험: 보강 필요
- 주요 리스크: 보강 필요

## 커리어 근거 매칭 근거
{context}

## 이력서에 앞세울 문장
- 보강 필요: JD 요구사항과 가장 직접 연결되는 프로젝트 ID를 선택해 작성

## 부족하거나 위험한 부분
- 보강 필요: JD 필수요건 중 제공된 근거 노트에 없는 항목을 명시

## 보강 질문
- 이 공고에서 반드시 강조하고 싶은 프로젝트는 무엇인가?
- 정량 성과의 원천 자료나 검증 근거가 있는가?
- 필수 자격 중 실제 경험이 약한 항목은 무엇인가?
""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
