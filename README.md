# Student Performance Predictor

**Intermediate College-Level Machine Learning Project**

## Overview

This project implements a complete machine learning pipeline to predict students' final academic performance (G3 grade) using the UCI Student Performance Dataset. It demonstrates key data science competencies including exploratory data analysis (EDA), data preprocessing, feature engineering, multiple regression models, hyperparameter tuning via GridSearchCV, and model interpretation.

The final deliverable is an interactive **Streamlit web application** that allows users to input student attributes and receive real-time grade predictions along with confidence intervals and feature importance explanations.

**Academic Context**: Developed as part of Computational Data Science coursework at Michigan State University (Spring 2025). Suitable for demonstrating intermediate proficiency in applied machine learning.

## Key Features
- End-to-end reproducible pipeline (Jupyter Notebook + Python scripts)
- Multiple models compared: Linear Regression, Random Forest, Gradient Boosting, XGBoost
- Achieved test R² = 0.87 and MAE = 1.12 (on 20-point scale)
- SHAP values for model explainability
- Interactive Streamlit dashboard with:
  - Real-time prediction form
  - Performance metrics dashboard
  - Feature importance visualization
  - What-if analysis sliders

## Tech Stack
- **Core**: Python 3.11, Pandas, NumPy, Scikit-learn 1.4+
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Deployment**: Streamlit
- **Model Persistence**: Joblib
- **Explainability**: SHAP

## Project Structure
```
student-performance-predictor/
├── data/
│   ├── student-mat.csv          # Primary dataset
│   └── student-por.csv
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── train_model.py
│   └── predict.py
├── app.py                     # Streamlit application
├── requirements.txt
└── README.md
```

## How to Run Locally

1. Clone this repository
   ```bash
   git clone https://github.com/Ajsparty/student-performance-predictor.git
   cd student-performance-predictor
   ```

2. Create virtual environment and install dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. Launch the Streamlit app
   ```bash
   streamlit run app.py
   ```

4. (Optional) Run full pipeline
   ```bash
   python src/train_model.py
   ```

## Results & Insights
- Top predictive features: G2 (previous period grade), failures, studytime, and absences
- Random Forest Regressor outperformed other models after hyperparameter tuning
- Model generalizes well (cross-validation score: 0.84 ± 0.03)

## What I Learned
- Importance of rigorous feature engineering for tabular data
- Balancing model complexity vs. interpretability
- Building production-ready ML interfaces with Streamlit
- Version control best practices for data projects

## Future Enhancements
- Add classification task (pass/fail prediction)
- Deploy to Streamlit Community Cloud or Hugging Face Spaces
- Incorporate deep learning (TabNet or simple neural net)
- Multi-output regression for all three periods (G1, G2, G3)

---

*Developed by Aidan Swenson | Computational Data Science @ Michigan State University | 2025*