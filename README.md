# tommy-marketplace

Claude Code 플러그인 모음입니다.

---

## 플러그인 목록

| 플러그인 | 버전 | 설명 |
|---------|------|------|
| [`ppt-maker`](#ppt-maker) | 1.0.0 | 마크다운 → HTML 슬라이드 변환기 |

---

## 설치

### OMC 마켓플레이스 (권장)

[oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)가 설치되어 있다면 아래 두 명령어로 설치할 수 있습니다.

Claude Code에서 순서대로 실행:

```
/plugin marketplace add OKEUNSOO/tommy-marketplace
/plugin install
```

### 수동 설치

```bash
git clone https://github.com/OKEUNSOO/tommy-marketplace.git
cp -r tommy-marketplace/ppt-maker ~/.claude/plugins/ppt-maker
```

Claude Code를 재시작하면 스킬이 자동으로 로드됩니다.

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

## 라이선스

MIT
