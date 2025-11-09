# Solar Data Dashboard Scripts

## Description
This folder contains supporting scripts for the Solar Energy Metrics Dashboard built with Streamlit.  
The dashboard visualizes Global, Direct, and Diffuse Horizontal Irradiance (GHI, DNI, DHI) metrics across different countries.

## Running the App
```bash
# 1. Activate your environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 2. Install dependencies
pip install streamlit pandas plotly

# 3. Run the app
streamlit run app/main.py
