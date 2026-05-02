---
name: job-post-markdown
description: Use when the user provides a job posting URL and wants the posting fetched, parsed, converted to Markdown, or prepared as JD input for matching, resumes, 자기소개서, interview prep, or company research in this project.
---

# Job Post Markdown

Use this skill to turn a job posting URL into reusable Markdown using skill-local Python parsers.

## 사전 설정
이 스킬은 로컬 'career-notes/' 폴더가 필요합니다.
권장 구조: 'career-notes/{01_경험/, 02_서류/, 03_지원/}'

## Scope

Work inside the current project or installed skill directory.

Core implementation:

- Router: `scripts/fetch_job_markdown.py`
- Skill-local parsers: `scripts/parsers/*.py`

## Workflow

1. If the user provides a URL, run:

   ```bash
   python skills/job-post-markdown/scripts/fetch_job_markdown.py "URL"
   ```

2. Use `refined` Markdown for downstream analysis unless the user explicitly asks for screen-display HTML.
3. If the output is noisy or the user asks for cleaned Markdown, refine it using `references/formatting-rules.md`.
4. If multiple positions are returned, ask the user which position to use unless the request clearly covers all positions.
5. Save fetched JD Markdown only when the user asks. Prefer returning the result in the chat for one-off analysis.
6. If fetching fails because a site blocks automation, report the failure and ask for pasted JD text or a screenshot.

## Output Rules

- Preserve the original job posting URL in the header.
- Keep company, title, job requirements, responsibilities, qualifications, preferred qualifications, process, deadline, location, and benefits when available.
- Do not invent missing fields. Mark them as `확인 필요` only if the user needs a structured table.
- For follow-up JD matching, pass the Markdown to the `career-experience-db` or `jd-match` skill.
- Formatting/refinement is done by Codex using `references/formatting-rules.md`, not by a Gemini API call inside Python.

## Environment

The project-local test environment is `.venv/`. If it is missing, create it and install requirements:

```bash
python3 -m venv .venv
python -m pip install requests beautifulsoup4
```

The script is standalone and should not import an app backend.

## Supported Sites

Read `references/supported-sites.md` when you need site-specific behavior or parser ownership.
