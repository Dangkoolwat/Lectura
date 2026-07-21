# Lectura 에이전트 행동 규칙 (v5.0 - Policy Router)

Lectura는 발표자, 교육자, 지식 생산자와 협력하여 지식 자산을 설계하고 발표용 슬라이드를 제작하는 시스템입니다. 본 파일은 얇은 라우팅 레이어로 동작하며, 세부 업무 시 지연 로딩(Lazy-Loading) 정책을 수범합니다.

---

## 0. 핵심 3원칙 & 통합 정책 라우팅 (Policy Router)

> **Scenario Plan = 내용의 기준** | **design.md = 표현의 기준** | **Slide Model = HTML과 PPT의 공통 원본**

### 필수 정책 지연 로딩 표 (Lazy-Loading Policy Table)
작업 트리거 발생 시 아래 링크된 정책 전용 문서를 지연 로딩하여 엄수합니다.

| 작업 영역 / 트리거 조건 | 필수 참조 지연 로딩 정책 문서 |
| :--- | :--- |
| **슬라이드 화면 설계 / design.md 12항목 / Slide Model 13대 스키마** | [슬라이드 디자인 표준 명세](docs/agent-policy/slide-design-spec.md) |
| **원본 자산 수납 / decompose.py / 아카이빙 / 파이썬 venv 셋업** | [지식 마이닝 및 파이프라인 규칙](docs/agent-policy/decomposition-workflow.md) |
| **4단계 탐색 계층 / serena & CRG 툴 / Flash 모델 Sequential Thinking** | [계층적 도구 탐색 및 토큰 절약 규격](docs/agent-policy/tooling-efficiency.md) |

---

## 1. 지식 관리 & 탐색 원칙

- **저장 구조**: 모든 교육 자산은 `kb/` 하위 규격 폴더 (`theory/`, `practice/`, `tips/`, `meta/`)에 조각 단위 적재.
- **토큰 최적화 탐색**: `kb/` 내 개별 마크다운 파일 다중 열람 금지. 1차로 `kb/index.json` 및 `kb/graph.json` 경량 인덱스를 조회 후, 필요한 자산만 핀포인트 선택 열람(Surgical Read). 자산 추가/수정 후 `python scripts/build_kb_graph.py` 실행 필수.

---

## 2. 2단계 파이프라인 요약

1. **STAGE 1 (Lecture Plan)**: 강사 대화를 통해 `outputs/latest/lecture_plan.md` 확정. *(슬라이드 규격 언급 금지)*
2. **STAGE 2 (Slide Production)**: 확정된 `lecture_plan.md`와 `design.md`를 입력받아 `outputs/latest/slide_model.json` 동적 설계 및 Python 렌더링.

---

## 3. 역할 경계 & Sequential Thinking

| 주체 | 핵심 역할 |
| :--- | :--- |
| **강사** | Lecture Plan 확정, HTML 미리보기 검토, 최종 PPT/PDF 빌드 승인 |
| **LLM** | Stage 1 대화형 강의안 작성, Stage 2 슬라이드 화면 구조 설계 (`slide_model.json`) |
| **Python** | Slide Model 정형화, HTML/PPT/PDF 렌더링, `design.md` 파싱, 파이프라인 마이닝 |

- **Flash 모델 추론 규칙**: Gemini Flash 사용 시 패스트 트랙(단순 Q&A) 제외 모든 파일 변경/설계 작업 전 `sequentialthinking` 최소 3단계 필수 실행.
- **Fail Fast (PoC 최우선 검증)**: 대규모 구현이나 파일 수정으로 바로 넘어가지 않고, 핵심 로직(파일럿)을 먼저 제안하고 소규모 검증(PoC) 후 확장한다.

---

## 4. 핵심 산출물 & 정합성 검증

- **산출물 위치**: `outputs/latest/` (최신 고정본) 및 `outputs/YYYY-MM-DD-MMSS-Model명/` (실행별 고유본).
- **Stage 2 렌더링 조건**: `slide_model.json` 생성 완료 및 `python scripts/validate_slide_design.py` PASS 필수.
- **정합성 검증 조건**: 지식 자산 생성/수정 직후 `python scripts/validate.py` 100% PASS (Errors 0, Warnings 0) 필수.

---

## 5. 엄격 금지 사항 & 시크릿 보안 (Strict Prohibition & Secret Scan)

1. **시크릿 하드코딩 금지 및 사전 스캔 의무화**: API Key(`nvapi-`, `sk-`, `AIzaSy` 등), 인증 토큰, 비밀번호를 소스 코드 및 문서에 하드코딩하는 행위 절대 금지. `git commit` 및 `git push` 실행 전 시크릿 포함 여부 100% 사전 스캔 필수. 반드시 환경변수(`os.getenv()`)로 처리. 실제 시크릿이 담긴 `.env` 파일의 내용 열람 및 콘솔 출력 금지 (템플릿용 `.env.example` 생성은 허용).
2. **Git Hygiene (버저닝 쓰레기 생성 금지) 강제**: `_v2`, `_fix` 같은 버저닝 사본 파일 생성을 엄금. 로직 꼬임 시 임시방편 덧대기를 금지하고 즉시 `git reset`으로 롤백한다.
3. 강사 명시적 허락 없는 `git commit`/`git push` 및 최종 빌드(PPT/PDF) 생성 절대 금지.
4. Lecture Plan 미확정 상태의 슬라이드 설계 진행 절대 금지.
5. **Anti-Sycophancy (순환논리 차단)**: 근거 없는 칭찬이나 사용자의 말을 앵무새처럼 되풀이하는 순환논리를 엄격히 차단한다. 검증할 수 없는 판단은 명확히 "확인 불가"로 표기한다.
