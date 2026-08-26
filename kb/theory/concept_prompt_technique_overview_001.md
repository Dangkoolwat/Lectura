---
id: concept_prompt_technique_overview_001
title: 대표 프롬프트 기법 한눈에 보기
type: concept
target: general
difficulty: intermediate
source: LectureP2_Final.pdf
page: 14
tags:
  - 프롬프트기법
  - 분류체계
  - 개요
relations: {}
education_value: high
interest_level: high
practice_feasibility: none
reuse_level: high
recommended_duration: 10min
status: active
---

# 대표 프롬프트 기법 분류 체계

기본 질문부터 전문적인 작업 설계까지, 프롬프트는 점점 구조화됩니다. 처음에는 '구조화된 프롬프트'부터 시작하는 것이 좋습니다.

## 1. 기본 요청
- **Zero-shot**: 예시 없이 바로 요청. 간단한 요약, 번역, 설명에 유용.
- **Role Prompting**: AI에게 역할을 지정. 여행 플래너, 강사, 마케터 관점이 필요할 때.
- **Output Format**: 표, 목록, 체크리스트 등 결과물 형식을 지정.

## 2. 예시와 구조
- **One/Few-shot**: 예시 1개 또는 여러 개를 제공. 말투, 형식, 분류 기준 통일에 유용.
- **Structured Prompt**: 목적, 조건, 형식을 나누어 요청. 업무 문서, 여행 계획, 보고서 초안에 유용.
- **Style/Tone Prompt**: 문체와 톤 지정. 카피, 메일, 블로그 초안에 유용.

## 3. 추론과 작업흐름
- **Critique**: 답변의 문제점과 누락을 검토. 중요한 결정 전 점검에 유용.
- **Ask-before-answer**: 답하기 전 필요한 조건을 먼저 질문. 맞춤형 추천에 유용.
- **Prompt Chaining**: 작업을 여러 단계로 나누어 진행. 조사 → 정리 → 작성 → 검토 흐름에 유용.

## 4. 자료 및 도구 기반
- **Tool-use / Agentic**: 검색, 파일, 표, 이미지 도구 활용. 최신 정보 확인, 계산, 콘텐츠 제작에 유용.
