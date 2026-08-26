---
id: concept_transformer_001
title: Transformer와 어텐션(Attention)
type: concept
target: general
difficulty: advanced
source: LectureP1_Finall_Rev.pdf
page: 10
tags:
  - 트랜스포머
  - 어텐션
  - 언어이해
relations: {}
education_value: high
interest_level: high
practice_feasibility: none
reuse_level: high
recommended_duration: 10min
status: active
---

# Transformer의 등장과 어텐션 메커니즘

## 1. Transformer (2017)
- **개념**: 단어를 앞에서부터 하나씩 순서대로 읽던 기존 방식의 한계를 넘어, **문장 속 단어들의 관계를 '한꺼번에 동시에' 계산**하는 혁신적인 구조입니다.
- **의의**: 긴 맥락 보존과 병렬 처리가 가능해지면서, 오늘날의 대규모 언어 모델(LLM)이 긴 문장을 이해하고 자연스럽게 답변할 수 있게 한 핵심 기반 기술입니다.

## 2. Attention (어텐션) 메커니즘
- **개념**: 문장 전체를 볼 때 모든 단어에 똑같은 비중을 두는 것이 아니라, 질문 속 핵심 조건이나 중요한 정보에 **더 큰 가중치(집중력)**를 부여하는 방식입니다.
- **비유**: 마치 표를 읽을 때 내가 관심 있는 특정 항목(예: 예산 40만 원, 덜 붐비는 곳)에 형광펜을 칠하고 그 부분과 연관된 정보(여행지)를 더 유심히 살펴보는 것과 같은 원리입니다.
