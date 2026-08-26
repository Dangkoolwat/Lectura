---
id: concept_context_drift_001
title: 대화가 길어지면 AI가 깜빡하는 이유 (Context Drift)
type: concept
target: general
difficulty: intermediate
source: LectureP2_Final.pdf
page: 5
tags:
  - 컨텍스트드리프트
  - 멀티턴대화
  - AI한계
relations: {}
education_value: high
interest_level: high
practice_feasibility: none
reuse_level: high
recommended_duration: 5min
status: active
---

# 대화가 길어지면 AI가 깜빡하는 이유

AI는 고쳐달라고 했는데 자꾸 처음 조건을 잊어버리는 것처럼 보일 때가 있습니다. 이것은 AI가 일부러 딴소리를 하는 것이 아니라, 대화가 길어지면서 처음의 맥락이 희석되는 **맥락 드리프트(Context Drift)** 현상입니다.

## 잘 생기는 상황
1. **대화가 길어질 때**: 처음 조건이 흐려지고 최근 말이 더 강해질 수 있습니다.
2. **수정 요청이 반복될 때**: 전체 목표보다 방금 고친 문장에만 반응할 수 있습니다.
3. **주제가 바뀔 때**: 이전 작업의 말투와 조건이 새 작업에 섞일 수 있습니다.

## 해결법
- **1대화방 = 1태스크**: 여행 계획, 보고서, 이미지 제작을 나눠서 진행합니다.
- **새 대화로 시작**: 새 목표와 조건을 다시 적습니다.
- **이어갈 때는 전환 선언**: "이전 주제는 잊고, 지금부터는 여행 계획만 다뤄 줘"
