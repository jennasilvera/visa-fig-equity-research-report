from pathlib import Path
import csv
import matplotlib.pyplot as plt

FIN_PATH = Path("data/processed/visa_historical_financials_source_backed.csv")
KPI_PATH = Path("data/processed/visa_operating_kpis_source_backed.csv")
OUT_PATH = Path("assets/charts/visa_kpi_dashboard_v2.png")
SUMMARY_PATH = Path("data/processed/kpi_dashboard_summary.csv")

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)

def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def parse_number(value):
    value = str(value).strip()
    if value.endswith("%"):
        return float(value[:-1])
    if value == "":
        return None
    return float(value.replace(",", ""))

financials = read_csv(FIN_PATH)
kpis = read_csv(KPI_PATH)

years = [row["Fiscal Year"] for row in financials]

net_revenue_b = [parse_number(row["Net Revenue"]) / 1000 for row in financials]
operating_income_b = [parse_number(row["Operating Income"]) / 1000 for row in financials]
free_cash_flow_b = [parse_number(row["Free Cash Flow"]) / 1000 for row in financials]
operating_margin = [parse_number(row["Operating Margin"]) for row in financials]

payments_volume_t = [parse_number(row["Payments Volume ($T)"]) for row in kpis]
processed_transactions_b = [parse_number(row["Processed Transactions (B)"]) for row in kpis]
net_revenue_yield = [parse_number(row["Net Revenue Yield"]) for row in kpis]

with SUMMARY_PATH.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Metric", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025"])
    writer.writerow(["Net Revenue ($B)", *net_revenue_b])
    writer.writerow(["Operating Income ($B)", *operating_income_b])
    writer.writerow(["Free Cash Flow ($B)", *free_cash_flow_b])
    writer.writerow(["Operating Margin (%)", *operating_margin])
    writer.writerow(["Payments Volume ($T)", *payments_volume_t])
    writer.writerow(["Processed Transactions (B)", *processed_transactions_b])
    writer.writerow(["Net Revenue Yield (%)", *net_revenue_yield])

fig, axes = plt.subplots(3, 2, figsize=(13, 10))

charts = [
    (axes[0, 0], net_revenue_b, "Net Revenue", "$ in billions"),
    (axes[0, 1], operating_income_b, "Operating Income", "$ in billions"),
    (axes[1, 0], payments_volume_t, "Payments Volume", "$ in trillions"),
    (axes[1, 1], processed_transactions_b, "Processed Transactions", "billions"),
    (axes[2, 0], operating_margin, "Operating Margin", "%"),
    (axes[2, 1], free_cash_flow_b, "Free Cash Flow", "$ in billions"),
]

for ax, values, title, ylabel in charts:
    ax.plot(years, values, marker="o")
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

fig.suptitle("Visa Historical KPI Dashboard", fontsize=16)

footnote = (
    "Source: Project CSVs based on Visa annual reports / Form 10-K data. "
    "Portfolio project only; not investment advice. Net revenue yield is tracked in the data file and model."
)
fig.text(0.01, 0.01, footnote, fontsize=8)

plt.tight_layout(rect=[0, 0.04, 1, 0.96])
plt.savefig(OUT_PATH, dpi=200, bbox_inches="tight")
plt.close()

print(f"Wrote {OUT_PATH}")
print(f"Wrote {SUMMARY_PATH}")
