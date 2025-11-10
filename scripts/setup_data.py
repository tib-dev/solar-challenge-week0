"""
scripts/setup_data.py

Purpose:
--------
Sets up the data environment for the Solar Challenge project.
Ensures that necessary folders exist, verifies dependencies,
and prepares placeholder data structure for processing.

Usage:
------
$ python scripts/setup_data.py
"""

import os
from pathlib import Path
import sys

# -------------------------------
# 1. Define core directories
# -------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
ARCHIVE_DIR = DATA_DIR / "archive"
METADATA_DIR = DATA_DIR / "metadata"
SAMPLES_DIR = DATA_DIR / "samples"

COUNTRIES = ["benin", "togo", "sierra_leone"]

# -------------------------------
# 2. Helper functions
# -------------------------------
def create_directories():
    """Create core project directories if missing."""
    dirs = [DATA_DIR, RAW_DIR, PROCESSED_DIR, ARCHIVE_DIR, METADATA_DIR, SAMPLES_DIR]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    print("✅ Directory structure initialized.")

def create_country_placeholders():
    """Create placeholder CSVs for each country if not found."""
    for country in COUNTRIES:
        processed_path = PROCESSED_DIR / f"{country}_clean.csv"
        if not processed_path.exists():
            processed_path.touch()
            print(f"📄 Created placeholder for {processed_path.name}")
    print("✅ Country placeholder files ready.")

def verify_environment():
    """Check essential packages are installed."""
    required = ["pandas", "numpy", "plotly", "streamlit"]
    missing = []
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print("⚠️ Missing dependencies:", ", ".join(missing))
        print("👉 Install them with: pip install -r requirements.txt")
    else:
        print("✅ All dependencies verified.")

def summarize_setup():
    """Summarize project structure."""
    print("\n📁 Project Structure Summary:")
    for path in [DATA_DIR, RAW_DIR, PROCESSED_DIR, ARCHIVE_DIR, METADATA_DIR, SAMPLES_DIR]:
        print(f" - {path.relative_to(PROJECT_ROOT)}")
    print("\nSetup completed successfully.")


# -------------------------------
# 3. Main Execution
# -------------------------------
if __name__ == "__main__":
    print("🚀 Initializing Solar Challenge Project Environment...\n")

    try:
        create_directories()
        create_country_placeholders()
        verify_environment()
        summarize_setup()
    except Exception as e:
        print("❌ Setup failed:", str(e))
        sys.exit(1)
