---
name: career-experience-db
description: Use when reading, auditing, cleaning, or expanding local career evidence notes, or when converting a JD into matched applicant context.
---

# Career Experience DB

Use this skill to read local career evidence notes as the source of truth for application materials.

## 사전 설정
이 스킬은 로컬 'career-notes/' 폴더가 필요합니다.
권장 구조: 'career-notes/{01_경험/, 02_서류/, 03_지원/}'

## Source Files

Read only what the task needs:

- `01_경험/`: project and work experience notes
- `01_경험/경험정리_인덱스.md`: experience index, when present
- `02_서류/`: resume, portfolio, 자기소개서 source material, when present
- `03_지원/`: company-specific application packages and JD notes, when present

## JD Context Script

When a JD text or Markdown is available and the user wants matching context, run:

```bash
python skills/career-experience-db/scripts/build_experience_context.py --jd-file PATH
```

Run it from the evidence root by default. If the evidence root is elsewhere:

```bash
python skills/career-experience-db/scripts/build_experience_context.py --jd-file PATH --evidence-root /path/to/career-notes
```

For pasted JD text:

```bash
printf '%s' "JD text" | python skills/career-experience-db/scripts/build_experience_context.py --stdin
```

## Rules

- Do not invent projects, periods, metrics, tools, or contribution levels.
- If evidence is missing, write `보강 필요` and name the missing field.
- When adding or correcting evidence, update the relevant source note first.
- Keep the user's positioning centered on data analysis, Product Analytics, BI/KPI, and ML-assisted analysis.
- For audits, list missing fields and suggested edits before rewriting large sections.
