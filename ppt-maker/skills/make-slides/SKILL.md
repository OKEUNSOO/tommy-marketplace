---
name: make-slides
description: HTML 슬라이드 프레젠테이션 생성기. 마크다운 기획서(ppt.md 등)를 읽어 1280×720 캔버스 기반 단일 HTML 파일로 변환한다. 키보드 네비게이션, PDF 내보내기, 빌드 애니메이션 내장.
type: flexible
---

# make-slides Skill

마크다운 기획서 → 브라우저에서 바로 실행되는 HTML 프레젠테이션 생성.

Base directory: 이 파일과 같은 디렉토리 (`skills/make-slides/`)

## 핵심 파일

| 파일 | 역할 |
|------|------|
| `template.html` | CSS + JS 보일러플레이트 (슬라이드 없음, `<!-- ═══ SLIDES_HERE ═══ -->` 마커 위치에 주입) |
| `components.md` | 슬라이드 레이아웃 컴포넌트 라이브러리 |

---

## 워크플로우

### Step 1 — 기획서 분석

입력 파일(ppt.md 또는 사용자가 제공한 문서)을 읽는다.

다음 항목을 파악한다:
- 총 슬라이드 수와 각 슬라이드의 **핵심 메시지 1줄**
- 각 슬라이드에 담을 데이터 유형 (표, 숫자, 비교, 목록, 다이어그램 등)
- 프로젝트명, 브랜드 컬러, 아이콘 키워드

### Step 2 — 슬라이드 계획표 작성

작업 전에 계획표를 사용자에게 보여준다:

```
슬라이드 계획 (총 N매)
──────────────────────────────────────────
 #  | 레이아웃            | 핵심 내용
──────────────────────────────────────────
 1  | Cover              | 서비스명, 한 줄 설명
 2  | Left+Right-Panel   | 문제 정의 비교
 3  | Card-Grid (4열)    | 페르소나 4종
 4  | Full-Table         | 공공데이터 맵
...
──────────────────────────────────────────
```

### Step 3 — 슬라이드 HTML 생성

`components.md`의 레이아웃 패턴을 기반으로 각 슬라이드 `<section>` 블록을 생성한다.

**절대 좌표 규칙 (1280×720 캔버스)**

| 항목 | 값 |
|------|-----|
| 캔버스 | 1280 × 720px |
| 좌측 여백 | left: 64px |
| 우측 한계 | left + width ≤ 1216px |
| 헤더 행 | top: 40px (슬라이드 1 제외) |
| 콘텐츠 시작 | top: 90~130px |
| 하단 한계 | top + height ≤ 690px |

**레이아웃 선택 기준**

| 콘텐츠 유형 | 권장 레이아웃 |
|------------|--------------|
| 서비스 소개 / 표지 | Cover |
| 문제 정의, 기존 vs 신규 비교 | Left-Title + Right-Two-Panel |
| 페르소나, 특징 카드 4개 | Top-Bar + Card-Grid (4열) |
| 데이터 표, 비교표 | Full-Width Table |
| 기능 설명 (아이콘+텍스트) | Left-Title + Right-Feature-List |
| KPI, 핵심 수치 | Metric Cards |
| 시스템 구조, 흐름 | Architecture / Flow |
| 단계별 공개 효과 필요 | Build Effect (data-step) |

### Step 4 — template.html에 슬라이드 주입

`template.html`을 읽어 `<!-- ═══ SLIDES_HERE ═══ -->` 위치에 생성한 슬라이드 HTML을 주입하고 출력 파일로 저장한다.

```python
skill_dir = "<이 SKILL.md가 있는 디렉토리 경로>"
template = open(f'{skill_dir}/template.html').read()
slides_html = "\n".join(all_slide_sections)
result = template.replace('<!-- ═══ SLIDES_HERE ═══ -->', slides_html)
result = result.replace('{{PRESENTATION_TITLE}}', '프레젠테이션 제목')
open('output.html', 'w').write(result)
```

또는 Read → Edit으로 직접 주입한다.

### Step 5 — QA 체크리스트

- [ ] 모든 슬라이드 내용이 기획서와 일치하는가
- [ ] `left + width ≤ 1216` 오버플로우 없음
- [ ] `top + height ≤ 690` 하단 잘림 없음
- [ ] `position: absolute` 누락 없음
- [ ] `z-index: 10` (텍스트/아이콘), `z-index: 1` (도형 배경) 구분 적용
- [ ] FontAwesome 아이콘 클래스명 정확함 (`fas fa-ICON`)
- [ ] 슬라이드 번호 `aria-label="슬라이드 N"` 순서 정확
- [ ] 브라우저에서 열어 네비게이션(← →) 정상 동작 확인

---

## 슬라이드 HTML 패턴

모든 슬라이드는 이 껍데기로 감싼다:

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">

    <!-- 공통 헤더 (슬라이드 1 제외) -->
    <div data-object="true" data-object-type="icon"
        style="position: absolute; left: 40px; top: 40px; width: 24px; height: 24px; z-index: 10; display: flex; align-items: center; justify-content: center;">
        <i class="fas fa-route" style="color: #007BFF; font-size: 20px;"></i>
    </div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 74px; top: 40px; width: 400px; height: 24px; z-index: 10; display: flex; align-items: center;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 18px; font-weight: 700; color: #333333; opacity: 0.9;">프로젝트명</p>
    </div>

    <!-- 슬라이드 콘텐츠 여기에 -->

  </div>
</section>
```

자세한 레이아웃 패턴은 `components.md`를 참조한다.

---

## 색상 / 폰트

- **Primary**: `#007BFF`
- **Text**: `#333333` / `#555555`
- **Light bg**: `#F8F9FA` / `#EEF2FF`
- **Font**: `'Noto Sans KR', sans-serif`
- **Font sizes**: 제목 48–84px · 소제목 24–32px · 본문 15–20px

---

## 기술 제약

- 외부 의존성: FontAwesome 6, Noto Sans KR (Google Fonts), Chart.js — template.html에 이미 포함
- 슬라이드 전환: JS가 자동 처리 (touch, keyboard, URL hash)
- PDF 내보내기: 브라우저 인쇄(P키) → `@media print` 자동 처리
- `data-step` 빌드 효과: 해당 요소에 `data-step="N"` 추가만으로 동작

---

## 출력 파일

기본값: 입력 파일과 같은 디렉토리에 `output.html` (또는 사용자가 지정한 파일명).
