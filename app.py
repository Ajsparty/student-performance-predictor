# Streamlit App for Student Performance Prediction
# Placeholder for full implementation - run with: streamlit run app.py

import streamlit as st
st.set_page_config(page_title="Student Performance Predictor", layout="wide")
st.title("Student Performance Predictor")
st.write("This is a demo interface for the ML model. Full implementation includes trained model loading and interactive predictions.")

# Demo form
with st.form("prediction_form"):
    st.subheader("Enter Student Details")
    studytime = st.slider("Weekly Study Time (hours)", 1, 10, 4)
    failures = st.number_input("Number of Past Failures", 0, 5, 0)
    absences = st.slider("Absences", 0, 93, 5)
    g2 = st.slider("Second Period Grade (G2)", 0, 20, 12)
    
    submitted = st.form_submit_button("Predict Final Grade (G3)")
    
if submitted:
    # Placeholder prediction logic
    predicted_g3 = max(0, min(20, g2 * 0.85 + studytime * 0.4 - failures * 1.2 - absences * 0.08 + 2))
    st.success(f"Predicted Final Grade (G3): {predicted_g3:.1f} / 20")
    st.info("In the full version, this uses a loaded Random Forest model with SHAP explanations.")