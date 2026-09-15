# MSBA 265 – Foundational Module 1: EDA, Data Dictionary & Outlier Pipeline

**Author:** Ziyan Chen

**Course:** MSBA 265 – Business Analytics Topics (Fall 2026)

**Instructor:** Shyla Solis

**Dataset:** French Motor Third-Party Liability Claims – `freMTPL2freq` (OpenML ID 41214)

This repository contains the full, reproducible workflow for Module 1: programmatic data
download, raw boundary audits, a Business Data Dictionary, distribution and correlation
plots with written interpretations, and a production Tukey 1.5 × IQR outlier-filtering script.

The final compiled report is **`Module1_Homework_Report.pdf`** in the repository root.

---

## Repository Structure

```
msba265-module1-ziyanchen/
|-- .gitignore                      # Excludes venv/, __pycache__/, checkpoint files
|-- README.md                       # Contains CLI setup and step-by-step execution guide
|-- requirements.txt                # Python dependencies (pandas, seaborn, etc.)
|-- Module1_Homework_Report.pdf     # Final compiled assignment PDF
|
|-- data/
|    |-- download_data.py           # Ingestion script
|    |-- raw_business_data.csv      # Fetch output
|    |-- cleaned_business_data.csv  # Outlier filter output
|
|-- notebooks/
|    |-- 01_eda_and_data_dictionary.ipynb   # Interactive Jupyter Notebook
|
|-- src/
|    |-- clean_outliers.py          # Production filtering pipeline
|
|-- reports/
|-- data_dictionary.csv             # Exported data dictionary artifact
`-- figures/
|-- feature_distributions.png       # Distribution plots artifact
`-- correlation_heatmap.png         # Heatmap artifact
```

---

## Prerequisites

- Python 3.10 or newer
- Git
- Visual Studio Code with the **Python** and **Jupyter** extensions (by Microsoft)

---

## Step-by-Step Reproduction Guide

### 1. Clone the repository

```bash
git clone https://github.com/ZiyanChen1/msba265-module1-ziyanchen.git
cd msba265-module1-ziyanchen
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

If PowerShell blocks the activation script, run this first, then activate again:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal prompt.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Download the raw dataset

Run from the **project root** (not from inside `data/`):

```bash
python data/download_data.py
```

Expected output:
```
[*] Extracting raw data from: https://www.openml.org/data/get_csv/20649148/freMTPL2freq.csv
[+] Saved locally to: data\raw_business_data.csv
[+] Record Count: 678013 rows x 12 columns
```

### 5. Run the EDA notebook

1. Open `notebooks/01_eda_and_data_dictionary.ipynb` in VS Code.
2. In the top-right corner, select the kernel **`venv`** (Python from this project's virtual environment).
3. Click **Run All**.

This regenerates:
- `reports/data_dictionary.csv`
- `reports/figures/correlation_heatmap.png`
- `reports/figures/feature_distributions.png`

### 6. Run the production outlier pipeline

Run from the **project root**:

```bash
python src/clean_outliers.py
```

Expected output:
```
==================================================
        PRODUCTION OUTLIER FILTERING REPORT
==================================================
Target Feature Filtered: Density
Initial Dataset Records: 678,013
Tukey IQR Valid Range:   [-2257.00, 4007.00]
Outlier Records Removed: 77,566 (11.44%)
Final Cleaned Records:   600,447

[+] Saved cleaned dataset artifact to: data\cleaned_business_data.csv
```

### 7. View the final report

Open `Module1_Homework_Report.pdf` in the repository root, or download it directly from GitHub.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `FileNotFoundError: Raw data missing` | Run `python data/download_data.py` first, from the project root. |
| `ModuleNotFoundError: No module named 'pandas'` | Make sure `(venv)` is active, then re-run `pip install -r requirements.txt`. |
| Notebook cannot find `../data/raw_business_data.csv` | Make sure Step 4 finished and the notebook kernel is set to `venv`. |
| `python` not recognized (Windows) | Use `py` instead of `python`, or reinstall Python with "Add to PATH" checked. |
| `python3` not found (macOS) | Install Python 3 from python.org or via Homebrew (`brew install python`). |

---

## Peer Reproduction Verification

A classmate has cloned this repository and successfully reproduced all outputs by following
the instructions above without additional help. The signed confirmation statement is included
in `PEER_VERIFICATION.md`.
