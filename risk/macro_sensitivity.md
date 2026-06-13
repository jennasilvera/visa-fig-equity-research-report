# Visa Macro Sensitivity Framework

## Purpose

Visa is not a lender and does not take direct credit risk like a bank. However, Visa is still economically sensitive because its revenue is linked to payment volume, processed transactions, cross-border activity, consumer spending, business spending, FX, and global travel.

This file explains how macro variables should flow through the model.

---

## Macro Exposure Summary

Visa's macro sensitivity is driven by:

1. Nominal consumer spending
2. Transaction growth
3. Cross-border travel
4. Cross-border ecommerce
5. FX translation
6. Inflation
7. Employment and consumer health
8. Business and commercial spending
9. Interest rates and valuation multiples
10. Recession risk

---

## Macro Driver Matrix

| Macro Driver | Visa Exposure | Model Line Affected | Directional Impact |
|---|---|---|---|
| Nominal Consumer Spending | Higher spending increases payments volume | Payments volume, service revenue | Positive |
| Inflation | Supports nominal volume but can pressure real demand | Payments volume, transaction mix | Mixed |
| Real Consumer Spending | Drives underlying transaction demand | Volume growth, processed transactions | Positive |
| Employment | Supports consumer purchasing power | Payment volume | Positive |
| Cross-Border Travel | High-yield driver of international revenue | Cross-border volume, international transaction revenue | Positive |
| Cross-Border Ecommerce | Supports card-not-present international activity | Cross-border volume | Positive |
| FX Translation | Affects reported revenue from international operations | Reported revenue growth | Mixed |
| Interest Rates | Affects valuation multiples and discount rates | WACC, terminal multiple | Negative when rates rise |
| Recession Risk | Pressures discretionary spending and travel | Revenue growth, margin | Negative |
| Business Spending | Supports commercial payments and B2B opportunity | Commercial volume, VAS | Positive |

---

## Key Sensitivities to Add to the Model

| Sensitivity | Suggested Range | Why It Matters |
|---|---|---|
| Net Revenue Growth | -300 bps to +300 bps | Captures macro-driven volume changes |
| Cross-Border Growth | -500 bps to +500 bps | Captures high-yield revenue volatility |
| Operating Margin | -200 bps to +200 bps | Captures operating leverage or deleverage |
| Client Incentives / Gross Revenue | +100 bps to +300 bps | Captures competitive and partner pressure |
| WACC | 7.0% to 10.0% | Captures rate environment |
| Terminal P/E | 22.0x to 36.0x | Captures multiple compression or expansion |
| Terminal Growth | 2.0% to 4.5% | Captures long-term growth duration |

---

## Scenario Integration

### Bull Macro Case

- Consumer spending remains resilient
- Cross-border travel remains strong
- Ecommerce growth continues
- FX is neutral or favorable
- Interest rates decline or stabilize
- Premium growth multiples remain supported

### Base Macro Case

- Spending growth normalizes
- Cross-border growth remains positive but moderates
- Inflation supports nominal volume without severe demand destruction
- Operating margin remains broadly stable
- Valuation multiple remains premium but disciplined

### Bear Macro Case

- Consumer spending slows
- Cross-border travel decelerates
- FX is unfavorable
- Operating leverage weakens
- Interest rates pressure long-duration equities
- Investors compress Visa's terminal multiple

### Severe Downside Macro Case

- Global recession
- Cross-border travel shock
- Discretionary spending slowdown
- Higher incentives and lower net revenue yield
- Multiple compression
- Buybacks less able to offset EPS pressure

---

## Why Macro Matters for Visa

Visa's direct credit risk is limited, but its revenue still depends on economic activity. In a downturn, Visa may not suffer credit losses like a bank, but it can experience:

- Slower payment volume growth
- Lower cross-border volume
- Lower international transaction revenue
- Reduced operating leverage
- Lower EPS growth
- Multiple compression

This is why the model should include both operating sensitivity and valuation sensitivity.
