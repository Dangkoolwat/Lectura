---
id: concept_hallucination_countermeasures_001
title: 글로벌 AI 업체들의 할루시네이션 대응 방안
type: concept
target: general
difficulty: intermediate
source: LectureP2_Final.pdf
page: 36
tags:
  - 할루시네이션대응
  - RAG
  - 가드레일
  - AI업체전략
relations: {}
education_value: high
interest_level: medium
practice_feasibility: none
reuse_level: high
recommended_duration: 10min
status: active
---

# 글로벌 AI 업체들의 할루시네이션 대응 방안

AI가 혼자 자신 있게 말하지 않도록, 근거, 출처, 검증, 제한 장치를 붙이는 글로벌 전략들입니다.

## 1. 고위험 주제 제한 (주요 AI 업체 공통)
의료, 법률, 금융 등은 안내 문구, 응답 제한, 전문가 확인을 붙입니다.

## 2. RAG / Grounding (Microsoft / Google)
외부 근거에 답변을 연결하여 사실에 기반한 응답을 유도합니다.

## 3. 출처 인용 (OpenAI / Google / Perplexity)
답변에 링크, 문서 번호를 붙여 사용자가 직접 확인하도록 지원합니다.

## 4. 가드레일 / 검증 (Anthropic / Nvidia / Microsoft)
위험한 응답, 근거 없는 주장, 정책 위반 가능성을 별도 장치로 점검합니다.

## 5. 불확실성 인정 학습 (OpenAI / Google / Anthropic)
근거가 부족한 질문에는 억지로 답하지 않고 "확인 필요"를 말하도록 모델을 개선합니다.

> 💡 **핵심**: 사용자는 출처와 근거를 확인하는 시간을 쓰고, 업체는 환각을 줄이기 위해 검색, 출처, 가드레일, 사람 검토 시스템을 운영합니다.
