#!/usr/bin/env python3
"""Create a company strategy prompt from JD and career evidence context."""

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


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a company strategy prompt.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--stdin", action="store_true")
    source.add_argument("--jd-file")
    source.add_argument("--jd-text")
    parser.add_argument("--company", required=True)
    parser.add_argument("--role", default="확인 필요")
    args = parser.parse_args()

    jd_text = read_jd(args)
    context = subprocess.run(
        [sys.executable, str(CONTEXT_SCRIPT), "--jd-text", jd_text],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    print(f"""다음 회사/직무에 대한 지원 전략을 작성하세요.

[대상]
- 회사: {args.company}
- 직무: {args.role}

[작성 섹션]
1. 기업이 해결하는 문제
2. 직무가 맡을 가능성이 높은 과제
3. 내 경험과 연결되는 지점
4. 지원동기 소재
5. 면접 예상 질문
6. 확인 필요 자료

[주의]
- 최신 뉴스, 재무, 대표자 정보는 JD에 없으면 `확인 필요`로 표시하세요.
- 제공된 근거 노트에 없는 경험은 만들지 마세요.
- KPI나 비즈니스 모델 추정은 `추정`이라고 표시하세요.

[커리어 근거 매칭 컨텍스트]
{context}

[JD 원문]
{jd_text}
""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
