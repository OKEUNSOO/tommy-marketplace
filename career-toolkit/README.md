# career-toolkit

한국어 커리어 지원 워크플로우 툴킷.

JD 파싱부터 경험 DB 관리, 적합도 분석, 서류 작성, 회사 조사, 면접 준비까지 취업/이직 전 과정을 하나의 스킬 세트로 커버합니다.

## 스킬 목록

| 스킬 | 역할 |
|------|------|
| `career-workspace` | 전체 워크플로우 라우팅 허브 |
| `job-post-markdown` | 채용공고 URL → Markdown 변환 |
| `career-experience-db` | 로컬 경험 근거 노트 관리 및 JD 매칭 컨텍스트 생성 |
| `jd-match` | JD vs 경험 적합도 분석, 갭 분석 |
| `application-writing` | 이력서 bullet, 자기소개서, 1분 자기소개, STAR 답변 작성 |
| `company-research` | 회사 조사, 지원동기 전략화 |
| `tailor-resume` | JD 기반 이력서 맞춤화 (jd-match + application-writing 통합) |
| `review-resume` | 이력서 리뷰 (일반 / JD 기반 / 근거 수치 검증) |
| `proofread` | 한국어 문서 교정 |
| `interview-prep` | 면접 준비 — JD 분석, 예상 질문, STAR 답변, 모의면접 |

## 사전 설정

Python 스크립트 기반 스킬(`career-experience-db`, `jd-match`, `application-writing`, `job-post-markdown`)은 로컬 `career-notes/` 폴더가 필요합니다.

권장 폴더 구조:

```
career-notes/
├── 01_경험/   # 프로젝트, 인턴, 교육 경험 원본 노트
├── 02_서류/   # 이력서, 포트폴리오, 자소서 소재
└── 03_지원/   # 회사별 지원 패키지와 채용공고
```

스크립트 없이도 모든 스킬은 Claude가 직접 분석해서 동작합니다. 스크립트는 반복 작업을 자동화하는 선택적 도구입니다.

## 핵심 원칙

- 커리어 근거 노트가 source of truth
- 근거 없는 수치, 기간, 기여도는 만들지 않음
- 부족한 근거는 `보강 필요`로 표시
- 기본 출력 언어: 한국어

## 일반적인 작업 흐름

```
채용공고 URL 입력
  → job-post-markdown (Markdown 변환)
  → jd-match (적합도 분석)
  → application-writing (서류 작성)
  → company-research (회사 조사 + 지원동기)
  → interview-prep (면접 준비)
```
