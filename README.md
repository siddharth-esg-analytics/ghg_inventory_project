## Data Source

This project uses publicly available electricity consumption data.

Original Dataset:
[Electricity Consumption Dataset / divanshu22 / Panda-monium]

Source:
https://www.kaggle.com/datasets/divanshu22/electricity-consumption-dataset

Data Handling Approach:
- Raw dataset stored in /data/raw
- No structural modifications applied to original data
- Derived datasets generated through documented transformation workflows




# GHG Inventory Scope 2 Analytics Pipeline

## Overview
This repository contains a modular analytics pipeline designed for scope 2 greenhouse gas (GHG) inventory processing, validation, and aggregation.

The system focuses on transforming high-frequency minute-level activity data into hourly auditable emissions outputs suitable for sustainability reporting and analysis.

---

## Objectives
- Data cleaning and preprocessing
- Validation and anomaly detection
- Temporal aggregation (minute → hourly → reporting level)
- Generation of structured analytical outputs

---

## Repository Structure

/data  
Raw, processed, and reference datasets

/python_pipeline  
Data cleaning, validation, and aggregation logic

/excel_model  
Auditable analytical models and assumptions framework

/outputs  
01_minute_level_energy_validation_summary.csv
02_hourly_energy_consumption_clean.csv
hourly_scope_2_aggregation_data.xlsx

---

## Functional Capabilities
- High-frequency data handling
- Validation workflows
- Reproducible aggregation logic
- Audit-friendly output design

---

## Use Cases
- GHG inventory preparation
- ESG analytics workflows
- Sustainability reporting pipelines
- Emissions data validation systems

---

## Technical Stack
- Python (data processing & validation)
- Excel (auditable modeling layer)

---

## Notes
This project demonstrates practical analytics architecture principles applied to emissions data workflows.
