# 🌞 KAIM-8 — Week 0 Interim Report

## Solar Data Discovery Challenge

---

## 1. Introduction

This interim report summarizes my **Week 0 plan and progress** for the _Solar Data Discovery Challenge_.  
The goal of this week is to explore solar datasets from **Benin**, **Sierra Leone**, and **Togo**, and prepare a clean, analyzable dataset for cross-country comparison.  
The report focuses on **Task 1 (Git & Environment Setup)** and **Task 2 (Data Profiling, Cleaning & EDA)**.

---

## 2. Task 1: Git & Environment Setup

**Objective:** Establish a reproducible development environment with proper version control to ensure smooth collaboration and workflow.

### 🔹 Key Actions Taken

#### 1. Repository Initialization

- Created GitHub repository: `solar-challenge-week0`
- Cloned repository locally and initialized a Python virtual environment (`venv`)
- Managed dependencies with `requirements.txt`

#### 2. Branching and Commits

- Created feature branch: `setup-task`
- Example commits:
  - `init: add .gitignore`
  - `chore: venv setup`
  - `ci: add GitHub Actions workflow`
- `.gitignore` configured to exclude:
  - `data/` and CSV files
  - `.ipynb_checkpoints/`

#### 3. Continuous Integration

- Added **GitHub Actions** workflow to:
  - Install dependencies (`pip install -r requirements.txt`)
  - Verify Python version and environment setup

#### 4. Environment Verification

- Created `requirements.txt` including:  
  `pandas`, `numpy`, `plotly`, `streamlit`
- Verified environment using:
  ```bash
  python --version
  pip freeze
  ```

## 3. Task 2: Data Profiling, Cleaning & EDA Approach

**Objective:**  
Understand, clean, and explore the solar datasets to prepare them for cross-country comparison and visualization.

---

### 3.1 Data Profiling

- Loaded CSV files into Pandas DataFrames with timestamp parsing
- Checked column types, missing values, and descriptive statistics
- Flagged columns with **> 5% missing values**
- Computed statistics for numeric columns:  
  `GHI`, `DNI`, `DHI`, `ModA`, `ModB`, `Tamb`, `RH`, `WS`, `WSgust`, `BP`

---

### 3.2 Data Cleaning

**Missing Values**

- Applied median imputation for key metrics
- Dropped rows with critical data missing

**Outliers**

- Identified using Z-score (|Z| > 3) for irradiance and sensor readings

**Timestamp Standardization**

- Ensured consistent timestamp formats and alignment across datasets

---

### 3.3 Exploratory Data Analysis (EDA)

| Focus Area               | Approach                                                | Expected Insights / Plots                         |
| ------------------------ | ------------------------------------------------------- | ------------------------------------------------- |
| **Time Series Analysis** | Line/bar plots of GHI, DNI, DHI, Tamb vs time           | Daily/seasonal trends, peaks, anomalies           |
| **Cleaning Impact**      | Compare ModA & ModB before/after cleaning               | Effectiveness of cleaning events                  |
| **Correlations**         | Heatmaps & scatter plots of GHI, DNI, DHI, TModA, TModB | Identify strong relationships                     |
| **Wind Patterns**        | Wind rose / radial plots                                | Variability and dominant directions               |
| **Temperature Analysis** | Scatter of Tamb vs RH or GHI                            | Relationship between humidity and solar radiation |
| **Bubble Chart**         | GHI vs Tamb (bubble = RH or BP)                         | Combined environmental visualization              |

**Outcome:**  
Each dataset is now clean, consistent, and ready for meaningful comparison and visualization.

---

## 4. Achievability & Forward Planning

### 🔸 Achievability

- **Data Availability:** Clean datasets already provided, minimizing preprocessing time.
- **Time Constraints:** Cleaning and EDA prioritized to meet deadlines.
- **Technical Readiness:** Environment validated with required Python packages.

---

### 🔸 Forward Planning

| Phase         | Actions                                              |
| ------------- | ---------------------------------------------------- |
| **Task 1**    | Completed — stable foundation for reproducibility    |
| **Task 2**    | Profile → Clean → Visualize in modular steps         |
| **Task 3**    | Reuse EDA outputs for cross-country comparison       |
| **Dashboard** | Begin parallel development to streamline integration |

---

### Mitigation of Challenges

- Addressed data inconsistencies using **median imputation** and **schema checks**
- Implemented **daily micro-milestones** for steady progress

**Outcome:**  
A structured, achievable workflow ensures smooth progression toward Week 0 objectives.
