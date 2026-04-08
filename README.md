# EnGIS Home

EnGIS(엔지스) 소개용 정적 웹사이트 시안 프로젝트입니다.  
공공·환경·해양 분야의 GIS, DB 구축, 정보시스템 개발, AI 솔루션 역량을 소개하는 마케팅 사이트로 구성되어 있습니다.

## 개요

- 빌드 도구 없이 HTML/CSS/JS만으로 구성된 정적 사이트입니다.
- 메인 페이지와 AI 솔루션 상세 페이지가 분리되어 있습니다.
- 공통 스타일은 단일 `styles.css` 파일에서 관리합니다.
- 최소한의 자바스크립트만 사용하며, 현재는 스크롤 시 헤더 상태 변경만 처리합니다.

## 파일 구조

- `index.html` : 메인 홈페이지
- `ai-solutions.html` : AI 솔루션 상세 페이지
- `projects.html` : 수행실적 상세 페이지
- `styles.css` : 공통 스타일시트
- `app.js` : 헤더 스크롤 상태 처리
- `assets/` : 로고 SVG 등 정적 에셋
- `decks/` : 영업/제안/설명용 보조 HTML 자료
- `docs/` : 기획/분석 문서
- `backups/` : 이전 백업본
- `CLAUDE.md` : 작업 가이드 문서

## 실행 방법

별도 설치 과정은 없습니다. 정적 파일 서버로 바로 실행하면 됩니다.

```bash
python3 -m http.server 8009
```

브라우저에서 아래 주소로 접속합니다.

```text
http://localhost:8009
```

다른 예시:

```bash
python3 -m http.server 8080
```

## 주요 페이지

### 1. 메인 페이지

`index.html`에는 다음 섹션이 포함됩니다.

- Hero
- 신뢰 요소
- 핵심 서비스
- AI 솔루션 요약
- 구축 사례
- 강점
- 문의 CTA

### 2. AI 솔루션 상세 페이지

`ai-solutions.html`에는 다음 제품 소개가 포함됩니다.

- `ENGIS Knowledge`
- `ENGIS Insight`
- `ENGIS Vision`

### 3. 수행실적 페이지

`projects.html`에는 다음 내용이 포함됩니다.

- 주요 수행 기관
- 대표 프로젝트
- 도메인별 경험
- 운영/유지관리 강점

### 4. 보조 자료 페이지

제안서형 또는 설명용 자료는 `decks/` 폴더에 별도 HTML로 관리합니다.

예시:

- `decks/engis_capability_deck.html`
- `decks/engis_solution_deck.html`
- `decks/mathai_misconception_platform_ui.html`
- `decks/mathai_teacher_dashboard.html`
- `decks/khoa_dt_report_mockup.html`
- `decks/haeyang-lite-dt-report.html`
- `decks/dt_01/index.html`

## 개발 메모

### 자료 페이지 운영 방식

- 메인 페이지 구조는 가능하면 안정적으로 유지합니다.
- 영업/제안/설명용 자료는 메인에 직접 넣기보다 `decks/` 아래 별도 HTML로 관리합니다.
- 필요할 때만 메인 `서비스` 영역이나 관련 페이지에서 링크를 노출합니다.
- 더 이상 노출이 필요 없으면 링크만 제거하고 파일은 보관할 수 있습니다.

### CSS 캐시 버전 관리

`styles.css`는 캐시 방지를 위해 쿼리 문자열 버전을 붙여 참조합니다.

예시:

```html
<link rel="stylesheet" href="./styles.css?v=20260327-4" />
```

`styles.css`를 수정한 뒤 실제 기기에서 변경이 반영되지 않으면:

1. `index.html`의 CSS 버전을 올립니다.
2. `ai-solutions.html`의 CSS 버전을 같은 값으로 올립니다.

## 스타일 원칙

- 색상, 표면, 그림자 값은 `:root`의 CSS 변수에서 관리합니다.
- 본문은 `Pretendard` 중심, 헤드라인/영문 라벨은 `Montserrat`를 사용합니다.
- 공통 헤더 구조는 `index.html`과 `ai-solutions.html` 양쪽에 동일하게 반영해야 합니다.
- 사용자 노출 텍스트는 주로 한국어이며, 제품명/섹션 키커에는 영어가 혼용됩니다.

## 참고 문서

- [docs/plan.md](/home/engis/projects/engis-home/docs/plan.md)
- [docs/solution.md](/home/engis/projects/engis-home/docs/solution.md)
- [docs/chatbot.md](/home/engis/projects/engis-home/docs/chatbot.md)

## 주의 사항

- 현재 프로젝트에는 빌드 시스템이나 패키지 매니저가 없습니다.
- 헤더/로고 변경은 두 HTML 파일 모두 확인해야 합니다.
- 모바일/태블릿 테스트 시 브라우저 캐시 영향이 있을 수 있으므로 CSS 버전 관리가 중요합니다.
