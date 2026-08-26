---
id: practice_structured_prompt_001
title: 구조화된 프롬프트 작성 실습
type: practice
target: general
difficulty: intermediate
source: LectureP2_Final.pdf
page: 15
tags:
  - 프롬프트작성
  - 구조화
  - 기본실습
relations: {}
education_value: high
interest_level: high
practice_feasibility: easy
reuse_level: high
recommended_duration: 15min
status: active
---

# 구조화된 프롬프트 작성 실습

그냥 질문하면 답변이 넓고 흐려지고, 원하는 형식이 안 나오고, 중요 조건이 빠지고, 다시 수정하는 시간이 늘어납니다. 프롬프트 기법을 쓰면 역할과 목적이 선명해지고, 조건과 기준이 보이고, 출력 형식을 맞추기 쉬워집니다.

## 구조화 5요소

### 1. 역할 (Role)
AI가 어떤 전문가 관점으로 답할지 지정합니다.

### 2. 배경 (Context)
현재 상황과 맥락을 설명합니다.

### 3. 목적 (Task)
무엇을 해달라는 것인지 명확히 합니다.

### 4. 조건 (Constraints)
예산, 기간, 대상, 제외할 항목 등을 붙입니다.

### 5. 출력 형식 (Format)
표, 체크리스트, 요약 등 결과물의 모양을 정합니다.

## 실습 예시
```text
너는 10년 경력의 여행 플래너야.
나는 바쁜 직장인이고 7월 중 2박 3일 힐링 여행을 계획 중이야.
예산은 1인당 60만 원 이내, 대중교통 중심으로 이동하고 싶어.
너무 빡빡한 일정은 피하고, 휴식과 맛집 방문을 적절히 섞어 줘.
바로 계획을 만들기 전에, 나에게 먼저 확인해야 할 질문 5개를 해 줘.
내가 답변하면 그 내용을 바탕으로 여행 계획을 작성해 줘.
```
