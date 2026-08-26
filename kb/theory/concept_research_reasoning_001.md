---
id: concept_research_reasoning_001
title: AI 연구형 추론 기법 (CoT, ToT, GoT)
type: concept
target: expert
difficulty: advanced
source: LectureP2_Final_ADV_PROMPT.pdf
page: 16
tags:
  - 프롬프트기법
  - 논리추론
  - 심화개념
relations: {}
education_value: medium
interest_level: high
practice_feasibility: hard
reuse_level: medium
recommended_duration: 10min
status: active
---

# 알아두면 좋은 AI 연구형 추론 기법

실무에서 매번 쓰지는 않지만, 최신 AI 연구에서 발전하고 있는 대표적인 고급 추론 프롬프트 기법 4가지입니다.

## 1. Chain of Thought (CoT)
- **개념**: 중간 사고 과정을 단계별로 전개하며 추론하도록 유도합니다.
- **예시**: "답을 바로 내지 말고, 계산 과정을 단계별로 자세히 설명해 줘."

## 2. Tree of Thought (ToT)
- **개념**: 하나의 답을 바로 고르지 않고 여러 선택지(가지)를 나누어 탐색합니다.
- **예시**: "이 문제를 해결할 수 있는 방법 3가지를 도출하고, 각각의 장단점을 비교한 뒤 최적의 하나를 선택해 줘."

## 3. Graph of Thought (GoT)
- **개념**: 생각을 선형(직선)이 아니라 복잡한 네트워크(그래프)처럼 연결하며 입체적으로 추론합니다. 복잡한 인과관계 분석에 유용합니다.

## 4. Self-Consistency
- **개념**: 한 번만 묻는 것이 아니라 여러 번(또는 여러 방식)으로 추론하게 한 뒤, 가장 일관되게 도출된 답을 최종 선택하게 합니다. 정확도를 극대화할 때 씁니다.
