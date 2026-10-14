# Student Performance Predictor

ML project using the UCI student dataset to predict final grades (G3). Started as coursework, then I kept adding a Streamlit frontend.

The model training notebook isn't in this repo yet (it's on my laptop). This is mostly the prediction UI with a simple placeholder formula so the form works.

## Stack
Python, pandas, scikit-learn, Streamlit, SHAP (when I get the real model loaded).

## Run it
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Stuff I learned
G2 (previous grade) dominates the predictions, which makes sense. Failures and absences matter too. SHAP took longer to set up than the model itself.

Test R² was around 0.87 on the held-out set when I ran the full pipeline. Still need to clean up the notebooks and push them.

Spring 2025, MSU Computational Data Science.