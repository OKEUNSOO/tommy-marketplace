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
