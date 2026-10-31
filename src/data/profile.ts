export type Link = {
  label: string;
  href: string;
};

export type Education = {
  degree: string;
  field: string;
  institution: string;
  period: string;
  affiliation?: string;
  lab?: Link;
  advisor?: Link;
  note?: string;
  details?: {
    label: string;
    value?: string;
    links?: Link[];
  }[];
};

export type Publication = {
  year: string;
  title: string;
  authors: string;
  venue: string;
  path?: string;
  figure?: string;
  figureAlt?: string;
  note?: string;
  links?: Link[];
};

export type Mode = {
  id: string;
  icon: string;
  cardLabel: string;
  photo: string;
  photoAlt: string;
  caption: string;
  label: string;
  status: string;
};

export const profile = {
  name: "Hanbee Jang",
  portrait: "/profile-photo.webp",
  portraitAlt: "Portrait of Hanbee Jang",
  authorAliases: ["Jang, Hanbee"],
  nameKo: "",
  role: "HCI Researcher",
  email: "hanbee.jang@kaist.ac.kr",
  intro:
    "I’m a designer reimagining how we create and experience space. I explore immersive tools for imagining, shaping, and sharing worlds of our own.",
  interests: ["Virtual Reality", "Human–Computer Interaction", "Spatial Computing"],
  education: [
    {
      degree: "Ph.D.",
      field: "Industrial Design",
      institution: "KAIST",
      period: "Sep 2026 — Present",
      lab: { label: "SketchLab", href: "https://sketch.kaist.ac.kr/" },
      advisor: { label: "Seok-Hyung Bae", href: "https://sketch.kaist.ac.kr/people/seokhyungbae" },
    },
    {
      degree: "M.S.",
      field: "Industrial Design",
      institution: "KAIST",
      period: "Sep 2024 — Aug 2026",
      lab: { label: "SketchLab", href: "https://sketch.kaist.ac.kr/" },
      advisor: { label: "Seok-Hyung Bae", href: "https://sketch.kaist.ac.kr/people/seokhyungbae" },
      details: [
        {
          label: "Thesis",
          value: "Projectively Aligned Plane Interactions for Interior Architectural Design in VR",
        },
        {
          label: "Committee",
          links: [
            { label: "Seok-Hyung Bae", href: "https://sketch.kaist.ac.kr/people/seokhyungbae" },
            { label: "Yiyun Kang", href: "https://www.yiyunkang.com/" },
            { label: "Seung Hyun Cha", href: "https://fsl.kaist.ac.kr/MEMBERS_Director" },
          ],
        },
      ],
    },
    {
      degree: "B.S.",
      field: "School of Computing",
      institution: "KAIST",
      period: "Mar 2020 — Aug 2024",
      affiliation: "Double Major: Industrial Design",
      details: [
        {
          label: "Academic",
          value: "GPA 3.91 / 4.30 (Magna Cum Laude, Department Rank 9 / 90)",
        },
        {
          label: "Activities",
          value: "School of Computing Student Council, ICISTS (Public Relations)",
        },
      ],
    },
  ] satisfies Education[],
  publications: [
    {
      year: "2026",
      figure: "/publication-figures/2026_uist_poster_afl.png",
      figureAlt: "Representative figure for Immersive Setup of Autonomous Forklifts in Factories",
      title: "Immersive Setup of Autonomous Forklifts in Factories",
      authors: "Joon Hyub Lee, Sang-Hyun Lee, Hanbee Jang, Siripon Sutthiwanna, Hyelim Hwang, and Seok-Hyung Bae",
      venue: "UIST 2026 Poster",
      note: "To appear",
    },
    {
      year: "2026",
      figure: "/publication-figures/2026_uist_pwfw.png",
      figureAlt: "Representative figure showing aligned plane interactions for interior architectural design in VR",
      title: "Projective Walls, Floors, and Windows: Aligned Plane Interactions for Interior Architectural Design in VR",
      authors: "Hanbee Jang, Seung-Jun Lee, and Seok-Hyung Bae",
      venue: "UIST 2026",
      note: "To appear",
    },
    {
      year: "2025",
      figure: "/publication-figures/2025_uist_garden_of_papers_1.jpg",
      figureAlt: "Representative figure for Garden of Papers",
      title: "Garden of papers: finding, reading, and organizing research papers in a visual, integrated, and flexible workspace.",
      authors: "Donghyeok Ma, Hanbee Jang, Joon Hyub Lee, and Seok-Hyung Bae",
      venue: "UIST 2025",
      links: [
        { label: "DOI", href: "https://dl.acm.org/doi/full/10.1145/3746059.3747637" },
      ],
    },
  ] satisfies Publication[],
  links: [
    { label: "LinkedIn", href: "https://www.linkedin.com/in/janghanbee/" },
    { label: "GitHub", href: "https://github.com/janghanbee" },
    { label: "Instagram", href: "https://www.instagram.com/janghanbee/" },
  ] satisfies Link[],
  modes: [
    {
      id: "daily",
      icon: "✦",
      cardLabel: "DAILY",
      photo: "/website_photo_lab.webp",
      photoAlt: "Hanbee Jang smiling at her desk in SketchLab",
      caption: "an ordinary day at SketchLab\u00A0✦",
      label: "Daily life",
      status: "Working from my favorite corner of the lab.",
    },
    {
      id: "research",
      icon: "🥽",
      cardLabel: "VR",
      photo: "/website_photo_1.webp",
      photoAlt: "Hanbee Jang in research mode",
      caption: "testing my VR prototype\u00A0✦",
      label: "VR research",
      status: "Exploring embodied interaction in virtual worlds.",
    },
    {
      id: "travel",
      icon: "✈️",
      cardLabel: "TRAVEL",
      photo: "/website_photo_3.webp",
      photoAlt: "Hanbee Jang in travel mode",
      caption: "meeting the Matterhorn\u00A0✦",
      label: "Travel",
      status: "Collecting new places, systems, and perspectives.",
    },
    {
      id: "piano",
      icon: "🎹",
      cardLabel: "KEYS",
      photo: "/website_photo_2.webp",
      photoAlt: "Hanbee Jang in piano mode",
      caption: "playing keys with the band\u00A0✦",
      label: "Keys",
      status: "Practicing one measure at a time.",
    },
    {
      id: "running",
      icon: "🏃",
      cardLabel: "RUN",
      photo: "/website_photo_4.webp",
      photoAlt: "Hanbee Jang after finishing a half marathon",
      caption: "half marathon finisher\u00A0✦",
      label: "Running",
      status: "Half marathon finisher.",
    },
  ] satisfies Mode[],
};
