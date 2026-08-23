# Researcher Portfolio

Astro로 만든 미니멀한 개인 연구자 웹사이트 템플릿입니다.

## 시작하기

```bash
npm install
npm run dev
```

브라우저에서 `http://localhost:4321`을 엽니다.

배포용 파일은 다음 명령으로 생성합니다.

```bash
npm run build
```

## CV

CV는 현재 배포에서 제외되어 있습니다. 웹 CV 초안은 `src/drafts/cv.astro`, PDF 원본은 `output/pdf/Hanbee_Jang_CV.pdf`에 보관됩니다.

PDF를 다시 생성하려면 다음 명령을 실행하세요.

```bash
npm run cv:pdf
```

생성 스크립트는 `scripts/generate_cv.py`에 있으며, 생성된 PDF는 공개 `public` 폴더로 복사되지 않습니다.

## 내 정보로 바꾸기

대부분의 텍스트와 링크는 `src/data/profile.ts` 한 파일에서 수정할 수 있습니다.

- `name`, `nameKo`: 영문·한글 이름
- `authorAliases`: 논문 저자 표기에 쓰이는 다른 이름 형식. `name`과 함께 자동 강조됩니다.
- `role`, `intro`, `interests`: 소개와 연구 분야
- `education`: 학사·석사 정보. `details`에 Thesis, Committee, GPA, Activities 같은 세부 정보를 추가할 수 있습니다.
- `publications`: 논문 목록과 링크. `figure`, `figureAlt`를 추가하면 번호와 제목 사이에 대표 피겨가 표시됩니다.
- `email`, `links`: 이메일, LinkedIn, Google Scholar, ORCID
- `photo`, `photoAlt`: 기본 프로필 사진과 대체 텍스트
- `modes`: 상단의 다섯 사진, 이모지, 사진별 `caption`과 모드 색상

상단에는 4:3 비율의 모드 사진과 현재 모드 이모지가 표시됩니다. 사진 모서리의 이모지를 누르면 다섯 사진이 순서대로 바뀝니다. 현재는 이미지가 깨지지 않도록 모든 모드에 같은 기본 사진을 연결해 두었으며, 각 `photo` 경로를 원하는 사진으로 교체하면 됩니다.

모드별 이모지는 `src/data/profile.ts`에서 변경할 수 있습니다.

```ts
icon: "🥽",
photo: "/photos/research.jpg",
photoAlt: "Hanbee Jang in research mode",
caption: "building tiny worlds ✦",
```

논문 대표 피겨는 `public` 폴더 안에 넣고 각 논문에 경로를 추가하세요. 피겨를 지정하지 않으면 `FIG.01` 형태의 자리표시자가 나타납니다.

```ts
figure: "/publication-figures/my-paper.png",
figureAlt: "Representative figure showing the study setup",
```

## 사이트 주소 설정

`astro.config.mjs`의 `site` 값을 실제 도메인으로 변경하세요.

```js
site: "https://your-domain.com",
```
