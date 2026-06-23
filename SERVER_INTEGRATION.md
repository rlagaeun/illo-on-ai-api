# 이력서 분석 API 서버 연동 가이드

## 개요

현재 구현된 이력서 분석 기능은 기존 일로온 AI 서버에 연동할 수 있도록 FastAPI Router 형태로 작성되었습니다.

현재 버전은 프론트엔드 화면 연동 및 API 테스트를 위한 하드코딩 응답 버전이며, 추후 Claude 기반 실제 분석 로직으로 교체 예정입니다.

---

## 추가 파일

```text
resume_analysis_router.py
```

---

## main.py 등록

기존 AI 서버 main.py에 아래 코드 추가

```python
from resume_analysis_router import router as resume_analysis_router

app.include_router(resume_analysis_router)
```

---

## 생성 API

### 1. 키워드 점수 분석

```http
POST /api/v1/resume/{user_id}/{resume_id}/analyze/score
```

설명

- 사용자 ID 수신
- 이력서 ID 수신
- 포트폴리오 URL 수신
- 4개 영역 점수 반환

---

### 2. 피드백 분석

```http
POST /api/v1/resume/{user_id}/{resume_id}/analyze/feedback
```

설명

- 사용자 ID 수신
- 이력서 ID 수신
- 포트폴리오 URL 수신
- 피드백 ID 반환
- 5개 평가영역 피드백 반환

---

### 3. 추천활동 생성

```http
POST /api/v1/resume/{user_id}/{resume_id}/analyze/activities
```

설명

- 사용자 ID 수신
- 이력서 ID 수신
- 포트폴리오 URL 수신
- 피드백 ID 반환
- 추천활동 3개 반환

---

## Request Body

현재 백엔드 Resume 생성 API 기준 구조 사용

예시

```json
{
  "title": "이력서",
  "isDefault": true,
  "workExperiences": [],
  "educations": [],
  "awards": [],
  "languages": [],
  "portfolios": [
    {
      "portfolioName": "포트폴리오",
      "url": "https://..."
    }
  ],
  "coverLetter": {
    "content": "자기소개서 내용"
  },
  "certifications": []
}
```

---

## 포트폴리오 URL 처리

현재 구현 내용

- portfolio.url 수신
- URL 존재 여부 확인
- URL 형식 검증
- 정상 수신 여부 반환

응답 예시

```json
{
  "portfolio_received": true,
  "portfolio_count": 1,
  "portfolio_urls": [
    {
      "portfolioName": "포트폴리오",
      "url": "https://..."
    }
  ]
}
```

---

## 현재 하드코딩 상태

현재 아래 데이터는 하드코딩 응답으로 구현되어 있습니다.

### 점수 분석

```python
HARDCODED_SCORE
```

반환 항목

- 스킬
- 경험
- 포트폴리오
- 직무적합성

---

### 피드백 분석

```python
HARDCODED_FEEDBACK
```

반환 항목

- 직무 적합도
- 경험·성과 구체성
- 실무·기술 역량
- 문서 완성도
- 경험 일관성·차별성

---

### 추천활동

```python
HARDCODED_ACTIVITIES
```

반환 항목

- 자격증
- 프로젝트
- 포트폴리오 개선

---

## 추후 구현 예정

현재 하드코딩 부분은 추후 실제 분석 로직으로 교체 예정

### 점수 분석

기존 프로젝트

```text
일로온-이력서키워드점수매칭
```

사용 예정 파일

```text
step01_extract_score_keywords.py
step02_calculate_resume_score.py
```

---

### 피드백 분석

기존 프로젝트

```text
resume-feedback-ai-server
```

사용 예정 파일

```text
step01_extract_evidence.py
step02_evaluate_level.py
step03_1_generate_feedback.py
step03_2_generate_activities.py
```

---

## 필요 환경 변수

추후 실제 Claude 연동 시

```env
ANTHROPIC_API_KEY=
```

등록 필요

---

## 비고

현재 버전은 프론트엔드 연동 및 API 연결 확인 목적의 임시 버전입니다.

실제 분석 로직 연결 시 HARDCODED_SCORE, HARDCODED_FEEDBACK, HARDCODED_ACTIVITIES를 제거하고 Claude 기반 분석 결과를 반환하도록 변경 예정입니다.