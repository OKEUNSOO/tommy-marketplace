---
name: career-workspace
description: Use when organizing or using a local career workspace with career evidence notes, including evidence cleanup, resume bullets, Korean 자기소개서 drafts, STAR interview answers, JD matching, company research framing, portfolio project positioning, and local skills improvement work.
---

# Career Workspace

Use this skill to turn the local career materials into job-search outputs grounded in real experience. Prefer Korean output unless requested otherwise.

## Workspace

Default workspace root:

```text
career-notes/
```

Read the root `README.md` first when orienting. If it is missing or stale, inspect the folder and update it before doing larger organization work.

## Workflow

1. Identify the task type and use the narrower project-local skill when applicable.
   - URL to Markdown: use `job-post-markdown`.
   - Career evidence context, cleanup, or audit: use `career-experience-db`.
   - JD fit, project matching, or gap analysis: use `jd-match`.
   - Resume, 자기소개서, 1-minute intro, interview answers, or email: use `application-writing`.
   - Company research and 지원동기 strategy: use `company-research`.

2. If no narrower skill covers the task, continue with this workspace-level workflow.
   - Experience cleanup: update or audit the relevant source note.
   - Resume or portfolio: extract projects from career evidence notes and rewrite into role-fit bullets.
   - 자기소개서 or 면접: use stored project notes, resume/portfolio drafts, and numeric evidence.
   - JD matching: compare the job posting against career evidence notes, prior application folders, and portfolio material.
   - Company strategy: use `skills/company-research/references/research-frame.md` as the research/playbook frame.
   - Tool/code work: follow the existing Python structure in `skills/`.

3. Load only the needed references.
   - Folder orientation: `references/folder-map.md`.
   - Skill/module routing: `references/skill-map.md`.
   - Career evidence writing rules: `references/experience-db-guide.md`.
   - Application output workflow: `references/application-workflow.md`.

4. Ground every output in stored evidence.
   - Prefer source career notes over invented claims.
   - Mark missing proof as `보강 필요` instead of filling with made-up numbers.
   - Keep claims conservative when period, contribution, or metric source is absent.

5. Preserve the user's positioning.
   - Career axis and story pattern should be inferred from the user's own career evidence notes.
   - Ask the user for their target role or positioning if not clear from the notes.
   - Tone: practical, specific, not overpolished or corporate-generic.

## Output Standards

- Write concise Korean summaries by default.
- For resume bullets, use action + method + result.
- For 자기소개서, avoid generic motivation and connect company task -> matching experience -> contribution.
- For interview answers, use STAR but keep the final answer conversational.
- For audits, return missing fields and suggested edits rather than rewriting everything at once.

## Editing Rules

- Do not add new dependencies unless the user asks for automation that truly needs them.
- Keep the user's career evidence notes as the source of truth.
- When adding a new project, update the relevant source note and index if relevant.
- When improving code, use the workspace Python environment described in the repository instructions.
