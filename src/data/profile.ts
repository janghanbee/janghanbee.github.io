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
  figure?: string;
  figureAlt?: string;
  note?: string;
  links?: Link[];
};

export type Mode = {
  id: string;
  icon: string;
  photo: string;
  photoAlt: string;
  caption: string;
  label: string;
  status: string;
};

export const profile = {
  name: "Hanbee Jang",
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
      title: "Immersive Setup of Autonomous Forklifts in Factories",
      authors: "Joon Hyub Lee, Sang-Hyun Lee, Hanbee Jang, Siripon Sutthiwanna, Hyelim Hwang, and Seok-Hyung Bae",
      venue: "UIST 2026 Poster",
      note: "To appear",
    },
    {
      year: "2026",
      figure: "/publication-figures/2026_uist_pwfw.png",
      title: "Projective Walls, Floors, and Windows: Aligned Plane Interactions for Interior Architectural Design in VR",
      authors: "Hanbee Jang, Seung-Jun Lee, and Seok-Hyung Bae",
      venue: "UIST 2026 Paper",
      note: "To appear",
    },
    {
      year: "2025",
      figure: "/publication-figures/2025_uist_garden_of_papers_1.jpg",
      title: "Garden of papers: finding, reading, and organizing research papers in a visual, integrated, and flexible workspace.",
      authors: "Donghyeok Ma, Hanbee Jang, Joon Hyub Lee, and Seok-Hyung Bae",
      venue: "UIST 2025 Paper",
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
      id: "research",
      icon: "🥽",
      photo: "/website_photo_1.webp",
      photoAlt: "Hanbee Jang in research mode",
      caption: "deep in my VR world\u00A0✦",
      label: "Research mode",
      status: "Exploring embodied interaction in virtual worlds.",
    },
    {
      id: "travel",
      icon: "✈️",
      photo: "/website_photo_3.webp",
      photoAlt: "Hanbee Jang in travel mode",
      caption: "hello, Matterhorn!\u00A0✦",
      label: "Travel mode",
      status: "Collecting new places, systems, and perspectives.",
    },
    {
      id: "piano",
      icon: "🎹",
      photo: "/website_photo_2.webp",
      photoAlt: "Hanbee Jang in piano mode",
      caption: "keys, lights, action!\u00A0✦",
      label: "Piano mode",
      status: "Practicing one measure at a time.",
    },
    {
      id: "baseball",
      icon: "⚾",
      photo: "/website_photo_5.webp",
      photoAlt: "Hanbee Jang enjoying baseball",
      caption: "we lost, still smiling\u00A0✦",
      label: "Baseball mode",
      status: "Waiting for the first pitch.",
    },
    {
      id: "running",
      icon: "🏃",
      photo: "/website_photo_4.webp",
      photoAlt: "Hanbee Jang in running mode",
      caption: "10K, done and happy\u00A0✦",
      label: "Run mode",
      status: "Out for a steady run.",
    },
  ] satisfies Mode[],
};
