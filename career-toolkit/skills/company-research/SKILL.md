---
name: company-research
description: Use when researching a company for an application, connecting company strategy to a JD, or preparing 지원동기, 면접 준비, or company-specific application positioning in this project.
---

# Company Research

Use this skill to turn company information and a JD into application strategy.

## 사전 설정
이 스킬은 로컬 'career-notes/' 폴더가 필요합니다.
권장 구조: 'career-notes/{01_경험/, 02_서류/, 03_지원/}'

## Local Sources

- JD Markdown from `job-post-markdown`
- Experience context from `career-experience-db`
- `references/research-frame.md`: offline company research and application strategy frame

## Workflow

1. If the company comes from a URL, fetch the JD first with `job-post-markdown`.
2. Extract company name, product/service, role, responsibilities, and requirements from the JD.
3. Use `references/research-frame.md` for the analysis frame.
4. If live research is not required, generate a grounded strategy prompt:

   ```bash
   python skills/company-research/scripts/make_company_strategy_prompt.py --jd-file PATH --company "회사명" --role "직무명"
   ```

5. If API keys are available and the user wants live research, use current browsing tools. Otherwise, work from the provided JD and local company notes.
6. Connect research to local career evidence:
   - what the company likely needs
   - which user projects are relevant
   - which metrics or skills prove fit
   - what gaps should be handled honestly

Read `references/research-frame.md` for the offline research structure.

## Output

- `기업이 해결하는 문제`
- `직무가 맡을 가능성이 높은 과제`
- `내 경험과 연결되는 지점`
- `지원동기 소재`
- `면접 예상 질문`
- `확인 필요 자료`

Do not invent recent news, financials, or leadership facts. Browse or mark `확인 필요`.
