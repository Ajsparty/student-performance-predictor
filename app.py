# streamlit app for the student grade predictor
# model isn't loaded yet, this is just the form with a rough formula so it does something

import streamlit as st
st.set_page_config(page_title="Student Performance Predictor", layout="wide")
st.title("Student Performance Predictor")
st.write("Demo UI. Full version loads a trained random forest and shows SHAP.")

with st.form("prediction_form"):
    st.subheader("Enter Student Details")
    studytime = st.slider("Weekly Study Time (hours)", 1, 10, 4)
    failures = st.number_input("Number of Past Failures", 0, 5, 0)
    absences = st.slider("Absences", 0, 93, 5)
    g2 = st.slider("Second Period Grade (G2)", 0, 20, 12)
    
    submitted = st.form_submit_button("Predict Final Grade (G3)")
    
if submitted:
    # placeholder until I push the real model
    predicted_g3 = max(0, min(20, g2 * 0.85 + studytime * 0.4 - failures * 1.2 - absences * 0.08 + 2))
    st.success(f"Predicted Final Grade (G3): {predicted_g3:.1f} / 20")
    st.info("This is a rough estimate. Real model is a tuned random forest.")