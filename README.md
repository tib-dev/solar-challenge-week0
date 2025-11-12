# AI Mastery: Solar Data Discovery - Week 0 Challenge

Kickstart your AI Mastery with cross-country solar farm analysis from Benin, Sierra Leone, and Togo. This project focuses on understanding, exploring, and analyzing solar farm data to identify trends, high-potential regions, and actionable insights for MoonLight Energy Solutions.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Objective](#business-objective)
- [Dataset Overview](#dataset-overview)
- [Folder Structure](#folder-structure)
- [Setup & Installation](#setup--installation)
- [Tasks Completed](#tasks-completed)
- [Technologies Used](#technologies-used)
- [Key Observations](#key-observations)

---

## Project Overview

Week 0 challenge for AI Mastery focuses on end-to-end solar data analysis:

- Data profiling, cleaning, and exploratory analysis (EDA)
- Cross-country comparison of solar metrics
- Optional interactive dashboard with Streamlit

The project uses real solar radiation datasets from Benin, Sierra Leone, and Togo.

---

## Business Objective

MoonLight Energy Solutions seeks to enhance operational efficiency and sustainability via targeted solar investments. Your task is to analyze environmental measurements and provide actionable insights for identifying high-potential solar installation regions.

---

## Dataset Overview

The dataset contains solar and environmental measurements:

| Column              | Description                               |
| ------------------- | ----------------------------------------- |
| Timestamp           | Date and time of observation              |
| GHI, DNI, DHI       | Solar radiation measurements (W/m²)       |
| ModA, ModB          | Module irradiance readings (W/m²)         |
| Tamb                | Ambient Temperature (°C)                  |
| RH                  | Relative Humidity (%)                     |
| WS, WSgust, WSstdev | Wind speed and variability (m/s)          |
| WD, WDstdev         | Wind direction and variability (°)        |
| BP                  | Barometric Pressure (hPa)                 |
| Precipitation       | Precipitation rate (mm/min)               |
| Cleaning            | Sensor/module cleaning flag (1 = cleaned) |
| TModA, TModB        | Module temperatures (°C)                  |
| Comments            | Additional notes                          |

Cleaned datasets are saved in `/data/processed/` (ignored in git).

---

## Project Structure

````text
solar-challenge-week0/
├── app/                   # Streamlit app and assets
│   ├── assets/            # Screenshots or static resources
│   ├── main.py            # Main Streamlit script
│   └── utils/             # App-specific utility functions
├── core/                  # Core modules for data processing and visualization
│   ├── eda.py
│   ├── pipeline.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── profiling.py
│   └── visualization.py
├── data/                  # Data folder
│   └── raw/               # Raw CSV files per country
│   └── processed/         # Cleaned CSV files per country
│   └── sample/            # Sample data for testing
├── notebook/              # Jupyter notebooks for EDA and country comparisons
│   ├── eda_benin.ipynb
│   ├── eda_sierra_leone.ipynb
│   ├── eda_togo.ipynb
│   └── compare_countries.ipynb
├── scripts/               # Automation scripts (data ingestion, setup)
├── tests/                 # Unit tests for core modules
├── requirements.txt       # Python dependencies
├── setup_env.sh           # Optional environment setup script
├── README.md              # Project overview and instructions
└── .gitignore             # Git ignore rules


---


## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/<username>/solar-challenge-week0.git
cd solar-challenge-week0

# Create a Python virtual environment
python -m venv venv
# Activate (Linux/Mac)
source venv/bin/activate
# Activate (Windows)
venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

# Run the Streamlit app

python -m streamlit run app/main.py


## Tasks Completed

### Task 1: Git & Environment Setup
- Repository initialized with `.gitignore`, `requirements.txt`, and CI workflow.
- Python virtual environment set up.

### Task 2: Data Profiling, Cleaning & EDA
- Country-specific notebooks for:
  - Benin
  - Sierra Leone
  - Togo
- Activities performed:
  - Summary statistics
  - Missing value handling
  - Outlier detection
  - Correlations
  - Visualizations

### Task 3: Cross-Country Comparison
- Compare solar metrics across countries.
- Methods used:
  - Boxplots
  - Summary tables
  - Statistical tests for GHI, DNI, DHI

### Bonus: Streamlit Dashboard
- Interactive visualization with country selection and metric display.
- Top regions summary table integrated.

---

## Technologies Used
- Python 3.x
- Pandas, NumPy, Matplotlib, Seaborn, Plotly
- Streamlit for dashboard
- Git & GitHub Actions for version control and CI
- Jupyter Notebooks for EDA

---

## Key Observations
- Country X has the highest median GHI but also high variability.
- Cleaning events impact module irradiance noticeably.
- Wind and humidity patterns influence solar radiation differently across countries.
````
