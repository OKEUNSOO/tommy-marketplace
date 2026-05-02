#!/usr/bin/env python3
"""Create a grounded prompt for resume, 자기소개서, intro, or interview output."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
CONTEXT_SCRIPT = PROJECT_ROOT / "skills" / "career-experience-db" / "scripts" / "build_experience_context.py"


OUTPUT_GUIDES = {
    "resume": "이력서 bullet을 action + method + result 구조로 작성하세요.",
    "cover-letter": "자기소개서를 회사/직무 과제 -> 내 경험 -> 행동 -> 결과 -> 기여 구조로 작성하세요.",
    "intro": "1분 자기소개를 현재 포지셔닝 -> 대표 경험 -> 직무 연결 순서로 작성하세요.",
    "interview": "STAR 면접 답변을 상황 -> 과제 -> 행동 -> 결과 -> 배운 점 순서로 작성하세요.",
    "email": "지원/문의 이메일 초안을 간결하게 작성하세요.",
}


def read_jd(args: argparse.Namespace) -> str:
    if args.stdin:
        return sys.stdin.read()
    if args.jd_file:
        return Path(args.jd_file).read_text(encoding="utf-8")
    if args.jd_text:
        return args.jd_text
    return ""


def build_context(jd_text: str) -> str:
    if not jd_text:
        completed = subprocess.run(
            [sys.executable, str(CONTEXT_SCRIPT), "--jd-text", "데이터 분석 Product Analytics BI KPI SQL Python"],
            check=True,
            capture_output=True,
            text=True,
        )
    else:
        completed = subprocess.run(
            [sys.executable, str(CONTEXT_SCRIPT), "--jd-text", jd_text],
            check=True,
            capture_output=True,
            text=True,
        )
    return completed.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a grounded application-writing prompt.")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--stdin", action="store_true")
    source.add_argument("--jd-file")
    source.add_argument("--jd-text")
    parser.add_argument("--type", choices=sorted(OUTPUT_GUIDES), default="resume")
    parser.add_argument("--company", default="확인 필요")
    parser.add_argument("--role", default="확인 필요")
    args = parser.parse_args()

    jd_text = read_jd(args)
    context = build_context(jd_text)

    print(f"""당신은 지원자의 실제 경험만 사용해 커리어 문서를 작성하는 편집자입니다.

[작성 대상]
- 회사: {args.company}
- 직무: {args.role}
- 산출물: {args.type}

[작성 지시]
{OUTPUT_GUIDES[args.type]}

[근거 규칙]
- 제공된 근거 노트에 없는 프로젝트, 기간, 수치, 기여도는 만들지 마세요.
- 근거가 부족한 주장은 `보강 필요`로 표시하세요.
- 한국어로 구체적이고 실무적인 문장으로 작성하세요.
- 과장된 경력자 표현을 피하고 신입/주니어 맥락을 유지하세요.

[커리어 근거 매칭 컨텍스트]
{context}

[JD 원문]
{jd_text if jd_text else "JD 없음"}
""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
