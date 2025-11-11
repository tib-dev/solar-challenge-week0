## 🧭 Conclusion & Observations  

### **Task 2: Data Profiling, Cleaning & EDA**

#### **Objective Recap**
The goal was to profile, clean, and explore each country’s solar dataset — **Benin**, **Sierra Leone**, and **Togo** — to ensure consistent and accurate data for regional comparison. Each dataset underwent descriptive analysis, anomaly detection, and exploratory visualization.

#### **Key Observations**
- **Data Quality & Cleaning:**  
  - Missing readings appeared mainly in `GHI`, `DNI`, and `DHI`. Median imputation was applied to preserve realistic patterns.  
  - Outlier detection via Z-score filtering (`|Z| > 3`) flagged abnormal sensor spikes in irradiance and wind data; removing these improved signal stability in module temperature plots (`ModA`, `ModB`).  
  - After cleaning, daily GHI and temperature cycles became smoother and more representative of true solar behavior.

- **Exploratory Insights:**  
  - Time-series charts showed clear diurnal peaks, with **Benin** typically recording the highest midday irradiance.  
  - Correlation heatmaps confirmed strong positive relations among `GHI`, `DNI`, and ambient temperature (`Tamb`), while **relative humidity (RH)** had a negative correlation — moisture reduces solar intensity.  
  - Wind analysis revealed moderate speeds across regions, consistent prevailing directions, and a weak correlation between wind gusts and irradiance.  
  - Humid conditions in **Sierra Leone** corresponded with lower irradiance, validated by bubble plots (`GHI vs Tamb`, bubble = RH).

#### **Cleaning Impact**
Post-cleaning averages of `ModA` and `ModB` readings aligned more closely, and anomalies diminished, confirming the success of the cleaning process.

---

### **Task 3: Cross-Country Comparison**

#### **Objective Recap**
Using the cleaned datasets, the objective was to compare solar metrics (`GHI`, `DNI`, `DHI`) across countries to evaluate solar potential and regional variability.

#### **Findings**
- **Boxplot Analysis:**  
  Each country exhibited distinct GHI distributions. **Benin** showed the highest median and spread, **Sierra Leone** the lowest overall irradiance, and **Togo** moderate but more consistent levels.  

- **Summary Table:**  
  Benin’s averages were consistently above others for `GHI` and `DNI`, indicating higher direct solar radiation potential.  
  Sierra Leone showed higher diffuse radiation (`DHI`) due to greater humidity and cloud cover.  

- **Statistical Testing:**  
  A one-way **ANOVA** returned a *p-value < 0.05*, confirming statistically significant differences in mean `GHI` across the countries.  
  The **Kruskal–Wallis** test produced a similar result, reinforcing robustness.  

- **Ranking (Average GHI):**  
  1. **Benin** — highest solar potential  
  2. **Togo** — moderate but stable irradiance  
  3. **Sierra Leone** — lowest direct solar exposure (likely from coastal cloud cover)

#### **Interpretation**
- **Benin** is best suited for high-capacity solar farm deployment.  
- **Togo** is favorable for consistent grid-support projects where reliability is key.  
- **Sierra Leone** may require hybrid or storage-integrated systems to offset lower irradiance.  

---

### **📊 Overall Insights**
- Data cleaning directly enhanced the credibility of cross-country comparisons.  
- Climate factors such as humidity and cloud cover clearly influence irradiance variability.  
- The integrated workflow — from EDA to statistical testing — demonstrates a complete, data-driven approach for **solar resource assessment and ranking**.  

---

### **✅ Key Performance Indicators (KPIs) Achieved**
- ✔️ Full profiling of missing values, outliers, and correlations  
- ✔️ Cleaned datasets (`data/<country>_clean.csv`) for all three countries  
- ✔️ Inclusion of all countries in comparative visuals  
- ✔️ Reported p-values from both ANOVA and Kruskal–Wallis tests  
- ✔️ Actionable insights linking data patterns to solar potential and design priorities  

---

### **🔭 Future Work**
- Extend analysis to **seasonal and yearly solar variability**.  
- Integrate **PV yield modeling** for each country using tools like PVLib or SAM.  
- Deploy a **Streamlit dashboard** to visualize solar potential interactively.  
