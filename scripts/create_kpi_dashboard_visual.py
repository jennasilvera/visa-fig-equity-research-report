from pathlib import Path
import csv
import matplotlib.pyplot as plt

FIN_PATH = Path("data/processed/visa_historical_financials_source_backed.csv")
KPI_PATH = Path("data/processed/visa_operating_kpis_source_backed.csv")
OUT_PATH = Path("assets/charts/visa_kpi_dashboard.png")
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

net_revenue = [parse_number(row["Net Revenue"]) for row in financials]
operating_income = [parse_number(row["Operating Income"]) for row in financials]
free_cash_flow = [parse_number(row["Free Cash Flow"]) for row in financials]
operating_margin = [parse_number(row["Operating Margin"]) for row in financials]

payments_volume = [parse_number(row["Payments Volume ($T)"]) for row in kpis]
processed_transactions = [parse_number(row["Processed Transactions (B)"]) for row in kpis]
credentials = [parse_number(row["Payment Credentials (B)"]) for row in kpis]
net_revenue_yield = [parse_number(row["Net Revenue Yield"]) for row in kpis]

with SUMMARY_PATH.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Metric", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025"])
    writer.writerow(["Net Revenue ($M)", *net_revenue])
    writer.writerow(["Operating Income ($M)", *operating_income])
    writer.writerow(["Free Cash Flow ($M)", *free_cash_flow])
    writer.writerow(["Operating Margin (%)", *operating_margin])
    writer.writerow(["Payments Volume ($T)", *payments_volume])
    writer.writerow(["Processed Transactions (B)", *processed_transactions])
    writer.writerow(["Payment Credentials (B)", *credentials])
    writer.writerow(["Net Revenue Yield (%)", *net_revenue_yield])

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(years, net_revenue, marker="o", label="Net Revenue")
axes[0, 0].plot(years, operating_income, marker="o", label="Operating Income")
axes[0, 0].set_title("Revenue and Operating Income")
axes[0, 0].set_ylabel("$ in millions")
axes[0, 0].legend()
axes[0, 0].grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

axes[0, 1].plot(years, payments_volume, marker="o", label="Payments Volume")
axes[0, 1].plot(years, processed_transactions, marker="o", label="Processed Transactions")
axes[0, 1].set_title("Operating Scale")
axes[0, 1].set_ylabel("$T / billions")
axes[0, 1].legend()
axes[0, 1].grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

axes[1, 0].plot(years, operating_margin, marker="o", label="Operating Margin")
axes[1, 0].plot(years, net_revenue_yield, marker="o", label="Net Revenue Yield")
axes[1, 0].set_title("Margin and Yield")
axes[1, 0].set_ylabel("%")
axes[1, 0].legend()
axes[1, 0].grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

axes[1, 1].plot(years, free_cash_flow, marker="o", label="Free Cash Flow")
axes[1, 1].set_title("Free Cash Flow")
axes[1, 1].set_ylabel("$ in millions")
axes[1, 1].legend()
axes[1, 1].grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

fig.suptitle("Visa Historical KPI Dashboard", fontsize=16)

footnote = (
    "Source: Project CSVs based on Visa annual reports / Form 10-K data. "
    "Portfolio project only; not investment advice."
)
fig.text(0.01, 0.01, footnote, fontsize=8)

plt.tight_layout(rect=[0, 0.04, 1, 0.95])
plt.savefig(OUT_PATH, dpi=200, bbox_inches="tight")
plt.close()

print(f"Wrote {OUT_PATH}")
print(f"Wrote {SUMMARY_PATH}")
