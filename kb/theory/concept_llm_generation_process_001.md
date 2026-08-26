---
id: concept_llm_generation_process_001
title: LLM 답변 생성 과정 (사서 비유)
type: concept
target: general
difficulty: beginner
source: LectureP1_Finall_Rev.pdf
page: 14
tags:
  - LLM
  - 답변생성원리
  - 비유
relations: {}
education_value: high
interest_level: high
practice_feasibility: none
reuse_level: high
recommended_duration: 10min
status: active
---

# LLM 답변 생성 과정: 도서관 사서 비유

LLM은 어딘가에 저장된 '정답지'를 그대로 꺼내오는 것이 아닙니다. 질문의 맥락을 보고 가장 자연스러운 답변을 실시간으로 만들어 냅니다. 이를 도서관 사서의 작업에 비유할 수 있습니다.

## 1. 사전 학습 (도서관 책 읽기)
- **사서**: 도서관의 수많은 책을 모두 읽어 지식을 머릿속에 담습니다.
- **LLM**: 방대한 데이터를 사전 학습합니다.

## 2. 문맥 이해 및 관련 정보 연결
- **사서**: 이용자의 질문(예: 여름휴가 계획)을 듣고 핵심과 조건을 파악한 뒤, 머릿속 서가에서 관련 지식들을 연결합니다.
- **LLM**: 토큰 단위로 나뉜 문장의 맥락과 의도를 파악하고, 학습된 지식과 연결합니다.

## 3. 답변 생성 (다음 단어 예측)
- **사서**: 정보를 조합해 이용자에게 자연스러운 말로 차례차례 설명합니다.
- **LLM**: 확률적으로 다음에 올 가능성이 가장 높은 단어를 예측하여 한 단어씩 문장을 이어가며 답변을 완성합니다.

## 🚨 주의할 점 (할루시네이션)
자연스럽게 말을 이어가는 데 특화되어 있다 보니, 확실히 모르는 정보도 그럴듯하게 지어내어 말할 수 있습니다(예: 세종대왕 맥북 던짐 사건). 따라서 사실 확인이 필요한 정보는 반드시 출처 검증이 필요합니다.
