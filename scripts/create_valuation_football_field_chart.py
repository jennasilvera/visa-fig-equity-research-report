from pathlib import Path
import csv
import matplotlib.pyplot as plt

DATA_PATH = Path("data/processed/valuation_football_field_ranges.csv")
OUT_PATH = Path("assets/charts/visa_valuation_football_field.png")

DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

rows = [
    ["Methodology", "Low", "High", "Notes"],
    ["DCF - Bear Case", 210, 270, "Illustrative downside range"],
    ["DCF - Base Case", 280, 340, "Illustrative intrinsic value range"],
    ["DCF - Bull Case", 340, 410, "Illustrative upside range"],
    ["Forward P/E", 260, 360, "Illustrative multiple-based range"],
    ["EV/EBITDA", 250, 350, "Illustrative enterprise value range"],
    ["FCF Yield", 240, 330, "Illustrative free cash flow yield range"],
    ["Historical Multiple Range", 260, 380, "Illustrative historical trading range"],
    ["SOTP", 280, 390, "Illustrative sum-of-the-parts range"],
]

with DATA_PATH.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

labels = [row[0] for row in rows[1:]]
lows = [float(row[1]) for row in rows[1:]]
highs = [float(row[2]) for row in rows[1:]]
widths = [high - low for low, high in zip(lows, highs)]
y_pos = list(range(len(labels)))

fig, ax = plt.subplots(figsize=(11, 6.2))

ax.barh(y_pos, widths, left=lows, height=0.55)

ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.invert_yaxis()

ax.set_xlabel("Illustrative Implied Share Price Range ($)")
ax.set_title("Visa Illustrative Valuation Football Field")

for i, (low, high) in enumerate(zip(lows, highs)):
    ax.text(low - 4, i, f"${low:.0f}", va="center", ha="right", fontsize=8)
    ax.text(high + 4, i, f"${high:.0f}", va="center", ha="left", fontsize=8)

ax.grid(axis="x", linestyle="--", linewidth=0.5, alpha=0.6)

footnote = (
    "Note: Ranges are illustrative framework outputs for portfolio/recruiting purposes. "
    "Refresh with current market data, peer multiples, filings, and model outputs before investment use."
)
fig.text(0.01, 0.01, footnote, fontsize=7)

plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(OUT_PATH, dpi=200, bbox_inches="tight")
plt.close()

print(f"Wrote {DATA_PATH}")
print(f"Wrote {OUT_PATH}")
