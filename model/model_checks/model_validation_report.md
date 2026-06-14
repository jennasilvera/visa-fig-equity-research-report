# Visa Institutional Model Validation Report

## Purpose

This report validates that the institutional Visa model contains the expected workbook tabs, source-backed data files, and model population outputs.

## Workbook Status

- Model file: `model/Visa_Institutional_Model_v2.xlsx`
- Workbook opens successfully: `YES`
- Sheet count: `25`

## Required Sheet Check

| Sheet | Status |
|---|---|
| `01_Cover` | FOUND |
| `02_Sources` | FOUND |
| `03_Setup_Control` | FOUND |
| `04_Historical_Financials` | FOUND |
| `05_KPI_History` | FOUND |
| `06_Revenue_Build` | FOUND |
| `07_Client_Incentives` | FOUND |
| `08_VAS_Model` | FOUND |
| `09_Cross_Border_Model` | FOUND |
| `10_Operating_Expense_Build` | FOUND |
| `11_Margin_Walk` | FOUND |
| `12_Tax_DA_Capex_NWC` | FOUND |
| `13_Free_Cash_Flow` | FOUND |
| `14_Share_Count_Buybacks` | FOUND |
| `15_DCF` | FOUND |
| `16_Trading_Comps` | FOUND |
| `17_Precedent_Transactions` | FOUND |
| `18_SOTP` | FOUND |
| `19_Scenario_Manager` | FOUND |
| `20_Sensitivity_Tables` | FOUND |
| `21_Consensus_Bridge` | FOUND |
| `22_Output_Dashboard` | FOUND |
| `23_Charts` | FOUND |
| `24_Model_Checks` | FOUND |
| `25_Print_Package` | FOUND |

## Required Source / Output File Check

| File | Status |
|---|---|
| `data/processed/visa_historical_financials_source_backed.csv` | FOUND |
| `data/processed/visa_operating_kpis_source_backed.csv` | FOUND |
| `data/processed/visa_historical_data_sources.md` | FOUND |
| `model/model_outputs/model_population_summary.csv` | FOUND |
| `scripts/populate_institutional_model_v2.py` | FOUND |

## Historical Data Spot Check

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|---:|---:|
| Net Revenue | 24105 | 29310 | 32653 | 35926 | 40000 |
| Operating Income | 15804 | 18813 | 21000 | 23595 | 23994 |
| Net Income | 12311 | 14957 | 17273 | 19743 | 20058 |
| Diluted EPS | 5.63 | 7 | 8.28 | 9.73 | 10.2 |

## Model Notes

- The V2 model has been populated with source-backed FY2021–FY2025 historical financials and operating KPIs.
- Historical operating expenses are currently plugged into G&A / Other until a detailed expense breakout is added.
- Forecast years, DCF outputs, trading comps, SOTP, and scenario outputs should be refreshed with current market data before publication or interview use.
