# HTML-PPT Component Library

슬라이드 캔버스: **1280 × 720px**, 모든 요소 `position: absolute`.

## 좌표 기준

| 구역 | 값 |
|------|-----|
| 캔버스 | 1280 × 720px |
| 좌측 여백 | left: 64px |
| 우측 끝 | right content: 1216px (width: 1216-left) |
| 헤더 행 | top: 40px (아이콘+프로젝트명) |
| 콘텐츠 시작 | top: 130px (헤더 이하) |
| 하단 여백 | bottom: 30px (top ≤ 690px) |

## 공통 헤더 (cover 슬라이드 제외 전 슬라이드)

```html
<!-- 아이콘 -->
<div data-object="true" data-object-type="icon"
    style="position: absolute; left: 40px; top: 40px; width: 24px; height: 24px; z-index: 10; display: flex; align-items: center; justify-content: center;">
    <i class="fas fa-ICON_NAME" style="color: #007BFF; font-size: 20px;"></i>
</div>
<!-- 프로젝트명 -->
<div data-object="true" data-object-type="textbox"
    style="position: absolute; left: 74px; top: 40px; width: 400px; height: 24px; z-index: 10; display: flex; align-items: center;">
    <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 18px; font-weight: 700; color: #333333; opacity: 0.9;">프로젝트명</p>
</div>
```

---

## 레이아웃 컴포넌트

### 1. Cover (표지)

배경 장식 원 + 대형 타이틀 + 컬러 서브타이틀 바 + 발표자 정보.

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">
    <!-- 배경 장식 원 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 740px; top: -200px; width: 800px; height: 800px; background: rgba(0,123,255,0.05); border-radius: 50%; z-index: 1;"></div>
    <!-- 카테고리 아이콘 -->
    <div data-object="true" data-object-type="icon"
        style="position: absolute; left: 64px; top: 64px; width: 30px; height: 30px; z-index: 10; display: flex; align-items: center; justify-content: center;">
        <i class="fas fa-ICON" style="color: #007BFF; font-size: 24px;"></i>
    </div>
    <!-- 카테고리 텍스트 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 104px; top: 64px; width: 500px; height: 30px; z-index: 10; display: flex; align-items: center;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 20px; font-weight: 500; color: #333333;">카테고리 텍스트</p>
    </div>
    <!-- 메인 타이틀 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 205px; width: 1000px; height: 130px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 84px; font-weight: 900; color: #333333; letter-spacing: -2px; line-height: 1.1;">
            서비스명<span style="color: #007BFF;">(영문)</span></p>
    </div>
    <!-- 서브타이틀 바 (배경) -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 64px; top: 350px; width: 720px; height: 56px; z-index: 1; background-color: #007BFF; border-radius: 4px;"></div>
    <!-- 서브타이틀 텍스트 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 350px; width: 720px; height: 56px; z-index: 10; display: flex; align-items: center; padding-left: 24px; box-sizing: border-box;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 26px; font-weight: 700; color: #FFFFFF; letter-spacing: -0.5px;">한 줄 설명</p>
    </div>
    <!-- 부제 설명 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 434px; width: 1000px; height: 40px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 22px; font-weight: 400; color: #333333;">상세 설명 텍스트</p>
    </div>
    <!-- 발표자 정보 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 580px; width: 300px; height: 90px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 16px; color: #333333; opacity: 0.8; margin-bottom: 8px;">팀/개인명:</p>
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 32px; font-weight: 700; color: #333333;">이름</p>
    </div>
  </div>
</section>
```

---

### 2. Left-Title + Right-Two-Panel (좌: 제목+설명, 우: 비교 패널 2개)

비교/대조 슬라이드.

**좌표 계산 (반드시 준수)**
```
좌측 컬럼:  left: 64px,  width: 460px  → 끝: 524px
우측 시작:  left: 544px (gap 20px)
패널 A:     left: 544px, width: 326px  → 끝: 870px  ✓
패널 B:     left: 878px, width: 338px  → 끝: 1216px ✓

패널 A 아이콘:  left: 560px
패널 A 텍스트:  left: 586px, width: 268px → 끝: 854px  ✓
패널 B 아이콘:  left: 894px
패널 B 텍스트:  left: 920px, width: 278px → 끝: 1198px ✓

행 간격 (패널 content top: 215px 기준):
  4행: 215, 315, 415, 515  (100px 간격)
  5행: 215, 295, 375, 455, 535  (80px 간격)
```

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">
    <!-- 공통 헤더 -->
    <!-- ... (위 공통 헤더 코드) ... -->

    <!-- 배경 장식 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 800px; top: -200px; width: 800px; height: 800px; background: rgba(0,123,255,0.05); border-radius: 50%; z-index: 1;"></div>

    <!-- 좌측: 대제목 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 130px; width: 460px; height: 100px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 56px; font-weight: 900; color: #333333; line-height: 1.1; letter-spacing: -1px;">슬라이드 제목</p>
    </div>
    <!-- 좌측: 소제목 (파란색) -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 238px; width: 460px; height: 80px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 28px; font-weight: 700; color: #007BFF; line-height: 1.4; letter-spacing: -0.5px;">핵심 메시지<br/>두 줄까지 가능</p>
    </div>
    <!-- 좌측: 본문 설명 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 338px; width: 460px; height: 100px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 17px; font-weight: 400; color: #333333; line-height: 1.65;">
            본문 내용. <span style="font-weight: 700; color: #007BFF;">강조 텍스트</span>는 이렇게 표시합니다.</p>
    </div>
    <!-- 좌측: 통계 하이라이트 박스 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 64px; top: 452px; width: 460px; height: 104px; background-color: #EEF2FF; border: 1px solid #D0E2FF; border-radius: 8px; z-index: 1;"></div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 84px; top: 468px; width: 420px; height: 72px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 15px; color: #555555; margin-bottom: 6px;">레이블</p>
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 24px; font-weight: 700; color: #333333;">큰 수치 <span style="font-size: 15px; font-weight: 400; color: #888888;">(부연 설명)</span></p>
    </div>

    <!-- 패널 A (회색 배경 + 테두리, 기존/비교 대상) -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 544px; top: 150px; width: 326px; height: 490px; background-color: #F8F9FA; border: 1px solid #D1D5DB; border-radius: 8px; z-index: 1;"></div>
    <!-- 패널 A 헤더 바 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 544px; top: 150px; width: 326px; height: 52px; background-color: #E5E7EB; border-top-left-radius: 7px; border-top-right-radius: 7px; z-index: 2;"></div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 544px; top: 163px; width: 326px; height: 32px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 18px; font-weight: 700; color: #555555; text-align: center;">패널 A 제목</p>
    </div>

    <!-- 패널 B (파란 헤더, 강조/솔루션) -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 878px; top: 150px; width: 338px; height: 490px; background-color: #FFFFFF; border: 2px solid #007BFF; border-radius: 8px; z-index: 1; box-shadow: 0 4px 16px rgba(0,123,255,0.12);"></div>
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 878px; top: 150px; width: 338px; height: 52px; background-color: #007BFF; border-top-left-radius: 6px; border-top-right-radius: 6px; z-index: 2;"></div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 878px; top: 163px; width: 338px; height: 32px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 18px; font-weight: 700; color: #FFFFFF; text-align: center;">패널 B 제목</p>
    </div>

    <!-- 비교 행 아이템 패턴
         4행: top = 215, 315, 415, 515
         5행: top = 215, 295, 375, 455, 535
    -->
    <!-- 패널 A 아이템 (top마다 반복) -->
    <div data-object="true" data-object-type="icon"
        style="position: absolute; left: 560px; top: 215px; width: 20px; height: 20px; z-index: 10; display: flex; align-items: center; justify-content: center;">
        <i class="fas fa-ICON" style="color: #888888; font-size: 15px;"></i>
    </div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 586px; top: 213px; width: 268px; height: 72px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 14px; font-weight: 400; color: #555555; line-height: 1.5;">A 패널 항목 설명</p>
    </div>
    <!-- 패널 B 아이템 (동일한 top 사용) -->
    <div data-object="true" data-object-type="icon"
        style="position: absolute; left: 894px; top: 215px; width: 20px; height: 20px; z-index: 10; display: flex; align-items: center; justify-content: center;">
        <i class="fas fa-ICON" style="color: #007BFF; font-size: 15px;"></i>
    </div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 920px; top: 213px; width: 278px; height: 72px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 14px; font-weight: 700; color: #333333; line-height: 1.5;">B 패널 항목 설명</p>
    </div>
  </div>
</section>
```

---

### 3. Top-Bar + Center-Title + Card Grid (페르소나/특징 카드)

상단 색상 바 + 중앙 제목 + 하단 카드 그리드 (4열 또는 2×2).

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">
    <!-- 상단 액센트 바 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; top: 0; left: 0; width: 1280px; height: 10px; background-color: #007BFF; z-index: 1;"></div>
    <!-- 공통 헤더 (top: 40px 기준) -->
    <!-- ... -->
    <!-- 중앙 제목 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; top: 40px; left: 0; width: 1280px; text-align: center; z-index: 10;">
        <h1 style="font-family: 'Noto Sans KR', sans-serif; font-size: 64px; font-weight: 900; letter-spacing: 1px; color: #007BFF; margin: 0;">슬라이드 제목</h1>
    </div>

    <!-- 4열 카드 (각 카드: width≈270px, 간격 20px, 시작 left: 64px) -->
    <!-- 카드 1 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 64px; top: 150px; width: 270px; height: 510px; background-color: #FFFFFF; border: 2px solid #007BFF; border-radius: 12px; z-index: 1; box-shadow: 0 4px 12px rgba(0,123,255,0.1);"></div>
    <!-- 카드 헤더 바 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 64px; top: 150px; width: 270px; height: 50px; background-color: #007BFF; border-top-left-radius: 10px; border-top-right-radius: 10px; z-index: 2;"></div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 74px; top: 162px; width: 250px; height: 30px; z-index: 10; display: flex; align-items: center; justify-content: center;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 18px; font-weight: 700; color: #FFFFFF; text-align: center;">카드 제목</p>
    </div>
    <!-- 카드 2: left: 64+270+20=354px -->
    <!-- 카드 3: left: 354+270+20=644px -->
    <!-- 카드 4: left: 644+270+20=934px -->

    <!-- 카드 내 아이콘 행 (top: 220, 290, 360, 430, 500) -->
    <div data-object="true" data-object-type="icon"
        style="position: absolute; left: 80px; top: 220px; width: 20px; height: 20px; z-index: 10; display: flex; align-items: center; justify-content: center;">
        <i class="fas fa-ICON" style="color: #007BFF; font-size: 16px;"></i>
    </div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 110px; top: 218px; width: 204px; height: 56px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 14px; color: #333333; line-height: 1.5;">항목 내용</p>
    </div>
  </div>
</section>
```

---

### 4. Full-Width Table (전체 너비 데이터 테이블)

상단에 제목, 하단에 `<table>` HTML 테이블 사용.

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">
    <!-- 공통 헤더 -->
    <!-- 슬라이드 제목 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 90px; width: 1152px; height: 60px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 48px; font-weight: 900; color: #333333; letter-spacing: -1px;">슬라이드 제목</p>
    </div>
    <!-- 핵심 메시지 부제 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 156px; width: 1152px; height: 30px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 20px; font-weight: 500; color: #007BFF;">핵심 메시지 한 줄</p>
    </div>
    <!-- 테이블 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 200px; width: 1152px; z-index: 10;">
        <table style="width: 100%; border-collapse: collapse; font-family: 'Noto Sans KR', sans-serif; font-size: 15px;">
            <thead>
                <tr style="background-color: #007BFF; color: #FFFFFF;">
                    <th style="padding: 10px 12px; text-align: left; font-weight: 700;">열 1</th>
                    <th style="padding: 10px 12px; text-align: left; font-weight: 700;">열 2</th>
                    <th style="padding: 10px 12px; text-align: left; font-weight: 700;">열 3</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background-color: #F8F9FA; border-bottom: 1px solid #E0E0E0;">
                    <td style="padding: 9px 12px; color: #333333; font-weight: 600;">행 1 열 1</td>
                    <td style="padding: 9px 12px; color: #555555;">행 1 열 2</td>
                    <td style="padding: 9px 12px; color: #555555;">행 1 열 3</td>
                </tr>
                <tr style="background-color: #FFFFFF; border-bottom: 1px solid #E0E0E0;">
                    <td style="padding: 9px 12px; color: #333333; font-weight: 600;">행 2 열 1</td>
                    <td style="padding: 9px 12px; color: #555555;">행 2 열 2</td>
                    <td style="padding: 9px 12px; color: #555555;">행 2 열 3</td>
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</section>
```

---

### 5. Left-Title + Right-Feature List (좌: 제목/설명, 우: 아이콘+텍스트 리스트)

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">
    <!-- 공통 헤더 -->
    <!-- 좌측 제목 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 130px; width: 500px; height: 80px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 60px; font-weight: 900; color: #333333; line-height: 1.1; letter-spacing: -2px;">제목</p>
    </div>
    <!-- 좌측 소제목 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 220px; width: 500px; height: 60px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 28px; font-weight: 700; color: #007BFF; line-height: 1.4; letter-spacing: -0.5px;">소제목</p>
    </div>
    <!-- 좌측 설명 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 300px; width: 500px; height: 200px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 18px; color: #555555; line-height: 1.7;">설명 텍스트</p>
    </div>

    <!-- 우측 feature 리스트 (각 행 top: 130, 210, 290, 370, 450, 530 — 80px 간격) -->
    <!-- 구분선 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 620px; top: 130px; width: 2px; height: 500px; background-color: #E0E0E0; z-index: 1;"></div>

    <!-- 아이템 1 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 652px; top: 130px; width: 40px; height: 40px; background-color: #EEF2FF; border-radius: 8px; z-index: 1;"></div>
    <div data-object="true" data-object-type="icon"
        style="position: absolute; left: 652px; top: 130px; width: 40px; height: 40px; z-index: 10; display: flex; align-items: center; justify-content: center;">
        <i class="fas fa-ICON" style="color: #007BFF; font-size: 18px;"></i>
    </div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 710px; top: 128px; width: 506px; height: 60px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 18px; font-weight: 700; color: #333333; margin-bottom: 4px;">항목 제목</p>
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 15px; color: #555555; line-height: 1.4;">항목 설명</p>
    </div>
    <!-- 아이템 2: top+80, 아이템 3: top+160 ... -->
  </div>
</section>
```

---

### 6. Metric Cards (대형 숫자 강조)

3열 또는 4열 숫자 카드. 각 카드 `width: 350px`, 3열 기준 `left: 64, 447, 830`.

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">
    <!-- 공통 헤더 -->
    <!-- 제목 -->
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 90px; width: 1152px; height: 60px; z-index: 10;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 48px; font-weight: 900; color: #333333; letter-spacing: -1px;">제목</p>
    </div>

    <!-- 카드 1 -->
    <div data-object="true" data-object-type="shape"
        style="position: absolute; left: 64px; top: 200px; width: 350px; height: 380px; background-color: #F8F9FA; border-radius: 16px; z-index: 1; border: 1px solid #E0E0E0;"></div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 270px; width: 350px; z-index: 10; text-align: center;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 80px; font-weight: 900; color: #007BFF; text-align: center; letter-spacing: -2px;">300만</p>
    </div>
    <div data-object="true" data-object-type="textbox"
        style="position: absolute; left: 64px; top: 390px; width: 350px; z-index: 10; text-align: center;">
        <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 20px; color: #555555; text-align: center; line-height: 1.5;">레이블 설명</p>
    </div>
    <!-- 카드 2: left: 447px -->
    <!-- 카드 3: left: 830px -->
  </div>
</section>
```

---

### 7. Architecture / Flow Diagram (텍스트 기반 아키텍처)

배경 박스들로 레이어 표현, 화살표는 `→` 유니코드 또는 FontAwesome `fa-arrow-down`.

```html
<!-- 레이어 박스 패턴 (top 간격 약 100px씩) -->
<div data-object="true" data-object-type="shape"
    style="position: absolute; left: 200px; top: 130px; width: 880px; height: 70px; background-color: #EEF2FF; border: 1px solid #C7D2FE; border-radius: 8px; z-index: 1;"></div>
<div data-object="true" data-object-type="textbox"
    style="position: absolute; left: 200px; top: 130px; width: 880px; height: 70px; z-index: 10; display: flex; align-items: center; justify-content: center;">
    <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 20px; font-weight: 700; color: #333333; text-align: center;">레이어 이름 — 구성 요소</p>
</div>
<!-- 화살표 -->
<div data-object="true" data-object-type="icon"
    style="position: absolute; left: 620px; top: 205px; width: 40px; height: 24px; z-index: 10; display: flex; align-items: center; justify-content: center;">
    <i class="fas fa-arrow-down" style="color: #007BFF; font-size: 18px;"></i>
</div>
```

---

### 8. Build Effect (단계별 등장, data-step)

`data-step` 속성을 가진 요소는 클릭/Space 시 순서대로 나타납니다.

```html
<!-- step 1 먼저 등장, step 2 그 다음... -->
<div data-object="true" data-object-type="textbox" data-step="1"
    style="position: absolute; left: 64px; top: 200px; width: 500px; height: 40px; z-index: 10; --delay: 0s;">
    <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 22px; color: #333333;">첫 번째로 나타날 내용</p>
</div>
<div data-object="true" data-object-type="textbox" data-step="2"
    style="position: absolute; left: 64px; top: 260px; width: 500px; height: 40px; z-index: 10; --delay: 0.08s;">
    <p style="font-family: 'Noto Sans KR', sans-serif; font-size: 22px; color: #333333;">두 번째로 나타날 내용</p>
</div>
```

---

### 9. Chart Components (Chart.js)

Chart.js는 `template.html`에 이미 포함되어 있음. 모든 차트 슬라이드는 아래 **공통 쉘**을 사용하고, 차트 타입별 JS 옵션만 교체한다.

#### 공통 색상 상수 (JS 상단에 한 번만 선언)

```javascript
const BLUE       = '#007BFF';
const BLUE_MID   = '#60A5FA';
const BLUE_LIGHT = '#BFDBFE';
const TEXT       = '#333333';
const gridColor  = 'rgba(0,0,0,0.06)';
const baseFont   = { family: "'Noto Sans KR', sans-serif", size: 14 };
const commonScales = {
  x: { grid: { display: false }, ticks: { font: baseFont, color: TEXT } },
  y: { grid: { color: gridColor }, ticks: { font: baseFont, color: '#888' }, border: { dash: [4,4] } }
};
```

#### 우측 KPI 패널 패턴 (right column: left:940, width:276)

박스 간격은 12px 고정. 박스 top 계산: 이전 박스 `top + height + 12`.

```html
<!-- 블루 KPI 카드 (주요 수치) — top: 88, height: 80 -->
<div style="position:absolute;left:940px;top:88px;width:276px;height:80px;background:#007BFF;border-radius:12px;z-index:1;"></div>
<div style="position:absolute;left:940px;top:88px;width:276px;height:80px;z-index:10;display:flex;flex-direction:column;align-items:center;justify-content:center;">
  <p style="font-family:'Noto Sans KR',sans-serif;font-size:30px;font-weight:900;color:#FFFFFF;">수치</p>
  <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;color:rgba(255,255,255,0.8);">레이블</p>
</div>

<!-- 보조 카드 (light blue bg) — top: 88+80+12=180 -->
<div style="position:absolute;left:940px;top:180px;width:276px;height:72px;background:#EEF2FF;border-radius:10px;border:1px solid #D0E2FF;z-index:1;"></div>
<div style="position:absolute;left:940px;top:180px;width:276px;height:72px;z-index:10;display:flex;flex-direction:column;align-items:center;justify-content:center;">
  <p style="font-family:'Noto Sans KR',sans-serif;font-size:22px;font-weight:900;color:#007BFF;">수치</p>
  <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;color:#555;">레이블</p>
</div>

<!-- 범례 박스 (flex 중앙 정렬 필수) — height: 2항목=80px, 3항목=108px -->
<div style="position:absolute;left:940px;top:88px;width:276px;height:80px;background:#F8F9FA;border-radius:12px;border:1px solid #E0E0E0;z-index:1;"></div>
<div style="position:absolute;left:940px;top:88px;width:276px;height:80px;z-index:10;display:flex;flex-direction:column;justify-content:center;gap:10px;padding-left:20px;">
  <div style="display:flex;align-items:center;">
    <div style="width:20px;height:12px;background:#007BFF;border-radius:2px;margin-right:10px;flex-shrink:0;"></div>
    <p style="font-family:'Noto Sans KR',sans-serif;font-size:14px;font-weight:700;color:#333;">항목 A</p>
  </div>
  <div style="display:flex;align-items:center;">
    <div style="width:20px;height:12px;background:#BFDBFE;border-radius:2px;margin-right:10px;flex-shrink:0;"></div>
    <p style="font-family:'Noto Sans KR',sans-serif;font-size:14px;font-weight:700;color:#333;">항목 B</p>
  </div>
</div>
```

#### 캔버스 위치

| 용도 | left | top | width | height |
|------|------|-----|-------|--------|
| 일반 차트 (막대/라인/콤보/워터폴/가로막대) | 64px | 192px | 858px | 458px |
| 도넛 차트 | 64px | 192px | 560px | 468px |

```html
<!-- 일반 차트 캔버스 -->
<div style="position:absolute;left:64px;top:192px;width:858px;height:458px;z-index:10;">
  <canvas id="chartN"></canvas>
</div>
```

---

#### ① Column Chart (단순 막대 — 기간별 추이, 카테고리 비교)

```javascript
new Chart(document.getElementById('chartN'), {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      data: [285, 312, 298, 360],
      backgroundColor: (ctx) => ctx.dataIndex >= 2 ? BLUE : BLUE_LIGHT, // 강조 구간 분리
      borderRadius: 6,
      borderSkipped: false,
    }]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      ...commonScales,
      y: { ...commonScales.y, ticks: { ...commonScales.y.ticks, callback: v => v + '억' } }
    }
  }
});
```

---

#### ② Grouped Column Chart (그룹 막대 — A vs B 비교)

```javascript
new Chart(document.getElementById('chartN'), {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [
      { label: '목표', data: [320, 350, 380, 410], backgroundColor: BLUE, borderRadius: 6, borderSkipped: false },
      { label: '실적', data: [342, 378, 395, 398], backgroundColor: BLUE_LIGHT, borderRadius: 6, borderSkipped: false }
    ]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: { ...commonScales, y: { ...commonScales.y, ticks: { ...commonScales.y.ticks, callback: v => v + '억' } } }
  }
});
```

---

#### ③ Line Chart (시계열 추세 + 점선 전망)

```javascript
new Chart(document.getElementById('chartN'), {
  type: 'line',
  data: {
    labels: ['2020', '2021', '2022', '2023', '2024', '2025', '2030'],
    datasets: [
      {
        label: '실적', data: [120, 148, 192, 265, 392, null, null],
        borderColor: BLUE, backgroundColor: 'rgba(0,123,255,0.08)',
        borderWidth: 3, pointRadius: 5, pointBackgroundColor: BLUE,
        pointBorderColor: '#fff', pointBorderWidth: 2, tension: 0.3, fill: true, spanGaps: false,
      },
      {
        label: '전망', data: [null, null, null, null, 392, 490, 1200],
        borderColor: BLUE, borderDash: [6, 4], borderWidth: 2.5,
        pointRadius: 5, pointBackgroundColor: '#fff', pointBorderColor: BLUE,
        pointBorderWidth: 2, tension: 0.3, fill: false, spanGaps: false,
      }
    ]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: { ...commonScales, y: { ...commonScales.y, ticks: { ...commonScales.y.ticks, callback: v => '$' + v + 'B' } } }
  }
});
```

범례 선 스타일 (실선/점선 구분):
```html
<div style="display:flex;align-items:center;">
  <div style="width:24px;height:3px;background:#007BFF;border-radius:2px;margin-right:8px;"></div>
  <p ...>실적 (2020–2024)</p>
</div>
<div style="display:flex;align-items:center;">
  <div style="width:24px;height:3px;background:#007BFF;opacity:0.4;border-top:2px dashed #007BFF;margin-right:8px;"></div>
  <p ...>전망 (2025–)</p>
</div>
```

---

#### ④ Stacked Column Chart (누적 막대 — 구성 비율 변화)

```javascript
new Chart(document.getElementById('chartN'), {
  type: 'bar',
  data: {
    labels: ['2022', '2023', '2024'],
    datasets: [
      { label: '구독', data: [148, 220, 327], backgroundColor: BLUE, borderRadius: 0, borderSkipped: false },
      { label: '프로젝트', data: [98, 115, 104], backgroundColor: BLUE_MID, borderRadius: 0, borderSkipped: false },
      { label: '일회성', data: [124, 95, 64], backgroundColor: BLUE_LIGHT, borderRadius: 6, borderSkipped: 'bottom' }
    ]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      x: { ...commonScales.x, stacked: true },
      y: { ...commonScales.y, stacked: true, ticks: { ...commonScales.y.ticks, callback: v => v + '억' } }
    }
  }
});
```

---

#### ⑤ Donut Chart (도넛 — 점유율·비중)

캔버스: `left:64, width:560`. 범례는 `left:650`에 배치.

```javascript
new Chart(document.getElementById('chartN'), {
  type: 'doughnut',
  data: {
    labels: ['A사', 'B사', 'C사', '기타'],
    datasets: [{
      data: [32, 22, 15, 31],
      backgroundColor: [BLUE, BLUE_MID, BLUE_LIGHT, '#E5E7EB'],
      borderWidth: 0,
      hoverOffset: 8,
    }]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    cutout: '62%',
    plugins: { legend: { display: false } }
  }
});
```

범례 (left:650, top:260):
```html
<div style="position:absolute;left:650px;top:260px;width:240px;z-index:10;">
  <div style="display:flex;align-items:center;margin-bottom:18px;">
    <div style="width:16px;height:16px;background:#007BFF;border-radius:3px;margin-right:10px;flex-shrink:0;"></div>
    <p style="font-family:'Noto Sans KR',sans-serif;font-size:17px;font-weight:700;color:#333;">A사 <span style="color:#007BFF;">32%</span></p>
  </div>
  <!-- 항목 반복 -->
</div>
```

---

#### ⑥ Horizontal Bar Chart (가로 막대 — 순위·랭킹)

```javascript
new Chart(document.getElementById('chartN'), {
  type: 'bar',
  data: {
    labels: ['1위 항목', '2위 항목', '3위', '4위', '5위', '6위'],
    datasets: [{
      data: [4.8, 4.2, 3.7, 3.1, 2.6, 2.0],
      backgroundColor: (ctx) => ctx.dataIndex === 0 ? BLUE : BLUE_LIGHT, // 1위만 강조
      borderRadius: 6,
      borderSkipped: false,
    }]
  },
  options: {
    indexAxis: 'y',  // ← 가로 막대 핵심 옵션
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      x: { grid: { color: gridColor }, ticks: { font: baseFont, color: '#888', callback: v => v + 'B' }, border: { dash: [4,4] } },
      y: { grid: { display: false }, ticks: { font: { ...baseFont, size: 13 }, color: TEXT } }
    }
  }
});
```

---

#### ⑦ Combo Chart — Bar + Line 이중축

막대: 절대값(좌축), 선: 비율·성장률(우축). `order` 필수 — line이 bar 위에 렌더링.

```javascript
new Chart(document.getElementById('chartN'), {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [
      {
        type: 'bar', label: '매출',
        data: [285, 312, 298, 360],
        backgroundColor: BLUE_LIGHT, borderRadius: 6,
        yAxisID: 'y', order: 2,  // order 높을수록 뒤에 그려짐
      },
      {
        type: 'line', label: 'YoY %',
        data: [null, null, 20.0, 32.6],
        borderColor: '#F97316', backgroundColor: 'transparent',
        borderWidth: 3, pointRadius: 6,
        pointBackgroundColor: '#F97316', pointBorderColor: '#fff', pointBorderWidth: 2,
        tension: 0.3, yAxisID: 'y2', order: 1,  // order 낮을수록 위에 그려짐
      }
    ]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      x: commonScales.x,
      y:  { ...commonScales.y, ticks: { ...commonScales.y.ticks, callback: v => v + '억' } },
      y2: { position: 'right', grid: { display: false }, border: { display: false },
            ticks: { font: baseFont, color: '#F97316', callback: v => v + '%' } }
    }
  }
});
```

---

#### ⑧ Waterfall Chart (워터폴 — 기여도·P&L 브릿지)

Chart.js floating bar `[start, end]` 방식. 기준값(합계)은 `[0, total]`, 증가는 `[prev, prev+delta]`, 감소는 `[prev, prev-delta]`.

색상: 합계=`BLUE`, 증가=`BLUE_MID`, 감소=`'#FDA4A4'`

```javascript
// 예: 2023(480) → 신규+80 → 업셀+60 → 이탈-40 → 가격+50 → 2024(630)
new Chart(document.getElementById('chartN'), {
  type: 'bar',
  data: {
    labels: ['2023 기준', '신규 고객', '업셀', '이탈', '가격 인상', '2024 기준'],
    datasets: [{
      data: [[0,480], [480,560], [560,620], [620,580], [580,630], [0,630]],
      backgroundColor: [BLUE, BLUE_MID, BLUE_MID, '#FDA4A4', BLUE_MID, BLUE],
      borderRadius: 6,
      borderSkipped: false,
    }]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: ctx => {
            const [s, e] = ctx.raw;
            const diff = e - s;
            if (s === 0) return ` 합계: ${e}억원`;
            return diff >= 0 ? ` +${diff}억원` : ` ${diff}억원`;
          }
        }
      }
    },
    scales: {
      x: commonScales.x,
      y: { ...commonScales.y, min: 400, ticks: { ...commonScales.y.ticks, callback: v => v + '억' } }
      // min 값: 데이터 최솟값보다 약간 낮게 설정해 워터폴 변화가 잘 보이도록
    }
  }
});
```

---

### 10. 2×2 Matrix (우선순위 매트릭스)

순수 HTML — JS 불필요. 4개 사분면 + 중심 교차선 + 축 레이블 + 아이템 점(circle).

**좌표 기준**
```
Matrix: left:96, top:188, width:804, height:440
  TL (좌상, 낮은X·높은Y): left:96,  top:188, width:402, height:220
  TR (우상, 높은X·높은Y): left:498, top:188, width:402, height:220  ← 강조
  BL (좌하, 낮은X·낮은Y): left:96,  top:408, width:402, height:220
  BR (우하, 높은X·낮은Y): left:498, top:408, width:402, height:220
중심 가로선: left:96,  top:408, width:804, height:2
중심 세로선: left:498, top:188, width:2,   height:440
X축 레이블: left:96, top:636, width:804, text-align:center
Y축 레이블: left:64, top:188, width:24, height:440, rotate(-90deg)
우측 KPI: left:916
```

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">
    <!-- 공통 헤더 -->
    <div style="position:absolute;left:64px;top:88px;width:800px;height:56px;z-index:10;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:48px;font-weight:900;color:#333333;letter-spacing:-1px;">슬라이드 제목</p>
    </div>
    <div style="position:absolute;left:64px;top:150px;width:800px;height:28px;z-index:10;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:20px;font-weight:500;color:#007BFF;">핵심 메시지</p>
    </div>

    <!-- Y축 레이블 (세로 텍스트) -->
    <div style="position:absolute;left:64px;top:188px;width:24px;height:440px;z-index:10;display:flex;align-items:center;justify-content:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;font-weight:700;color:#555;transform:rotate(-90deg);white-space:nowrap;">← 낮음   Y축 레이블   높음 →</p>
    </div>

    <!-- TL: 낮은 X, 높은 Y -->
    <div style="position:absolute;left:96px;top:188px;width:402px;height:220px;background:#F8F9FA;border:1px solid #E0E0E0;z-index:1;"></div>
    <div style="position:absolute;left:106px;top:196px;z-index:10;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;font-weight:700;color:#888;">❓ 재검토</p>
    </div>

    <!-- TR: 높은 X, 높은 Y — 강조 (파란 테두리) -->
    <div style="position:absolute;left:498px;top:188px;width:402px;height:220px;background:#EEF2FF;border:2px solid #007BFF;z-index:1;"></div>
    <div style="position:absolute;left:508px;top:196px;z-index:10;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;font-weight:700;color:#007BFF;">⭐ 주력 집중</p>
    </div>

    <!-- BL: 낮은 X, 낮은 Y -->
    <div style="position:absolute;left:96px;top:408px;width:402px;height:220px;background:#F8F9FA;border:1px solid #E0E0E0;z-index:1;"></div>
    <div style="position:absolute;left:106px;top:594px;z-index:10;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;font-weight:700;color:#888;">🔻 보류</p>
    </div>

    <!-- BR: 높은 X, 낮은 Y -->
    <div style="position:absolute;left:498px;top:408px;width:402px;height:220px;background:#F8F9FA;border:1px solid #E0E0E0;z-index:1;"></div>
    <div style="position:absolute;left:508px;top:594px;z-index:10;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;font-weight:700;color:#888;">⚡ 빠른 실행</p>
    </div>

    <!-- 중심 교차선 -->
    <div style="position:absolute;left:96px;top:408px;width:804px;height:2px;background:#007BFF;opacity:0.25;z-index:2;"></div>
    <div style="position:absolute;left:498px;top:188px;width:2px;height:440px;background:#007BFF;opacity:0.25;z-index:2;"></div>

    <!-- X축 레이블 -->
    <div style="position:absolute;left:96px;top:636px;width:804px;height:24px;z-index:10;display:flex;justify-content:center;align-items:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;font-weight:700;color:#555;">← 낮음   X축 레이블   높음 →</p>
    </div>

    <!-- 아이템 점 패턴
         강조(TR): background:#007BFF, 흰 텍스트
         보통(TL): background:#D0E2FF, border:#007BFF, 파란 텍스트
         낮은 우선순위(BR/BL): background:#E5E7EB, border:#999, 회색 텍스트
         크기: width:44px, height:44px, border-radius:50%
         내부 텍스트: font-size:11~12px, 2~4글자 권장
         레이블: 점 바로 아래 (top+48px), width:68px, text-align:center (선택)
    -->
    <!-- TR 아이템 예시 -->
    <div style="position:absolute;left:640px;top:220px;width:44px;height:44px;background:#007BFF;border-radius:50%;z-index:10;display:flex;align-items:center;justify-content:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:11px;font-weight:700;color:#FFFFFF;">항목A</p>
    </div>

    <!-- 우측 KPI 패널 -->
    <div style="position:absolute;left:916px;top:188px;width:276px;height:80px;background:#007BFF;border-radius:12px;z-index:1;"></div>
    <div style="position:absolute;left:916px;top:188px;width:276px;height:80px;z-index:10;display:flex;flex-direction:column;align-items:center;justify-content:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:20px;font-weight:900;color:#FFFFFF;">주력 집중 N개</p>
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;color:rgba(255,255,255,0.8);">즉시 실행 우선순위</p>
    </div>
  </div>
</section>
```

---

### 11. Funnel Chart (전환 깔때기)

순수 HTML — JS 불필요. 중앙 정렬 가로 막대 (비율 너비) + 우측 수치 레이블.

**바 너비 계산 (비율 기반 — 필수)**
```
max_width = 520  (Stage 1 기준)
center_x  = 430  (left:170 + 520/2)

stage_width = round((stage_count / stage1_count) * max_width)
stage_left  = 170 + round((520 - stage_width) / 2)

예시 (5,200명 기준):
  Stage 1: 5200명 → width:520, left:170
  Stage 2: 3800명 → width:380, left:240
  Stage 3: 2100명 → width:210, left:275
  Stage 4:  980명 → width:98,  left:381
  Stage 5:  420명 → width:42,  left:409
```

**좌표 기준**
```
Stage top 시작: top:228 (제목/부제 충분한 여백 확보)
각 stage 높이: 68px, 간격: 6px
Stage 1 top: 228 → Stage 5 bottom: 228+5×68+4×6=592
우측 수치: left:704, width:200 → right:904
우측 KPI: left:916
```

**스테이지 색상 (밝기 감소)**
```
Stage 1: #007BFF (흰 텍스트)
Stage 2: #2E8FFF (흰 텍스트)
Stage 3: #60A5FA (흰 텍스트)
Stage 4: #93C5FD (어두운 텍스트)
Stage 5: #BFDBFE (어두운 텍스트)
최대 이탈 구간: border:2px solid #F97316 + 오렌지 뱃지
```

```html
<section class="slide" role="group" aria-roledescription="slide" aria-label="슬라이드 N">
  <div class="slide-container" style="position: relative; width: 1280px; height: 720px; overflow: hidden; top: 0; left: 0; background-color: #FFFFFF;">
    <!-- 공통 헤더 -->
    <div style="position:absolute;left:64px;top:88px;width:800px;height:56px;z-index:10;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:48px;font-weight:900;color:#333333;letter-spacing:-1px;">전환 깔때기 분석</p>
    </div>
    <div style="position:absolute;left:64px;top:150px;width:800px;height:28px;z-index:10;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:20px;font-weight:500;color:#007BFF;">핵심 메시지</p>
    </div>

    <!-- Stage 1 (비율로 width·left 계산 후 대입) -->
    <div style="position:absolute;left:170px;top:228px;width:520px;height:68px;background:#007BFF;border-radius:8px;z-index:1;"></div>
    <div style="position:absolute;left:170px;top:228px;width:520px;height:68px;z-index:10;display:flex;align-items:center;padding-left:20px;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:16px;font-weight:700;color:#FFFFFF;">인지 (Awareness)</p>
    </div>
    <div style="position:absolute;left:704px;top:228px;width:200px;height:68px;z-index:10;display:flex;flex-direction:column;justify-content:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:20px;font-weight:900;color:#007BFF;">N명</p>
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:12px;color:#888;">100%</p>
    </div>

    <!-- Stage 2 top:302 (228+68+6) -->
    <div style="position:absolute;left:[계산된 left]px;top:302px;width:[계산된 width]px;height:68px;background:#2E8FFF;border-radius:8px;z-index:1;"></div>
    <div style="position:absolute;left:[계산된 left]px;top:302px;width:[계산된 width]px;height:68px;z-index:10;display:flex;align-items:center;padding-left:20px;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:16px;font-weight:700;color:#FFFFFF;">관심 (Interest)</p>
    </div>
    <div style="position:absolute;left:704px;top:302px;width:200px;height:68px;z-index:10;display:flex;flex-direction:column;justify-content:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:20px;font-weight:900;color:#007BFF;">N명</p>
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:12px;color:#888;">XX% <span style="color:#60A5FA;">▼ XX%p</span></p>
    </div>

    <!-- Stage 3 top:376 — 최대 이탈 구간이면 border:2px solid #F97316 추가 -->
    <!-- Stage 4 top:450 -->
    <!-- Stage 5 top:524 -->
    <!-- top 공식: stage1_top + (n-1) × (68+6) -->

    <!-- 우측 KPI -->
    <div style="position:absolute;left:916px;top:228px;width:276px;height:80px;background:#007BFF;border-radius:12px;z-index:1;"></div>
    <div style="position:absolute;left:916px;top:228px;width:276px;height:80px;z-index:10;display:flex;flex-direction:column;align-items:center;justify-content:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:30px;font-weight:900;color:#FFFFFF;">X.X%</p>
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;color:rgba(255,255,255,0.8);">최종 전환율</p>
    </div>
  </div>
</section>
```

---

### 12. Timeline / Roadmap (수평 타임라인)

순수 HTML — JS 불필요. 수평선 + 마일스톤 원 + 카드 레이블 (위/아래 교차 배치).

**좌표 기준**
```
수평선: top:400 기준
마일스톤 원: width:40, height:40, top:380 (중심=400)
현재 마일스톤 강조: width:56, height:56, top:372 + 외곽 glow ring
과거 구간 선: background:#007BFF
미래 구간 선: background:#D0E2FF (dashed 효과는 border 활용)
레이블 카드 위: top 약 240–280
레이블 카드 아래: top 약 450–470
수직 연결선: width:2px, background:#007BFF (과거), #D0E2FF (미래), opacity:0.4
```

**마일스톤 상태별 스타일**
```
완료 (과거):  background:#007BFF, 내부 fa-check 아이콘
현재 진행:    background:#FFFFFF, border:4px solid #007BFF,
              내부 width:18px blue dot, box-shadow:0 0 0 6px rgba(0,123,255,0.15)
예정 (미래):  background:#FFFFFF, border:3px solid #D0E2FF, 내부 #D0E2FF dot
마지막(목표): background:#FFFFFF, border:3px solid #D0E2FF, 내부 fa-flag #D0E2FF
```

**레이블 카드 스타일**
```
완료 카드(위): background:#007BFF, border-radius:8px, 흰 텍스트
완료 카드(아래): background:#EEF2FF, border:1px solid #D0E2FF, 파란 텍스트
예정 카드: background:#F8F9FA, border:1px dashed #D0E2FF, 회색 텍스트
```

```html
<section class="slide" ...>
  <div class="slide-container" ...>
    <!-- 헤더, 제목, 부제 -->

    <!-- 과거 구간 선 -->
    <div style="position:absolute;left:120px;top:399px;width:520px;height:4px;background:#007BFF;border-radius:2px 0 0 2px;z-index:2;"></div>
    <!-- 미래 구간 선 -->
    <div style="position:absolute;left:640px;top:399px;width:240px;height:4px;background:#D0E2FF;border-radius:0 2px 2px 0;z-index:2;"></div>

    <!-- 완료 마일스톤 -->
    <div style="position:absolute;left:100px;top:380px;width:40px;height:40px;background:#007BFF;border-radius:50%;z-index:10;display:flex;align-items:center;justify-content:center;">
      <i class="fas fa-check" style="color:#fff;font-size:13px;"></i>
    </div>
    <!-- 수직 연결선 -->
    <div style="position:absolute;left:119px;top:298px;width:2px;height:82px;background:#007BFF;opacity:0.4;z-index:2;"></div>
    <!-- 날짜 레이블 (아래) -->
    <div style="position:absolute;left:88px;top:428px;z-index:10;text-align:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:12px;font-weight:700;color:#007BFF;">Q1 2025</p>
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:11px;color:#888;">완료 ✓</p>
    </div>

    <!-- 현재 마일스톤 (glow 강조) -->
    <div style="position:absolute;left:617px;top:372px;width:56px;height:56px;background:#FFFFFF;border:4px solid #007BFF;border-radius:50%;z-index:10;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px rgba(0,123,255,0.15);">
      <div style="width:18px;height:18px;background:#007BFF;border-radius:50%;"></div>
    </div>

    <!-- 우측 KPI 패널 (left:916) -->
    <div style="position:absolute;left:916px;top:190px;width:276px;height:80px;background:#007BFF;border-radius:12px;z-index:1;"></div>
    <!-- ... KPI 내용 ... -->
  </div>
</section>
```

---

### 13. Chevron Process (화살표 5단계)

순수 HTML — JS 불필요. `clip-path` polygon으로 화살표 형태 구현.

**좌표 기준**
```
각 chevron: width:220, height:90, top:290
left 시작:  64, 260, 456, 652, 848  (겹침 24px)
겹침 처리:  각 div z-index:3,4,5,6,7 순서로 증가
```

**clip-path 패턴**
```
첫 번째 (직각 왼쪽):
  polygon(0 0, calc(100%-22px) 0, 100% 50%, calc(100%-22px) 100%, 0 100%)

중간 (양쪽 화살표):
  polygon(22px 0, calc(100%-22px) 0, 100% 50%, calc(100%-22px) 100%, 0 100%, 22px 50%)

마지막 (직각 오른쪽):
  polygon(22px 0, 100% 0, 100% 100%, 0 100%, 22px 50%)
```

**색상 + 텍스트 색**
```
Step 1: #007BFF  → 텍스트 #FFFFFF
Step 2: #2E8FFF  → 텍스트 #FFFFFF
Step 3: #60A5FA  → 텍스트 #FFFFFF
Step 4: #93C5FD  → 텍스트 #333333
Step 5: #BFDBFE  → 텍스트 #333333
```

**하단 상세 카드** (top:404, 각 chevron 너비에 맞춰 배치)
```
border-top:3px solid [step 색상], border-radius:0 0 8px 8px
내부: 소제목 + 설명 + 기간 레이블
```

```html
<!-- 첫 번째 chevron -->
<div style="position:absolute;left:64px;top:290px;width:220px;height:90px;background:#007BFF;z-index:3;
  clip-path:polygon(0 0, calc(100% - 22px) 0, 100% 50%, calc(100% - 22px) 100%, 0 100%);
  display:flex;align-items:center;justify-content:center;padding-right:22px;">
  <div style="text-align:center;">
    <p style="font-family:'Noto Sans KR',sans-serif;font-size:12px;font-weight:700;color:rgba(255,255,255,0.8);margin-bottom:2px;">STEP 01</p>
    <p style="font-family:'Noto Sans KR',sans-serif;font-size:16px;font-weight:700;color:#fff;">단계명</p>
  </div>
</div>

<!-- 중간 chevron (left:260, z-index:4) -->
<div style="position:absolute;left:260px;top:290px;width:220px;height:90px;background:#2E8FFF;z-index:4;
  clip-path:polygon(22px 0, calc(100% - 22px) 0, 100% 50%, calc(100% - 22px) 100%, 0 100%, 22px 50%);
  display:flex;align-items:center;justify-content:center;">
  <!-- ... -->
</div>

<!-- 마지막 chevron (left:848, z-index:7) -->
<div style="position:absolute;left:848px;top:290px;width:220px;height:90px;background:#BFDBFE;z-index:7;
  clip-path:polygon(22px 0, 100% 0, 100% 100%, 0 100%, 22px 50%);
  display:flex;align-items:center;justify-content:center;padding-left:22px;">
  <!-- ... -->
</div>
```

---

#### ⑨ Scatter / Bubble Chart (분포 분석)

Chart.js `bubble` 타입. 원 크기(`r`)로 세 번째 차원 표현.

캔버스: `left:64, top:192, width:858, height:458` (일반 차트와 동일)

```javascript
new Chart(document.getElementById('chartN'), {
  type: 'bubble',
  data: {
    datasets: [
      {
        label: 'Enterprise',
        data: [
          { x: 85, y: 920, r: 22 },   // x: 이용률%, y: 매출, r: 버블 반지름(px)
          { x: 92, y: 1240, r: 28 },
        ],
        backgroundColor: 'rgba(0,123,255,0.55)',
        borderColor: '#007BFF',
        borderWidth: 2,
      },
      {
        label: 'Mid-Market',
        data: [{ x: 52, y: 320, r: 12 }],
        backgroundColor: 'rgba(96,165,250,0.55)',
        borderColor: '#60A5FA',
        borderWidth: 2,
      },
      {
        label: 'SMB',
        data: [{ x: 22, y: 80, r: 6 }],
        backgroundColor: 'rgba(191,219,254,0.65)',
        borderColor: '#BFDBFE',
        borderWidth: 1.5,
      }
    ]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: { legend: { display: false } },
    scales: {
      x: {
        title: { display: true, text: 'X축 레이블', font: baseFont, color: '#888' },
        grid: { color: gridColor },
        ticks: { font: baseFont, color: '#888', callback: v => v + '%' },
        border: { dash: [4, 4] }, min: 0, max: 110
      },
      y: {
        title: { display: true, text: 'Y축 레이블', font: baseFont, color: '#888' },
        grid: { color: gridColor },
        ticks: { font: baseFont, color: '#888' },
        border: { dash: [4, 4] }
      }
    }
  }
});
```

범례: 우측 KPI 패널 내 원형 색상 스와치 (border-radius:50%)
```html
<div style="display:flex;align-items:center;">
  <div style="width:16px;height:16px;background:#007BFF;border-radius:50%;margin-right:10px;opacity:0.7;flex-shrink:0;"></div>
  <p ...>Enterprise</p>
</div>
```

---

### 14. KPI Dashboard (6타일 2×3)

순수 HTML — JS 불필요. 각 타일은 `display:flex;flex-direction:column` 컨테이너.

**좌표 기준**
```
타일 크기: width:373, height:234
col left: 64, 453, 842  (gap:16px)
row top:  176, 426       (gap:16px)
```

**타일 내부 구조 (flex column, justify-content:space-between)**
```
① 상단 accent bar (height:6px) — Row 1: #007BFF, Row 2: #60A5FA
② 내부 padding:16px 20px, flex:1, justify-content:space-between
   - 상단 행: 지표명(13px #888) + 아이콘
   - 중간: 큰 숫자(44px 900) + 보조 설명(12px #aaa)
   - 하단: 트렌드 뱃지 (inline-flex, align-self:flex-start)
```

**트렌드 뱃지 색상**
```
상승(긍정): background:#DCFCE7, 텍스트 #16A34A, fa-arrow-up
하락(긍정): background:#DCFCE7, 텍스트 #16A34A, fa-arrow-down  ← 이탈률 감소 등
하락(부정): background:#FEE2E2, 텍스트 #DC2626, fa-arrow-down
```

```html
<div style="position:absolute;left:64px;top:176px;width:373px;height:234px;
  background:#FFFFFF;border:1px solid #E0E0E0;border-radius:12px;
  box-shadow:0 2px 8px rgba(0,0,0,0.06);overflow:hidden;
  display:flex;flex-direction:column;z-index:10;">
  <!-- Accent bar -->
  <div style="height:6px;background:#007BFF;flex-shrink:0;"></div>
  <!-- 내용 -->
  <div style="padding:16px 20px;display:flex;flex-direction:column;flex:1;justify-content:space-between;">
    <!-- 레이블 + 아이콘 -->
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;color:#888;font-weight:500;">지표명</p>
      <i class="fas fa-ICON" style="color:#007BFF;font-size:15px;"></i>
    </div>
    <!-- 큰 숫자 -->
    <div>
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:44px;font-weight:900;color:#333333;letter-spacing:-2px;line-height:1.1;">수치<span style="font-size:20px;font-weight:700;color:#888;margin-left:4px;">단위</span></p>
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:12px;color:#aaa;margin-top:4px;">보조 설명</p>
    </div>
    <!-- 트렌드 뱃지 -->
    <div style="display:inline-flex;align-items:center;background:#DCFCE7;border-radius:20px;padding:5px 12px;gap:5px;align-self:flex-start;">
      <i class="fas fa-arrow-up" style="color:#16A34A;font-size:11px;"></i>
      <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;font-weight:700;color:#16A34A;">+X% QoQ</p>
    </div>
  </div>
</div>
<!-- col 2: left:453 / col 3: left:842 -->
<!-- row 2: top:426, accent bar color:#60A5FA -->
```

---

### 15. Treemap (트리맵)

순수 HTML — JS 불필요. 비율 기반 너비 계산 후 2개 row로 배치.

**좌표 기준**
```
전체 영역: left:64, top:163, width:1152
Row 1: top:163, height:272
Row 2: top:439 (gap:4px), height:231
블록 간 gap: 4px (left 계산에 반영)
```

**너비 계산 (비율 기반 — 필수)**
```
총 가용 너비 = 1152px (gap 제외한 순수 콘텐츠)
블록 너비 = round(해당 값 / 행 합계 * 1152)
마지막 블록 = 1152 - 앞 블록 합계  (반올림 오차 흡수)

left 계산:
  블록1: left = 64
  블록2: left = 64 + 블록1 너비 + 4(gap)
  블록3: left = 블록2 left + 블록2 너비 + 4(gap)
  ...
```

**색상 (크기 내림차순 파란계열)**
```
1위 (가장 큰): #007BFF  → 흰 텍스트
2위:           #2E8FFF  → 흰 텍스트
3위:           #60A5FA  → 흰 텍스트
4위:           #93C5FD  → 어두운 텍스트 (#1e3a5f)
5위:           #BFDBFE  → 어두운 텍스트
6위:           #DBEAFE  → 어두운 텍스트
7위 (가장 작): #EFF6FF  → 어두운 텍스트 + border:1px solid #DBEAFE
```

**블록 내부 레이아웃**
```
display:flex;flex-direction:column;justify-content:flex-end;padding:16px
하단에: 카테고리명(bold) + 수치·비율(13px)
중앙 배경 퍼센트: 큰 폰트, color:rgba(255,255,255,0.2) — 장식용
```

```html
<!-- Row 1 예시 (3블록) -->
<div style="position:absolute;left:64px;top:163px;width:[A_WIDTH]px;height:272px;background:#007BFF;border-radius:6px;z-index:1;">
  <!-- 중앙 장식 퍼센트 -->
  <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;z-index:2;">
    <p style="font-family:'Noto Sans KR',sans-serif;font-size:56px;font-weight:900;color:rgba(255,255,255,0.2);">33%</p>
  </div>
  <!-- 하단 레이블 -->
  <div style="position:absolute;bottom:0;left:0;right:0;padding:16px;z-index:3;">
    <p style="font-family:'Noto Sans KR',sans-serif;font-size:20px;font-weight:900;color:#FFFFFF;margin-bottom:4px;">카테고리명</p>
    <p style="font-family:'Noto Sans KR',sans-serif;font-size:13px;color:rgba(255,255,255,0.8);">₩XXX억 · XX%</p>
  </div>
</div>
<!-- B: left = 64+A_WIDTH+4 -->
<!-- C: left = B_left+B_WIDTH+4, width = 1216-C_left -->

<!-- Row 2 예시 (4블록, top:439, height:231) -->
```

---

## 색상 팔레트

| 역할 | 값 |
|------|-----|
| Primary blue | `#007BFF` |
| 강조 배경 | `#EEF2FF` |
| 강조 테두리 | `#D0E2FF` |
| 본문 텍스트 | `#333333` |
| 보조 텍스트 | `#555555` |
| 흐린 텍스트 | `#888888` |
| 카드 배경 | `#F8F9FA` |
| 기본 배경 | `#FFFFFF` |

## FontAwesome 아이콘 참고

`fas fa-route` `fas fa-elevator` `fas fa-stairs` `fas fa-bus` `fas fa-robot`
`fas fa-map-marker-alt` `fas fa-chart-bar` `fas fa-code` `fas fa-database`
`fas fa-server` `fas fa-mobile-alt` `fas fa-shield-alt` `fas fa-check-circle`
`fas fa-arrow-down` `fas fa-arrow-right` `fas fa-laptop-code`
