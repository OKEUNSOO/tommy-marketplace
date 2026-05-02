# Job Post Formatting Rules

Use these rules after `scripts/fetch_job_markdown.py` returns raw or directly extracted Markdown. These replace the old app-level Gemini refinement step.

## Non-Negotiable Rules

- Preserve the top title link exactly when it is valid:
  `### [회사 | 직무](URL)` or `### [직무](URL)`.
- Do not invent, summarize away, or delete job-posting facts.
- Keep all dates, numbers, locations, salary ranges, URLs, tools, qualifications, deadlines, and hiring process details.
- If extracted text is noisy, remove navigation/footer/login/search noise only when it is clearly unrelated to the posting.
- If a field is missing, write `확인 필요` only in structured summaries. Do not fabricate.

## Markdown Style

- Use `####` for sections inside a posting.
- Use `- ` for bullets.
- Convert `~` ranges to `-` to avoid Markdown strikethrough, e.g. `1-3년`.
- Keep one blank line between sections.
- Convert bare URLs in body text to Markdown links when useful, but never remove the URL.
- Avoid emoji in refined output unless it appears in the original title or the user asks to keep it.

## Preferred Section Order

When the posting contains enough information, organize sections in this order:

1. `#### 공고 요약`
2. `#### 회사/서비스 소개`
3. `#### 주요 업무`
4. `#### 자격 요건`
5. `#### 우대 사항`
6. `#### 기술 스택`
7. `#### 혜택 및 복지`
8. `#### 채용 절차`
9. `#### 근무 조건`
10. `#### 참고 사항`

Do not add empty sections.

## Site Hints

### Jumpit

- Preserve all original technical requirements.
- Turn long paragraphs into bullets only when it improves readability.
- Keep the title link unchanged.

### GroupBy

- Keep company context as prose when it explains problem, product, or culture.
- Put actual requirements and responsibilities into bullets.
- Prefer a report-like structure, but do not shorten the posting.

### Rallit, Wanted, Zighang, Jasoseol

- Preserve all details.
- Remove repeated URL fragments and encoding artifacts if they leaked into the body.
- Standardize section headings with `####`.
- Convert `ㆍ`, `•`, and duplicated bullet symbols into `- `.

### Saramin and JobKorea

- Remove obvious portal UI noise such as login, search, footer, unrelated recommendations, map copyright, or repeated navigation.
- Keep application deadline, location, employment type, career level, education, and process when present.
