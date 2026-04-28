# tommy-marketplace

Claude Code 플러그인 모음입니다.

---

## 플러그인 목록

| 플러그인 | 버전 | 설명 |
|---------|------|------|
| [`ppt-maker`](#ppt-maker) | 1.0.0 | 마크다운 → HTML 슬라이드 변환기 |
| [`resume-designer`](#resume-designer) | 1.0.0 | 마크다운 이력서 → A4 HTML · P키 PDF 저장 |

---

## 설치

Claude Code에서 순서대로 실행:

```
/plugin marketplace add OKEUNSOO/tommy-marketplace
/plugin install
```

---

## ppt-maker

마크다운 기획서를 **브라우저에서 바로 실행되는 단일 HTML 파일**로 변환합니다.

### 사용법

```
/make-slides                    # 현재 디렉토리의 ppt.md를 슬라이드로 변환
/make-slides my-plan.md         # 특정 파일 지정
/make-slides AI 트렌드를 검색해서 슬라이드 만들어줘   # 웹 검색 후 슬라이드 생성
```

### 출력

- 단일 `output.html` (서버 불필요, 브라우저로 바로 열기)
- `← →` 슬라이드 이동 · `Space` 빌드 애니메이션 · `P` PDF 저장 · `F` 전체화면

### 지원 레이아웃

| 콘텐츠 유형 | 레이아웃 |
|------------|---------|
| 표지·서비스 소개 | Cover |
| 비교·대조 | Left + Right Two-Panel |
| 카드 나열 | Card Grid (4열 / 2×2) |
| 데이터·비교표 | Full-Width Table |
| 기능 설명 | Feature List |
| KPI·핵심 수치 | Metric Cards |
| 시스템 구조·흐름 | Architecture / Flow |
| 단계별 공개 | Build Effect |

### 구조

```
ppt-maker/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── make-slides/
        ├── SKILL.md        # 스킬 정의
        ├── template.html   # HTML 보일러플레이트
        └── components.md   # 레이아웃 컴포넌트 라이브러리
```

---

## resume-designer

마크다운 이력서를 **A4 인쇄 최적화 단일 HTML 파일**로 변환합니다.

### 사용법

```
/design-resume                  # 현재 디렉토리의 이력서.md 변환
/design-resume my-resume.md     # 특정 파일 지정
```

### 출력

- 단일 `resume.html` (서버 불필요, 브라우저로 바로 열기)
- `P` PDF 저장 (브라우저 인쇄 다이얼로그)
- A4 세로 · Noto Sans KR · 포인트컬러 #2563a8

### 구조

```
resume-designer/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── design-resume/
        ├── SKILL.md        # 스킬 정의
        └── template.html   # A4 HTML 보일러플레이트
```

---

## 라이선스

MIT
