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

net_revenue_b = [parse_number(row["Net Revenue"]) / 1000 for row in financials]
operating_income_b = [parse_number(row["Operating Income"]) / 1000 for row in financials]
free_cash_flow_b = [parse_number(row["Free Cash Flow"]) / 1000 for row in financials]
operating_margin = [parse_number(row["Operating Margin"]) for row in financials]

payments_volume_t = [parse_number(row["Payments Volume ($T)"]) for row in kpis]
processed_transactions_b = [parse_number(row["Processed Transactions (B)"]) for row in kpis]
credentials_b = [parse_number(row["Payment Credentials (B)") if False else "Payment Credentials (B)"]) for row in kpis]
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
    writer.writerow(["Payment Credentials (B)", *credentials_b])
    writer.writerow(["Net Revenue Yield (%)", *net_revenue_yield])

fig, axes = plt.subplots(2, 2, figsize=(13, 8.5))

# Revenue and operating income
axes[0, 0].plot(years, net_revenue_b, marker="o", label="Net Revenue")
axes[0, 0].plot(years, operating_income_b, marker="o", label="Operating Income")
axes[0, 0].set_title("Revenue and Operating Income")
axes[0, 0].set_ylabel("$ in billions")
axes[0, 0].legend()
axes[0, 0].grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

# Operating scale with dual axis
ax1 = axes[0, 1]
ax2 = ax1.twinx()

line1 = ax1.plot(years, payments_volume_t, marker="o", label="Payments Volume")
line2 = ax2.plot(years, processed_transactions_b, marker="o", label="Processed Transactions")

ax1.set_title("Operating Scale")
ax1.set_ylabel("Payments Volume ($T)")
ax2.set_ylabel("Processed Transactions (B)")
ax1.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

lines = line1 + line2
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper left")

# Margin and yield with dual axis
ax3 = axes[1, 0]
ax4 = ax3.twinx()

line3 = ax3.plot(years, operating_margin, marker="o", label="Operating Margin")
line4 = ax4.plot(years, net_revenue_yield, marker="o", label="Net Revenue Yield")

ax3.set_title("Margin and Revenue Yield")
ax3.set_ylabel("Operating Margin (%)")
ax4.set_ylabel("Net Revenue Yield (%)")
ax3.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

lines = line3 + line4
labels = [line.get_label() for line in lines]
ax3.legend(lines, labels, loc="upper left")

# Free cash flow
axes[1, 1].plot(years, free_cash_flow_b, marker="o", label="Free Cash Flow")
axes[1, 1].set_title("Free Cash Flow")
axes[1, 1].set_ylabel("$ in billions")
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
