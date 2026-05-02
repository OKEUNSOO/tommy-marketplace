---
name: application-writing
description: Use when drafting or revising Korean resume bullets, 자기소개서, 1-minute self-introductions, STAR interview answers, cover emails, or portfolio positioning from local career evidence notes and a target JD.
---

# Application Writing

Use this skill to create application materials grounded in the user's stored evidence.

## 사전 설정
이 스킬은 로컬 'career-notes/' 폴더가 필요합니다.
권장 구조: 'career-notes/{01_경험/, 02_서류/, 03_지원/}'

## Required Grounding

1. Load matched context with `career-experience-db` when a JD is present.
2. Read the relevant source notes before writing final claims.
3. Use only metrics that appear in the source notes.
4. If a claim is useful but not evidenced, mark it as `보강 필요` instead of fabricating it.

## Output Patterns

For a grounded prompt that already includes matched career evidence context, run:

```bash
python skills/application-writing/scripts/make_application_prompt.py --jd-file PATH --type resume --company "회사명" --role "직무명"
```

Available `--type` values: `resume`, `cover-letter`, `intro`, `interview`, `email`.

Read `references/output-templates.md` when you need exact structures.

Resume bullets:

```text
동사 + 분석/구현 방법 + 정량/정성 결과 + 직무 연결성
```

자기소개서:

```text
회사/직무 과제 -> 연결되는 내 경험 -> 구체적 행동 -> 결과/학습 -> 입사 후 기여
```

Interview STAR:

```text
상황 -> 과제 -> 행동 -> 결과 -> 배운 점/재현 가능성
```

## Style

- Default to Korean.
- Be specific, practical, and not overpolished.
- Avoid generic motivation paragraphs.
- Do not use inflated seniority or claims not supported by the source notes.
- Keep final interview answers conversational rather than document-like.
