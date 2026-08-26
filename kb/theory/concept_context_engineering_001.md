---
id: concept_context_engineering_001
title: Context Engineering (맥락 설계)
type: concept
target: general
difficulty: advanced
source: LectureP2_Final_ADV_PROMPT.pdf
page: 14
tags:
  - 프롬프트기법
  - AI작업설계
  - 맥락제한
relations: {}
education_value: high
interest_level: medium
practice_feasibility: easy
reuse_level: high
recommended_duration: 10min
status: active
---

# Context Engineering (맥락 및 환경 설계)

## 개념
단순히 질문 한 줄을 잘 쓰는 프롬프트 엔지니어링을 넘어, AI가 참고할 **자료, 규칙, 대화 흐름**을 하나의 통제된 맥락으로 설계하는 기법입니다. AI의 환각(Hallucination)을 막고 답변의 신뢰도를 극대화할 수 있습니다.

## 핵심 구성 요소
- **자료**: PDF, 회의록, 강의안, 표 등 구체적 데이터 제공
- **규칙**: 역할 지정, 금지 사항, 확인 필요 표시 등 제약 조건
- **대화**: 이전 조건 기억, 수정 사항 반영 등 맥락 유지

## 프롬프트 예시
> "첨부한 강의안과 프로젝트 지침만 기준으로 답변해 줘. 자료에 없는 내용은 절대 추측하지 말고 '확인 필요'로 표시해 줘."
