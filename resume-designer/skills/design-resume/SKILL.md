---
description: 마크다운 이력서를 A4 HTML로 변환. 브라우저에서 P키로 PDF 저장
argument-hint: [이력서.md 경로 또는 내용]
---

마크다운 이력서를 HTML로 변환해줘.

입력: $ARGUMENTS (없으면 현재 디렉토리의 `이력서.md` 읽기)

## 작업 순서

1. **이력서 내용 파악**
   - 인자가 파일 경로면 읽어오기
   - 인자가 텍스트면 그대로 사용
   - 인자 없으면 현재 디렉토리 `이력서.md` 읽기

2. **템플릿 읽기**
   - 이 스킬 디렉토리의 `template.html` 읽기

3. **내용 채우기**
   이력서 마크다운을 파싱해서 템플릿의 각 영역에 매핑:

   | 마크다운 | HTML 영역 |
   |---------|-----------|
   | 문서 최상단 이름 (`# 이름`) | `.header h1` |
   | 이메일·연락처·링크 | `.contact-grid` span/a 태그 |
   | `## 요약` 또는 `## 자기소개` | `.section.intro` `.intro-text` |
   | `## 경험` 하위 `###` 각 항목 | `.item` 블록 (제목+날짜+불릿) |
   | `## 프로젝트` 하위 `###` 각 항목 | `.item` 블록 |
   | `## 스킬` | `.skill-group` 블록 |
   | `## 수상` / `## 자격증` | `.item` 블록 (title-light) |
   | `## 교육` | `.item` 블록 (title-light) |
   | `## 학력` | `.item` 블록 + `.item-subtitle` |

   **불릿 처리 규칙**
   - `-` 항목 → `<li>`
   - 중첩 `  -` → `<li>` 안의 `<ul><li>`
   - **굵게** → `<strong class="highlight">`
   - 날짜 패턴 `YYYY.MM – YYYY.MM` → `.item-date` span

   **페이지 분리**
   - 경험/프로젝트 → 첫 번째 `<div class="page">`
   - 스킬/수상/교육/학력 → 두 번째 `<div class="page page-secondary">`
   - 내용이 길면 자연스럽게 판단해서 분배

4. **파일 저장**
   - 현재 디렉토리에 `resume.html` 저장
   - "브라우저로 열고 P키를 누르면 PDF로 저장됩니다" 안내

## 출력 파일

- `resume.html` — 서버 불필요, 브라우저로 바로 열기
- **P** : 브라우저 인쇄 다이얼로그 → PDF 저장
- A4 세로, 여백 0, Noto Sans KR 폰트, 포인트컬러 #2563a8
