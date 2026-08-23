from html import escape
from pathlib import Path
import shutil

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Hanbee_Jang_CV.pdf"
BUILD_OUTPUT = ROOT / "tmp" / "pdfs" / "Hanbee_Jang_CV-build.pdf"

PINK = colors.HexColor("#E85F92")
BLUE = colors.HexColor("#315CFF")
INK = colors.HexColor("#17191D")
MUTED = colors.HexColor("#69707A")
LIGHT = colors.HexColor("#D9DDE3")


def register_fonts():
    font_root = ROOT / "node_modules" / "@fontsource-variable" / "instrument-sans" / "files"
    regular = font_root / "instrument-sans-latin-wght-normal.woff2"
    italic = font_root / "instrument-sans-latin-wght-italic.woff2"
    try:
        if regular.exists():
            pdfmetrics.registerFont(TTFont("InstrumentSans", str(regular)))
        if italic.exists():
            pdfmetrics.registerFont(TTFont("InstrumentSansItalic", str(italic)))
    except Exception:
        pass


register_fonts()
BODY_FONT = "InstrumentSans" if "InstrumentSans" in pdfmetrics.getRegisteredFontNames() else "Helvetica"
ITALIC_FONT = (
    "InstrumentSansItalic"
    if "InstrumentSansItalic" in pdfmetrics.getRegisteredFontNames()
    else "Helvetica-Oblique"
)
BOLD_FONT = "Helvetica-Bold"

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="CvName",
        fontName=BOLD_FONT,
        fontSize=24,
        leading=26,
        textColor=INK,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="Kicker",
        fontName=BOLD_FONT,
        fontSize=6.5,
        leading=8,
        textColor=PINK,
        tracking=1.2,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        name="Role",
        fontName=BOLD_FONT,
        fontSize=7.5,
        leading=9,
        textColor=MUTED,
        tracking=0.7,
    )
)
styles.add(
    ParagraphStyle(
        name="Contact",
        fontName=BODY_FONT,
        fontSize=7.5,
        leading=10,
        textColor=MUTED,
        alignment=TA_RIGHT,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        fontName=BOLD_FONT,
        fontSize=6.8,
        leading=8,
        textColor=PINK,
        tracking=0.9,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyCv",
        fontName=BODY_FONT,
        fontSize=9,
        leading=12.4,
        textColor=colors.HexColor("#3F454D"),
    )
)
styles.add(
    ParagraphStyle(
        name="Interest",
        fontName=BOLD_FONT,
        fontSize=7.8,
        leading=10,
        textColor=BLUE,
        spaceBefore=5,
    )
)
styles.add(
    ParagraphStyle(
        name="Period",
        fontName=BODY_FONT,
        fontSize=7.5,
        leading=9.5,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="EntryTitle",
        fontName=BOLD_FONT,
        fontSize=9.4,
        leading=11.2,
        textColor=INK,
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="EntryMeta",
        fontName=BODY_FONT,
        fontSize=7.8,
        leading=10,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="Detail",
        fontName=BODY_FONT,
        fontSize=7.7,
        leading=10.2,
        textColor=MUTED,
        spaceBefore=3,
    )
)
styles.add(
    ParagraphStyle(
        name="PubTitle",
        fontName=BOLD_FONT,
        fontSize=8.7,
        leading=10.8,
        textColor=INK,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="PubMeta",
        fontName=BODY_FONT,
        fontSize=7.5,
        leading=9.8,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="PubVenue",
        fontName=ITALIC_FONT,
        fontSize=7.4,
        leading=9.8,
        textColor=colors.HexColor("#858B94"),
        spaceBefore=1,
    )
)
styles.add(
    ParagraphStyle(
        name="Footer",
        fontName=BODY_FONT,
        fontSize=6.2,
        leading=8,
        textColor=colors.HexColor("#9BA1A9"),
        tracking=0.4,
    )
)


def highlight_name(authors: str) -> str:
    return escape(authors).replace("Hanbee Jang", "<b>Hanbee Jang</b>")


def section(label: str, content):
    table = Table(
        [[Paragraph(label.upper(), styles["Section"]), content]],
        colWidths=[29 * mm, 141 * mm],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return [Spacer(1, 6.2 * mm), table, Spacer(1, 6.2 * mm), HRFlowable(width="100%", thickness=0.5, color=LIGHT)]


def education_block():
    rows = []
    entries = [
        (
            "Sep 2026 - Present",
            "Ph.D. in Industrial Design",
            "KAIST (SketchLab | Advisor: Seok-Hyung Bae)",
            [],
        ),
        (
            "Sep 2024 - Aug 2026",
            "M.S. in Industrial Design",
            "KAIST (SketchLab | Advisor: Seok-Hyung Bae)",
            [
                ("Thesis", "Projectively Aligned Plane Interactions for Interior Architectural Design in VR"),
                ("Committee", "Seok-Hyung Bae | Yiyun Kang | Seung Hyun Cha"),
            ],
        ),
        (
            "Mar 2020 - Aug 2024",
            "B.S. in School of Computing",
            "KAIST (Double Major: Industrial Design)",
            [
                ("Academic", "GPA 3.91 / 4.30 | Magna Cum Laude | Department Rank 9 / 90"),
            ],
        ),
    ]
    for index, (period, degree, institution, details) in enumerate(entries):
        body = [
            Paragraph(escape(degree), styles["EntryTitle"]),
            Paragraph(escape(institution), styles["EntryMeta"]),
        ]
        body.extend(
            Paragraph(
                f'<font color="#858B94" size="6.5"><b>{escape(label.upper())}</b></font>'
                f'&nbsp;&nbsp;{escape(value)}',
                styles["Detail"],
            )
            for label, value in details
        )
        rows.append([Paragraph(period, styles["Period"]), body])
        if index != len(entries) - 1:
            rows.append([Spacer(1, 4.5 * mm), Spacer(1, 4.5 * mm)])
    table = Table(rows, colWidths=[31 * mm, 110 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (0, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return table


def publications_block():
    publications = [
        {
            "title": "Immersive Setup of Autonomous Forklifts in Factories",
            "authors": "Joon Hyub Lee, Sang-Hyun Lee, Hanbee Jang, Siripon Sutthiwanna, Hyelim Hwang, and Seok-Hyung Bae",
            "venue": "UIST 2026 (Poster) | To appear",
        },
        {
            "title": "Projective Walls, Floors, and Windows: Aligned Plane Interactions for Interior Architectural Design in VR",
            "authors": "Hanbee Jang, Seung-Jun Lee, and Seok-Hyung Bae",
            "venue": "UIST 2026 | To appear",
        },
        {
            "title": "Garden of papers: finding, reading, and organizing research papers in a visual, integrated, and flexible workspace.",
            "authors": "Donghyeok Ma, Hanbee Jang, Joon Hyub Lee, and Seok-Hyung Bae",
            "venue": "UIST 2025",
        },
    ]
    rows = []
    for index, publication in enumerate(publications, start=1):
        entry = [
            Paragraph(escape(publication["title"]), styles["PubTitle"]),
            Paragraph(highlight_name(publication["authors"]), styles["PubMeta"]),
            Paragraph(escape(publication["venue"]), styles["PubVenue"]),
        ]
        rows.append([entry])
        if index != len(publications):
            rows.append([Spacer(1, 4 * mm)])
    table = Table(rows, colWidths=[141 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return table


def activities_block():
    items = [
        [
            Paragraph("KAIST School of Computing Student Council", styles["EntryTitle"]),
            Paragraph("ICISTS", styles["EntryTitle"]),
        ],
        [
            Paragraph("Student council member", styles["EntryMeta"]),
            Paragraph("Public Relations", styles["EntryMeta"]),
        ],
    ]
    table = Table(items, colWidths=[70.5 * mm, 70.5 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return table


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setTitle("Hanbee Jang - Curriculum Vitae")
    canvas.setAuthor("Hanbee Jang")
    canvas.setSubject("Academic curriculum vitae")
    canvas.setFont(BODY_FONT, 6.2)
    canvas.setFillColor(colors.HexColor("#9BA1A9"))
    canvas.drawRightString(A4[0] - 17 * mm, 9 * mm, f"{doc.page}")
    canvas.restoreState()


def build_cv():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    BUILD_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(BUILD_OUTPUT),
        pagesize=A4,
        leftMargin=17 * mm,
        rightMargin=17 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
        title="Hanbee Jang - Curriculum Vitae",
        author="Hanbee Jang",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="cv-frame", showBoundary=0)
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=add_page_number)])

    header_left = [
        Paragraph("CURRICULUM VITAE", styles["Kicker"]),
        Paragraph("Hanbee Jang", styles["CvName"]),
        Paragraph("VR | HCI RESEARCHER", styles["Role"]),
    ]
    header_right = Paragraph(
        '<link href="mailto:hanbee.jang@kaist.ac.kr" color="#315CFF">hanbee.jang@kaist.ac.kr</link>',
        styles["Contact"],
    )
    header = Table([[header_left, header_right]], colWidths=[120 * mm, 50 * mm])
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    profile = [
        Paragraph(
            "I study how people perceive, interact, and create in virtual environments, drawing from computer science and industrial design.",
            styles["BodyCv"],
        ),
        Paragraph(
            "Virtual Reality | Human-Computer Interaction | Spatial Computing",
            styles["Interest"],
        ),
    ]

    story = [header, Spacer(1, 7 * mm), HRFlowable(width="100%", thickness=0.7, color=LIGHT)]
    story.extend(section("Profile", profile))
    story.extend(section("Education", education_block()))
    story.extend(section("Publications", publications_block()))
    story.extend(section("Activities", activities_block()))
    story.extend(
        [
            Spacer(1, 4.5 * mm),
            Table(
                [[Paragraph("LAST UPDATED AUGUST 2026", styles["Footer"]), Paragraph("HANBEE JANG | CURRICULUM VITAE", styles["Footer"])]],
                colWidths=[85 * mm, 85 * mm],
                style=TableStyle(
                    [
                        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 0),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                        ("TOPPADDING", (0, 0), (-1, -1), 0),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                    ]
                ),
            ),
        ]
    )

    doc.build(story)
    shutil.copy2(BUILD_OUTPUT, OUTPUT)
    BUILD_OUTPUT.unlink(missing_ok=True)
    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    build_cv()
