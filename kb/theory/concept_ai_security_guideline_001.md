---
id: concept_ai_security_guideline_001
title: AI 입력 정보 신호등 (보안 및 민감정보)
type: concept
target: general
difficulty: beginner
source: LectureP4_Final.pdf
page: 25
tags:
  - AI보안
  - 데이터보안
  - 민감정보가이드
relations: {}
education_value: high
interest_level: medium
practice_feasibility: none
reuse_level: high
recommended_duration: 5min
status: active
---

# AI 입력 정보 신호등: "밖으로 나가도 되는 정보인가?"

AI 모델(특히 클라우드 기반 LLM)에 데이터를 입력할 때는 반드시 보안 등급을 스스로 판단해야 합니다.

## 🟢 초록불 (입력 가능 / 공개 가능 정보)
- **대상**: 공개된 여행 정보, 뉴스, 제품 설명, 이미 공개된 강의/정책 자료
- **활용**: 일반적인 정보의 정리, 요약, 초안 작성에 자유롭게 활용 가능합니다.

## 🟡 노란불 (활용 주의 / 개인·업무 민감정보)
- **대상**: 개인의 구체적 일정, 가족/지인 이야기, 회사 업무 초안, 상담 내용, 공개 전 보고서
- **활용 방안**: 통째로 복사해서 넣지 말고, 필요한 부분만 최소한으로 입력하거나 핵심 키워드는 **마스킹(A회사, B프로젝트 등 비식별 처리)** 후 승인된 환경에서만 활용해야 합니다.

## 🔴 빨간불 (입력 절대 금지 / 유출 위험·기밀 정보)
- **대상**: 주민등록번호, 계좌/카드번호, 비밀번호/인증번호, 계약서 원문, 병원 진료 기록, 타인의 개인정보, 감사/인사/징계 자료, 안보/수사 기밀
- **원칙**: 일반 상용 AI(ChatGPT, Gemini 등) 프롬프트 창에 **절대 입력해서는 안 됩니다**.
