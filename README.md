# Student Performance Predictor

A machine learning application that predicts student academic performance (final grade G3) using the UCI Student Performance dataset.

Features an interactive Streamlit interface for inputting student attributes and generating predictions, with support for model interpretability via SHAP.

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- SHAP

## Setup and Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Model Details
Random Forest regressor achieving approximately R² = 0.87 on held-out data. Key features include previous grades, study time, and absences. Full training pipeline and notebooks available upon request or in future updates.

Developed as a practical data science application for educational analytics.