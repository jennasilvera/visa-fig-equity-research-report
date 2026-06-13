from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from pathlib import Path

out = Path("model/Visa_Institutional_Model_v2.xlsx")

tabs = [
    "01_Cover",
    "02_Sources",
    "03_Setup_Control",
    "04_Historical_Financials",
    "05_KPI_History",
    "06_Revenue_Build",
    "07_Client_Incentives",
    "08_VAS_Model",
    "09_Cross_Border_Model",
    "10_Operating_Expense_Build",
    "11_Margin_Walk",
    "12_Tax_DA_Capex_NWC",
    "13_Free_Cash_Flow",
    "14_Share_Count_Buybacks",
    "15_DCF",
    "16_Trading_Comps",
    "17_Precedent_Transactions",
    "18_SOTP",
    "19_Scenario_Manager",
    "20_Sensitivity_Tables",
    "21_Consensus_Bridge",
    "22_Output_Dashboard",
    "23_Charts",
    "24_Model_Checks",
    "25_Print_Package",
]

wb = Workbook()
wb.remove(wb.active)

dark = "1F2937"
blue = "1D4ED8"
light_blue = "DBEAFE"
gray = "E5E7EB"
yellow = "FEF3C7"
green = "DCFCE7"
white = "FFFFFF"

thin = Side(style="thin", color="D1D5DB")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

def title(ws, text, subtitle=None):
    ws["A1"] = text
    ws["A1"].font = Font(size=16, bold=True, color=white)
    ws["A1"].fill = PatternFill("solid", fgColor=dark)
    ws.merge_cells("A1:H1")
    if subtitle:
        ws["A2"] = subtitle
        ws["A2"].font = Font(italic=True, color="374151")
        ws.merge_cells("A2:H2")

def headers(ws, row, values):
    for col, value in enumerate(values, 1):
        cell = ws.cell(row, col, value)
        cell.font = Font(bold=True, color=white)
        cell.fill = PatternFill("solid", fgColor=blue)
        cell.alignment = Alignment(horizontal="center", wrap_text=True)
        cell.border = border

def label(cell):
    cell.font = Font(bold=True)
    cell.fill = PatternFill("solid", fgColor=gray)
    cell.border = border

def input_cell(cell):
    cell.fill = PatternFill("solid", fgColor=yellow)
    cell.border = border

def formula_cell(cell):
    cell.fill = PatternFill("solid", fgColor=light_blue)
    cell.border = border

def output_cell(cell):
    cell.fill = PatternFill("solid", fgColor=green)
    cell.border = border
    cell.font = Font(bold=True)

def setup_sheet(ws):
    for i in range(1, 13):
        ws.column_dimensions[get_column_letter(i)].width = 22
    ws.column_dimensions["A"].width = 34
    ws.freeze_panes = "B4"
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical="center", wrap_text=True)

for t in tabs:
    wb.create_sheet(t)

years = ["FY2021A", "FY2022A", "FY2023A", "FY2024A", "FY2025A", "FY2026E", "FY2027E", "FY2028E"]

for ws in wb.worksheets:
    setup_sheet(ws)

# Cover
ws = wb["01_Cover"]
title(ws, "Visa Institutional Equity Research Model V2", "FIG / Payments Coverage Model")
cover_rows = [
    ("Company", "Visa Inc."),
    ("Ticker", "NYSE: V"),
    ("Sector", "Financial Institutions / Payments"),
    ("Purpose", "Institutional-style equity research, valuation, and KPI model"),
    ("Primary Outputs", "DCF, trading comps, precedents, SOTP, scenarios, KPI dashboard"),
    ("Status", "V2 model scaffold; historical data and market data should be refreshed before use"),
]
for r, (k, v) in enumerate(cover_rows, 4):
    ws.cell(r, 1, k); label(ws.cell(r, 1))
    ws.cell(r, 2, v); ws.cell(r, 2).border = border

ws["A12"] = "Color Code"; label(ws["A12"])
legend = [("Yellow", "Hardcoded input"), ("Blue", "Formula"), ("Green", "Output")]
for r, (k, v) in enumerate(legend, 13):
    ws.cell(r, 1, k); ws.cell(r, 2, v)
    ws.cell(r, 1).border = ws.cell(r, 2).border = border

# Sources
ws = wb["02_Sources"]
title(ws, "Sources", "All major figures should be traceable to filings, transcripts, or public market data.")
headers(ws, 4, ["Source Type", "Document", "Date", "Metric / Section", "Reference", "Notes"])
sources = [
    ["Company Filing", "Visa 10-K", "TBD", "Historical financials / KPIs", "TBD", "Add filing section or page"],
    ["Company Filing", "Visa 10-Q", "TBD", "Quarterly update", "TBD", "Add filing section or page"],
    ["Transcript", "Visa earnings call", "TBD", "Management commentary", "TBD", "Add transcript source"],
    ["Peer Filing", "Mastercard 10-K", "TBD", "Peer comparison", "TBD", "Add filing section or page"],
    ["Market Data", "Public market data", "TBD", "Share price / multiples", "TBD", "Refresh before use"],
]
for r, row in enumerate(sources, 5):
    for c, value in enumerate(row, 1):
        ws.cell(r, c, value).border = border

# Setup Control
ws = wb["03_Setup_Control"]
title(ws, "Setup and Control", "Central assumptions for valuation and scenarios.")
headers(ws, 4, ["Assumption", "Base", "Bear", "Bull", "Notes"])
assumptions = [
    ["Current Share Price", "", "", "", "Input latest price"],
    ["Diluted Shares", "", "", "", "Input latest diluted shares"],
    ["Net Cash / (Debt)", "", "", "", "Cash less debt"],
    ["WACC", 0.085, 0.095, 0.075, "Discount rate"],
    ["Terminal Growth Rate", 0.035, 0.025, 0.045, "Perpetuity growth"],
    ["Exit EBITDA Multiple", 20.0, 16.0, 24.0, "Terminal value cross-check"],
    ["Target P/E Multiple", 30.0, 24.0, 35.0, "Forward EPS multiple"],
]
for r, row in enumerate(assumptions, 5):
    for c, value in enumerate(row, 1):
        ws.cell(r, c, value)
        ws.cell(r, c).border = border
        if c in [2, 3, 4]:
            input_cell(ws.cell(r, c))

# Historical Financials
ws = wb["04_Historical_Financials"]
title(ws, "Historical Financials", "Input reported historical financials and forecast core line items.")
headers(ws, 4, ["$ in millions, except per-share data"] + years)
items = [
    "Net Revenue",
    "YoY Revenue Growth",
    "Operating Expenses",
    "Operating Income",
    "Operating Margin",
    "Net Income",
    "Diluted EPS",
    "Operating Cash Flow",
    "Capital Expenditures",
    "Free Cash Flow",
    "Diluted Shares",
]
for r, item in enumerate(items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        if c <= 6:
            input_cell(ws.cell(r, c))
        else:
            formula_cell(ws.cell(r, c))
for c in range(3, 10):
    ws.cell(6, c, f"={get_column_letter(c)}5/{get_column_letter(c-1)}5-1")
for c in range(2, 10):
    ws.cell(8, c, f"={get_column_letter(c)}5-{get_column_letter(c)}7")
    ws.cell(9, c, f"={get_column_letter(c)}8/{get_column_letter(c)}5")
    ws.cell(14, c, f"={get_column_letter(c)}12-{get_column_letter(c)}13")

# KPI History
ws = wb["05_KPI_History"]
title(ws, "Payments KPI History", "Operating KPIs specific to networks and payments.")
headers(ws, 4, ["KPI"] + years + ["Why It Matters"])
kpis = [
    ("Payments Volume", "Primary scale driver"),
    ("Processed Transactions", "Data processing driver"),
    ("Cross-Border Volume", "High-yield international driver"),
    ("Credentials", "Network reach"),
    ("Acceptance Locations", "Merchant acceptance moat"),
    ("Gross Revenue Yield", "Pre-incentive monetization"),
    ("Net Revenue Yield", "Post-incentive monetization"),
    ("Client Incentives / Gross Revenue", "Pricing pressure"),
    ("VAS Revenue", "Services growth driver"),
    ("VAS % of Net Revenue", "Mix shift indicator"),
]
for r, (kpi, why) in enumerate(kpis, 5):
    ws.cell(r, 1, kpi); label(ws.cell(r, 1))
    ws.cell(r, 10, why); ws.cell(r, 10).border = border
    for c in range(2, 10):
        input_cell(ws.cell(r, c))

# Revenue Build
ws = wb["06_Revenue_Build"]
title(ws, "Revenue Build", "Driver-based revenue forecast.")
headers(ws, 4, ["$ in millions"] + years)
rev_items = [
    "Service Revenue",
    "Data Processing Revenue",
    "International Transaction Revenue",
    "Other Revenue",
    "Gross Revenue",
    "Client Incentives",
    "Net Revenue",
    "Net Revenue Growth",
]
for r, item in enumerate(rev_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        if r in [5, 6, 7, 8, 10]:
            input_cell(ws.cell(r, c))
        else:
            formula_cell(ws.cell(r, c))
for c in range(2, 10):
    ws.cell(9, c, f"=SUM({get_column_letter(c)}5:{get_column_letter(c)}8)")
    ws.cell(11, c, f"={get_column_letter(c)}9-{get_column_letter(c)}10")
for c in range(3, 10):
    ws.cell(12, c, f"={get_column_letter(c)}11/{get_column_letter(c-1)}11-1")

# Client Incentives
ws = wb["07_Client_Incentives"]
title(ws, "Client Incentives", "Analyze partner economics and take-rate pressure.")
headers(ws, 4, ["Metric"] + years)
client_items = [
    "Gross Revenue",
    "Client Incentives",
    "Net Revenue",
    "Client Incentives / Gross Revenue",
    "Incremental Incentive Ratio",
]
for r, item in enumerate(client_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        formula_cell(ws.cell(r, c))
for c in range(2, 10):
    ws.cell(5, c, f"='06_Revenue_Build'!{get_column_letter(c)}9")
    ws.cell(6, c, f"='06_Revenue_Build'!{get_column_letter(c)}10")
    ws.cell(7, c, f"='06_Revenue_Build'!{get_column_letter(c)}11")
    ws.cell(8, c, f"={get_column_letter(c)}6/{get_column_letter(c)}5")
for c in range(3, 10):
    ws.cell(9, c, f"=({get_column_letter(c)}6-{get_column_letter(c-1)}6)/({get_column_letter(c)}5-{get_column_letter(c-1)}5)")

# VAS Model
ws = wb["08_VAS_Model"]
title(ws, "Value-Added Services Model", "Analyze Visa's services growth runway.")
headers(ws, 4, ["Metric"] + years)
vas_items = ["VAS Revenue", "VAS Growth", "Net Revenue", "VAS % of Net Revenue", "Illustrative VAS Margin", "Illustrative VAS EBIT"]
for r, item in enumerate(vas_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        if r in [5, 9]:
            input_cell(ws.cell(r, c))
        else:
            formula_cell(ws.cell(r, c))
for c in range(3, 10):
    ws.cell(6, c, f"={get_column_letter(c)}5/{get_column_letter(c-1)}5-1")
for c in range(2, 10):
    ws.cell(7, c, f"='06_Revenue_Build'!{get_column_letter(c)}11")
    ws.cell(8, c, f"={get_column_letter(c)}5/{get_column_letter(c)}7")
    ws.cell(10, c, f"={get_column_letter(c)}5*{get_column_letter(c)}9")

# Cross Border
ws = wb["09_Cross_Border_Model"]
title(ws, "Cross-Border Model", "High-yield international revenue sensitivity.")
headers(ws, 4, ["Metric"] + years)
cb_items = [
    "Cross-Border Volume",
    "Cross-Border Volume Growth",
    "International Transaction Revenue",
    "International Revenue Growth",
    "International Revenue Yield",
]
for r, item in enumerate(cb_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        if r in [5, 7]:
            input_cell(ws.cell(r, c))
        else:
            formula_cell(ws.cell(r, c))
for c in range(3, 10):
    ws.cell(6, c, f"={get_column_letter(c)}5/{get_column_letter(c-1)}5-1")
    ws.cell(8, c, f"={get_column_letter(c)}7/{get_column_letter(c-1)}7-1")
for c in range(2, 10):
    ws.cell(9, c, f"={get_column_letter(c)}7/{get_column_letter(c)}5")

# Opex
ws = wb["10_Operating_Expense_Build"]
title(ws, "Operating Expense Build", "Forecast expenses and operating leverage.")
headers(ws, 4, ["$ in millions"] + years)
opex_items = ["Net Revenue", "Personnel", "Marketing", "Network and Processing", "Professional Fees", "G&A / Other", "Total Operating Expenses", "Operating Income", "Operating Margin"]
for r, item in enumerate(opex_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        if r in [6, 7, 8, 9, 10]:
            input_cell(ws.cell(r, c))
        else:
            formula_cell(ws.cell(r, c))
for c in range(2, 10):
    ws.cell(5, c, f"='06_Revenue_Build'!{get_column_letter(c)}11")
    ws.cell(11, c, f"=SUM({get_column_letter(c)}6:{get_column_letter(c)}10)")
    ws.cell(12, c, f"={get_column_letter(c)}5-{get_column_letter(c)}11")
    ws.cell(13, c, f"={get_column_letter(c)}12/{get_column_letter(c)}5")

# Margin Walk
ws = wb["11_Margin_Walk"]
title(ws, "Operating Margin Walk", "Bridge current margin to forecast margin.")
headers(ws, 4, ["Driver", "Margin Impact", "Commentary"])
walk = [
    ("FY2025 Operating Margin", "", "Starting point"),
    ("Volume Growth / Scale", "", "Operating leverage"),
    ("VAS Mix", "", "Services contribution"),
    ("Client Incentives", "", "Partner economics pressure"),
    ("Technology Investment", "", "Product and security investment"),
    ("Regulatory / Litigation", "", "Legal and compliance burden"),
    ("FY2028E Operating Margin", "=SUM(B5:B10)", "Ending margin"),
]
for r, row in enumerate(walk, 5):
    for c, value in enumerate(row, 1):
        ws.cell(r, c, value)
        ws.cell(r, c).border = border
        if c == 1:
            label(ws.cell(r, c))
        elif c == 2 and r < 11:
            input_cell(ws.cell(r, c))
        elif c == 2:
            formula_cell(ws.cell(r, c))

# Tax / D&A / Capex / NWC
ws = wb["12_Tax_DA_Capex_NWC"]
title(ws, "Tax, D&A, Capex, and Working Capital", "Core free cash flow forecast assumptions.")
headers(ws, 4, ["Metric"] + years)
tax_items = ["Operating Income", "Tax Rate", "NOPAT", "D&A", "D&A % Revenue", "Capex", "Capex % Revenue", "Change in NWC", "NWC % Revenue"]
for r, item in enumerate(tax_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        if r in [6, 8, 10, 12]:
            input_cell(ws.cell(r, c))
        else:
            formula_cell(ws.cell(r, c))
for c in range(2, 10):
    ws.cell(5, c, f"='10_Operating_Expense_Build'!{get_column_letter(c)}12")
    ws.cell(7, c, f"={get_column_letter(c)}5*(1-{get_column_letter(c)}6)")
    ws.cell(9, c, f"={get_column_letter(c)}8/'06_Revenue_Build'!{get_column_letter(c)}11")
    ws.cell(11, c, f"={get_column_letter(c)}10/'06_Revenue_Build'!{get_column_letter(c)}11")
    ws.cell(13, c, f"={get_column_letter(c)}12/'06_Revenue_Build'!{get_column_letter(c)}11")

# FCF
ws = wb["13_Free_Cash_Flow"]
title(ws, "Unlevered Free Cash Flow", "DCF cash flow build.")
headers(ws, 4, ["$ in millions"] + years)
fcf_items = ["NOPAT", "D&A", "Capital Expenditures", "Change in NWC", "Unlevered FCF", "FCF Margin", "FCF Growth"]
for r, item in enumerate(fcf_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        formula_cell(ws.cell(r, c))
for c in range(2, 10):
    ws.cell(5, c, f"='12_Tax_DA_Capex_NWC'!{get_column_letter(c)}7")
    ws.cell(6, c, f"='12_Tax_DA_Capex_NWC'!{get_column_letter(c)}8")
    ws.cell(7, c, f"='12_Tax_DA_Capex_NWC'!{get_column_letter(c)}10")
    ws.cell(8, c, f"='12_Tax_DA_Capex_NWC'!{get_column_letter(c)}12")
    ws.cell(9, c, f"={get_column_letter(c)}5+{get_column_letter(c)}6-{get_column_letter(c)}7-{get_column_letter(c)}8")
    ws.cell(10, c, f"={get_column_letter(c)}9/'06_Revenue_Build'!{get_column_letter(c)}11")
for c in range(3, 10):
    ws.cell(11, c, f"={get_column_letter(c)}9/{get_column_letter(c-1)}9-1")

# Buybacks
ws = wb["14_Share_Count_Buybacks"]
title(ws, "Share Count and Buybacks", "Model EPS accretion from capital return.")
headers(ws, 4, ["Metric"] + years)
buyback_items = ["Beginning Diluted Shares", "Repurchase Dollars", "Average Repurchase Price", "Shares Retired", "SBC / Other", "Ending Diluted Shares", "Net Income", "Diluted EPS"]
for r, item in enumerate(buyback_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        if r in [5, 6, 7, 9]:
            input_cell(ws.cell(r, c))
        else:
            formula_cell(ws.cell(r, c))
for c in range(2, 10):
    ws.cell(8, c, f"={get_column_letter(c)}6/{get_column_letter(c)}7")
    ws.cell(10, c, f"={get_column_letter(c)}5-{get_column_letter(c)}8+{get_column_letter(c)}9")
    ws.cell(11, c, f"='04_Historical_Financials'!{get_column_letter(c)}10")
    ws.cell(12, c, f"={get_column_letter(c)}11/{get_column_letter(c)}10")

# DCF
ws = wb["15_DCF"]
title(ws, "DCF Valuation", "Intrinsic valuation using unlevered free cash flow.")
headers(ws, 4, ["$ in millions"] + years)
dcf_items = ["Unlevered FCF", "Discount Period", "Discount Factor", "PV of FCF"]
for r, item in enumerate(dcf_items, 5):
    ws.cell(r, 1, item); label(ws.cell(r, 1))
    for c in range(2, 10):
        formula_cell(ws.cell(r, c))
for c in range(2, 10):
    ws.cell(5, c, f"='13_Free_Cash_Flow'!{get_column_letter(c)}9")
    ws.cell(6, c, c - 1)
    ws.cell(7, c, f"=1/(1+'03_Setup_Control'!B8)^{get_column_letter(c)}6")
    ws.cell(8, c, f"={get_column_letter(c)}5*{get_column_letter(c)}7")

summary = [
    ("PV of Explicit FCF", "=SUM(B8:I8)"),
    ("Terminal FCF", "=I5*(1+'03_Setup_Control'!B9)"),
    ("Terminal Value", "=B13/('03_Setup_Control'!B8-'03_Setup_Control'!B9)"),
    ("PV of Terminal Value", "=B14*I7"),
    ("Enterprise Value", "=B12+B15"),
    ("Net Cash / (Debt)", "='03_Setup_Control'!B7"),
    ("Equity Value", "=B16+B17"),
    ("Diluted Shares", "='03_Setup_Control'!B6"),
    ("Implied DCF Value / Share", "=B18/B19"),
]
for r, (k, v) in enumerate(summary, 12):
    ws.cell(r, 1, k); label(ws.cell(r, 1))
    ws.cell(r, 2, v); output_cell(ws.cell(r, 2))

# Trading Comps
ws = wb["16_Trading_Comps"]
title(ws, "Trading Comparable Company Analysis", "Benchmark Visa against payments peers.")
headers(ws, 4, ["Company", "Ticker", "Peer Group", "Market Cap", "EV", "Revenue Growth", "EBITDA Margin", "P/E", "EV/EBITDA", "FCF Yield", "Notes"])
peers = [
    ["Visa", "V", "Network"],
    ["Mastercard", "MA", "Network"],
    ["American Express", "AXP", "Closed-loop"],
    ["Fiserv", "FI", "Processor"],
    ["Global Payments", "GPN", "Processor"],
    ["Shift4", "FOUR", "Acquirer / PSP"],
    ["Adyen", "ADYEN", "Acquirer / PSP"],
    ["PayPal", "PYPL", "Wallet / Fintech"],
    ["Block", "XYZ", "Wallet / Fintech"],
    ["FIS", "FIS", "Infrastructure"],
]
for r, row in enumerate(peers, 5):
    for c in range(1, 12):
        ws.cell(r, c, row[c-1] if c <= len(row) else "")
        ws.cell(r, c).border = border
        if c >= 4:
            input_cell(ws.cell(r, c))

# Precedents
ws = wb["17_Precedent_Transactions"]
title(ws, "Precedent Transaction Analysis", "Payments M&A valuation context.")
headers(ws, 4, ["Date", "Acquirer", "Target", "Category", "Transaction Value", "Revenue", "EBITDA", "EV/Revenue", "EV/EBITDA", "Strategic Rationale", "Relevance to Visa"])
for r in range(5, 15):
    for c in range(1, 12):
        if c in [8, 9]:
            ws.cell(r, c, f"=E{r}/F{r}" if c == 8 else f"=E{r}/G{r}")
            formula_cell(ws.cell(r, c))
        else:
            input_cell(ws.cell(r, c))

# SOTP
ws = wb["18_SOTP"]
title(ws, "Sum-of-the-Parts Valuation", "Separate core network, VAS, and money movement value pools.")
headers(ws, 4, ["Segment", "Metric", "Metric Value", "Multiple", "Implied Value", "Rationale"])
segments = [
    "Core Consumer Payments Network",
    "Commercial / B2B Payments",
    "Value-Added Services",
    "Visa Direct / Money Movement",
    "Net Cash / Other",
]
for r, seg in enumerate(segments, 5):
    ws.cell(r, 1, seg); label(ws.cell(r, 1))
    for c in range(2, 7):
        if c == 5:
            ws.cell(r, c, f"=C{r}*D{r}")
            formula_cell(ws.cell(r, c))
        else:
            input_cell(ws.cell(r, c))
ws["D12"] = "Total SOTP Equity Value"; label(ws["D12"])
ws["E12"] = "=SUM(E5:E9)"; output_cell(ws["E12"])

# Scenario Manager
ws = wb["19_Scenario_Manager"]
title(ws, "Scenario Manager", "Driver-based severe downside, bear, base, and bull cases.")
headers(ws, 4, ["Driver", "Severe Downside", "Bear", "Base", "Bull"])
drivers = [
    "Revenue CAGR",
    "Operating Margin",
    "Client Incentives / Gross Revenue",
    "VAS Growth",
    "Cross-Border Growth",
    "Terminal P/E",
    "DCF Value / Share",
    "Comps Value / Share",
    "Scenario Target Price",
]
for r, driver in enumerate(drivers, 5):
    ws.cell(r, 1, driver); label(ws.cell(r, 1))
    for c in range(2, 6):
        if r <= 10:
            input_cell(ws.cell(r, c))
        else:
            formula_cell(ws.cell(r, c))
for c in range(2, 6):
    ws.cell(13, c, f"=AVERAGE({get_column_letter(c)}11:{get_column_letter(c)}12)")

# Sensitivities
ws = wb["20_Sensitivity_Tables"]
title(ws, "Sensitivity Tables", "DCF and valuation sensitivity outputs.")
ws["A4"] = "DCF Sensitivity: WACC vs Terminal Growth"; label(ws["A4"])
waccs = [0.075, 0.08, 0.085, 0.09, 0.095]
growths = [0.025, 0.03, 0.035, 0.04, 0.045]
for i, wacc in enumerate(waccs, 2):
    ws.cell(5, i, wacc); label(ws.cell(5, i))
for r, growth in enumerate(growths, 6):
    ws.cell(r, 1, growth); label(ws.cell(r, 1))
    for c in range(2, 7):
        ws.cell(r, c, "Link to DCF")
        formula_cell(ws.cell(r, c))

# Consensus Bridge
ws = wb["21_Consensus_Bridge"]
title(ws, "Consensus Bridge", "Compare project estimates with consensus expectations.")
headers(ws, 4, ["Metric", "FY2026E Consensus", "FY2026E Project", "Variance", "FY2027E Consensus", "FY2027E Project", "Variance", "Interpretation"])
metrics = ["Net Revenue", "Operating Margin", "EPS", "FCF", "Buybacks", "Target P/E"]
for r, metric in enumerate(metrics, 5):
    ws.cell(r, 1, metric); label(ws.cell(r, 1))
    for c in range(2, 9):
        if c in [4, 7]:
            ws.cell(r, c, f"=C{r}-B{r}" if c == 4 else f"=F{r}-E{r}")
            formula_cell(ws.cell(r, c))
        else:
            input_cell(ws.cell(r, c))

# Dashboard
ws = wb["22_Output_Dashboard"]
title(ws, "Output Dashboard", "Recruiter-friendly model summary.")
dashboard = [
    ("Recommendation", "Outperform / Base Case Positive"),
    ("Primary Valuation Method", "DCF + Forward P/E + Comps"),
    ("DCF Value / Share", "='15_DCF'!B20"),
    ("Base Scenario Target", "='19_Scenario_Manager'!D13"),
    ("Bear Scenario Target", "='19_Scenario_Manager'!C13"),
    ("Bull Scenario Target", "='19_Scenario_Manager'!E13"),
    ("Key Debate", "Take-rate durability vs regulatory and alternative-rail pressure"),
    ("Variant Perception", "VAS, tokenization, risk/fraud, and money movement extend network relevance"),
]
for r, (k, v) in enumerate(dashboard, 4):
    ws.cell(r, 1, k); label(ws.cell(r, 1))
    ws.cell(r, 2, v); output_cell(ws.cell(r, 2))

# Charts
ws = wb["23_Charts"]
title(ws, "Charts", "Placeholder sheet for report-ready chart outputs.")
chart_list = [
    "Revenue and margin trend",
    "Payments volume and processed transactions",
    "Cross-border volume",
    "Client incentives as % of gross revenue",
    "VAS revenue mix",
    "Peer valuation comparison",
    "DCF sensitivity",
    "Scenario output matrix",
    "Football field valuation",
]
for r, item in enumerate(chart_list, 4):
    ws.cell(r, 1, item)
    ws.cell(r, 1).border = border

# Checks
ws = wb["24_Model_Checks"]
title(ws, "Model Checks", "Quality-control checks for model integrity.")
headers(ws, 4, ["Check", "Logic", "Status"])
checks = [
    ["Revenue Build Check", "Gross Revenue - Client Incentives = Net Revenue", '=IF(ABS(\'06_Revenue_Build\'!I9-\'06_Revenue_Build\'!I10-\'06_Revenue_Build\'!I11)<1,"OK","ERROR")'],
    ["FCF Check", "NOPAT + D&A - Capex - NWC = UFCF", '=IF(ABS(\'13_Free_Cash_Flow\'!I5+\'13_Free_Cash_Flow\'!I6-\'13_Free_Cash_Flow\'!I7-\'13_Free_Cash_Flow\'!I8-\'13_Free_Cash_Flow\'!I9)<1,"OK","ERROR")'],
    ["DCF Check", "Equity Value / Shares = Value per Share", '=IFERROR(IF(ABS(\'15_DCF\'!B18/\'15_DCF\'!B19-\'15_DCF\'!B20)<0.01,"OK","ERROR"),"CHECK INPUTS")'],
]
for r, row in enumerate(checks, 5):
    for c, value in enumerate(row, 1):
        ws.cell(r, c, value)
        ws.cell(r, c).border = border
        if c == 1:
            label(ws.cell(r, c))
        elif c == 3:
            output_cell(ws.cell(r, c))

# Print Package
ws = wb["25_Print_Package"]
title(ws, "Print Package", "Sections to print/export for appendix.")
for r, item in enumerate(["Output Dashboard", "DCF", "Trading Comps", "Precedents", "SOTP", "Scenarios", "Sensitivities", "Model Checks"], 4):
    ws.cell(r, 1, item)
    ws.cell(r, 1).border = border

for ws in wb.worksheets:
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical="center", wrap_text=True)
    for r in range(1, ws.max_row + 1):
        ws.row_dimensions[r].height = 22

wb.save(out)
print(f"Created {out}")
