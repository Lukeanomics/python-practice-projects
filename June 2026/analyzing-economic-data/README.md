
---

# Analyzing Economic Data (Practice Project)

## Purpose

Build a structured macroeconomic data pipeline using Python (Pandas) that transforms raw CPI data into interpretable economic metrics (MoM, YoY, and category-level changes).

---

## Current Stage

Layer 2 — Data Transformation & Metric Construction

---

## What this project does right now

* Loads CPI-style CSV data into a Pandas DataFrame
* Filters dataset by hierarchical CPI structure (`Indent-Level`)
* Removes irrelevant or redundant columns
* Renames raw dataset fields into analyst-readable labels
* Computes derived macroeconomic metrics:

  * Absolute change (Delta)
  * Month-over-Month percentage change (MoM%)
* Reorders output for analytical readability

---

## Data being used

CPI expenditure-category dataset containing:

* Expenditure category hierarchy (`Indent-Level`)
* CPI index values (April 2026, May 2026)
* Pre-calculated YoY and MoM fields (partially used/validated)
* Derived metrics created within pipeline (Delta, MoM%)

---

## Key transformations introduced

* Structural filtering (hierarchical CPI levels)
* Column reduction (removing non-essential metadata fields)
* Feature engineering:

  * `Delta = May Index − April Index`
  * `MoM% Change = Delta / April Index`
* Analytical restructuring of output table

---

## Goal of next step

Transition from transformation → interpretation by:

* Sorting and ranking categories by MoM movement
* Identifying top inflation drivers and deflationary components
* Separating macro groups (Food, Energy, Core services)
* Producing structured economic summaries instead of raw tables

---
