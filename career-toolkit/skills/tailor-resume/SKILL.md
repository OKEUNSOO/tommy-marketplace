---
name: tailor-resume
description: JD 기반 이력서 맞춤화 — jd-match로 적합도 분석 후 application-writing으로 서류 작성
argument-hint: "[이력서 파일/텍스트] + [JD 파일/URL/텍스트]"
---

JD와 이력서를 받아 다음 순서로 처리한다.

입력: $ARGUMENTS

## 작업 순서

### 1단계: JD 적합도 분석
'jd-match' 스킬을 사용해 JD와 경험 근거를 비교한다.
- JD가 URL이면 먼저 'job-post-markdown'으로 Markdown 변환
- 적합도 요약, 강점, 갭 분석 출력

### 2단계: 서류 작성
'application-writing' 스킬을 사용해 분석 결과 기반으로 이력서 bullet을 재작성한다.
- JD 키워드 정렬
- XYZ+S 공식: "[S 스킬/도구]를 활용해 [Z 방법]으로 [Y 지표] 기준 [X 성과] 달성"
- 근거 없는 수치는 절대 지어내지 않는다 — '보강 필요'로 표시

### 3단계: 결과 저장
맞춤 이력서를 마크다운 파일로 저장한다.

## 두 스킬이 없는 환경에서는 이 스킬이 직접 처리한다.
