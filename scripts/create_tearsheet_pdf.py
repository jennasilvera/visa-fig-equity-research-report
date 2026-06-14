from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

OUT = Path("tearsheet/Visa_One_Page_Tearsheet.pdf")
OUT.parent.mkdir(exist_ok=True)

doc = SimpleDocTemplate(
    str(OUT),
    pagesize=landscape(letter),
    rightMargin=0.35 * inch,
    leftMargin=0.35 * inch,
    topMargin=0.30 * inch,
    bottomMargin=0.30 * inch,
)

styles = {
    "title": ParagraphStyle(
        "title",
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=21,
        textColor=colors.HexColor("#111827"),
        spaceAfter=6,
    ),
    "subtitle": ParagraphStyle(
        "subtitle",
        fontName="Helvetica",
        fontSize=8.5,
        leading=10,
        textColor=colors.HexColor("#374151"),
        spaceAfter=5,
    ),
    "section": ParagraphStyle(
        "section",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=11,
        textColor=colors.white,
    ),
    "body": ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=7.4,
        leading=9,
        textColor=colors.HexColor("#111827"),
    ),
    "small": ParagraphStyle(
        "small",
        fontName="Helvetica",
        fontSize=6.7,
        leading=8,
        textColor=colors.HexColor("#374151"),
    ),
    "bold": ParagraphStyle(
        "bold",
        fontName="Helvetica-Bold",
        fontSize=7.4,
        leading=9,
        textColor=colors.HexColor("#111827"),
    ),
}

def section_header(text):
    t = Table([[Paragraph(text, styles["section"])]], colWidths=[3.45 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1F2937")),
        ("BOX", (0, 0), (-1, -1), 0.25, colors.HexColor("#1F2937")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t

def simple_table(rows, widths):
    t = Table(rows, colWidths=widths)
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 6.8),
        ("LEADING", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D1D5DB")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E5E7EB")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t

def p(text, style="body"):
    return Paragraph(text, styles[style])

left = []
middle = []
right = []

left.append(section_header("Investment View"))
left.append(Spacer(1, 4))
left.append(p(
    "Visa is a high-quality global payments network with durable secular growth, "
    "strong margins, high free cash flow conversion, limited direct credit risk, "
    "and optionality from value-added services, Visa Direct, tokenization, fraud/risk tools, "
    "and next-generation money movement."
))
left.append(Spacer(1, 6))
left.append(section_header("Variant Perception"))
left.append(Spacer(1, 4))
left.append(p(
    "Consensus understands Visa is a high-quality compounder. The variant view is that "
    "Visa may be evolving from a card-network toll road into a broader trust, risk, "
    "identity, tokenization, and money-movement infrastructure layer."
))
left.append(Spacer(1, 6))
left.append(section_header("Key Drivers"))
left.append(Spacer(1, 4))
left.append(simple_table([
    ["Driver", "Why It Matters"],
    ["Payments Volume", "Main network scale driver"],
    ["Processed Transactions", "Data processing revenue driver"],
    ["Cross-Border Volume", "High-yield international driver"],
    ["Client Incentives", "Pressure point for net revenue yield"],
    ["VAS Growth", "Services-led growth runway"],
    ["Visa Direct", "Non-carded money movement optionality"],
    ["Buybacks", "EPS compounding and capital return"],
], [1.35 * inch, 2.10 * inch]))

middle.append(section_header("Bull / Base / Bear"))
middle.append(Spacer(1, 4))
middle.append(simple_table([
    ["Case", "Thesis"],
    ["Bull", "VAS, Visa Direct, tokenization, and money movement extend growth duration; premium multiple sustained."],
    ["Base", "Durable payments compounder with manageable regulation, resilient margins, and buyback-supported EPS growth."],
    ["Bear", "Regulation, client incentives, alternative rails, and multiple compression pressure returns."],
    ["Severe Downside", "Regulatory shock, macro slowdown, cross-border weakness, and take-rate compression occur together."],
], [0.95 * inch, 2.50 * inch]))
middle.append(Spacer(1, 6))
middle.append(section_header("Valuation Framework"))
middle.append(Spacer(1, 4))
middle.append(p(
    "Primary methods: DCF, forward P/E, EV/EBITDA, FCF yield, historical multiple range, "
    "SOTP, precedent transaction context, and bull/base/bear scenarios."
))
middle.append(Spacer(1, 4))
middle.append(p(
    "Highest weighting should be placed on DCF and forward P/E. Precedent transactions are useful "
    "for payments infrastructure context but should not be the primary valuation anchor for Visa."
))

right.append(section_header("Key Risks"))
right.append(Spacer(1, 4))
right.append(simple_table([
    ["Risk", "Why It Matters"],
    ["Regulation", "Can affect fees, routing, interchange economics, and multiple"],
    ["Client Incentives", "Rising incentives can pressure net revenue yield"],
    ["Alternative Rails", "A2A, RTP, FedNow, PIX, UPI, and stablecoins pressure selected use cases"],
    ["Wallet Steering", "Wallets may preserve Visa credentials or steer to bank funding"],
    ["Cross-Border Slowdown", "High-yield international revenue is cyclical"],
    ["Multiple Compression", "Premium valuation depends on moat confidence"],
], [1.20 * inch, 2.25 * inch]))
right.append(Spacer(1, 6))
right.append(section_header("What Would Change the Thesis"))
right.append(Spacer(1, 4))
right.append(p(
    "- Client incentives rise faster than gross revenue<br/>"
    "- Net revenue yield deteriorates structurally<br/>"
    "- VAS growth slows materially<br/>"
    "- Visa Direct fails to gain traction<br/>"
    "- Alternative rails gain high-value transaction share<br/>"
    "- Regulation directly impairs network economics<br/>"
    "- Visa underperforms Mastercard on growth or services mix",
    "small"
))

title = [
    Paragraph("Visa One-Page Investment Tear Sheet", styles["title"]),
    Paragraph(
        "<b>Visa Inc. (NYSE: V)</b> | Financial Institutions / Payments | "
        "Equity Research / Buy-Side Investment Memo | Recommendation Framework: "
        "<b>Outperform / Positive Base Case</b>",
        styles["subtitle"],
    ),
    Spacer(1, 4),
]

layout = Table(
    [[left, middle, right]],
    colWidths=[3.55 * inch, 3.55 * inch, 3.55 * inch],
)

layout.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
]))

story = title + [layout, Spacer(1, 6), Paragraph(
    "Educational portfolio project only. Not investment advice or a securities recommendation. "
    "All figures and assumptions should be independently verified using current filings, company disclosures, "
    "market data, and regulatory sources.",
    styles["small"],
)]

doc.build(story)
print(f"Created {OUT}")
