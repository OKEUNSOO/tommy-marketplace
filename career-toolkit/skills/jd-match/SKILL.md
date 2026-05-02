---
name: jd-match
description: Use when matching a job description or fetched job-post Markdown against local career evidence notes to produce fit analysis, project recommendations, gap analysis, or application strategy.
---

# JD Match

Use this skill after a JD is available as pasted text or Markdown from `job-post-markdown`.

## 사전 설정
이 스킬은 로컬 'career-notes/' 폴더가 필요합니다.
권장 구조: 'career-notes/{01_경험/, 02_서류/, 03_지원/}'

## Inputs

- JD Markdown or raw JD text
- Experience context from `career-experience-db`
- Optional target role, seniority, or company preference from the user

## Workflow

1. If the input is a URL, first use `job-post-markdown`.
2. Build matched experience context:

   ```bash
   python skills/career-experience-db/scripts/build_experience_context.py --jd-file PATH
   ```

3. For a deterministic report scaffold, run:

   ```bash
   python skills/jd-match/scripts/render_jd_match_report.py --jd-file PATH --company "회사명" --role "직무명"
   ```

4. Compare the JD against:
   - responsibilities and must-have qualifications
   - preferred qualifications
   - tools and domain keywords
   - company mission or product context
5. Produce:
   - `적합도 요약`
   - `강하게 연결되는 경험`
   - `이력서에 앞세울 문장`
   - `부족하거나 위험한 부분`
   - `보강 질문`

## Evidence Standard

- Cite project IDs such as `P001` when possible.
- Use only claims present in the source career notes.
- Mark missing evidence as `보강 필요`.
- Keep conclusions conservative when contribution, period, metric, or source is unclear.
