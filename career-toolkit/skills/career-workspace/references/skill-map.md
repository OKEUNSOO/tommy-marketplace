# Career Skill Map

This project-local skill set turns local career evidence notes into reusable Codex workflows.

| Skill | Covers | Local implementation |
| --- | --- | --- |
| `job-post-markdown` | URL -> raw/refined JD Markdown | `skills/job-post-markdown/scripts/fetch_job_markdown.py`, `skills/job-post-markdown/scripts/parsers/*.py` |
| `career-experience-db` | Career evidence reading, audit, JD-matched context | `skills/career-experience-db/scripts/build_experience_context.py`, `{01_경험,02_서류,03_지원}/*.md` |
| `jd-match` | JD fit, relevant projects, gap analysis, strategy inputs | `skills/jd-match/scripts/render_jd_match_report.py` |
| `application-writing` | Resume bullets, 자기소개서, 1-minute intro, STAR interview answers, email drafts | `skills/application-writing/scripts/make_application_prompt.py`, `skills/application-writing/references/output-templates.md` |
| `company-research` | Company/application strategy and 지원동기 research | `skills/company-research/scripts/make_company_strategy_prompt.py`, `skills/company-research/references/research-frame.md` |
| `career-workspace` | Top-level routing and workspace orientation | `README.md`, this skill map |

Execution-heavy functionality should be exposed through `scripts/` when it needs deterministic local code. Text-generation workflows stay in `SKILL.md` unless they need a stable CLI wrapper around an existing module.

## Remaining App Dependencies

These skill functions are now self-contained:

- Career evidence matched context: `skills/career-experience-db/scripts/build_experience_context.py`
- JD report scaffold: `skills/jd-match/scripts/render_jd_match_report.py`
- application prompt creation: `skills/application-writing/scripts/make_application_prompt.py`
- company strategy prompt creation: `skills/company-research/scripts/make_company_strategy_prompt.py`

The career context script reads local evidence notes directly and does not depend on an app backend.

The URL -> Markdown skill is now standalone for:

- Samsung Careers API postings
- Generic HTML pages

Specialized skill-local parsers now exist for `jumpit`, `groupby`, `rallit`, `zighang`, `wanted`, `jobkorea`, `jasoseol`, `saramin`, and `samsungcareers`. They do not call app-level Gemini refinement. Formatting is handled by Codex through `skills/job-post-markdown/references/formatting-rules.md`.
