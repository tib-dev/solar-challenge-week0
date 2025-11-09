# 🌞 KAIM-8 — Week 0 Interim Report  
## Solar Data Discovery Challenge

---

## 1. Introduction
This interim report summarizes my **Week 0 plan and progress** for the *Solar Data Discovery Challenge*.  
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
