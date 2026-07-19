from typing import Any
import streamlit as st


def render_prediction_form() -> dict[str, Any] | None:
    st.subheader("Patient Risk Prediction")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", 1, 120, 50)
            sex = st.selectbox("Sex", [0, 1])
            cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
            dataset = st.selectbox("Dataset", [0, 1, 2, 3])
            trestbps = st.number_input("Resting BP", 50, 250, 120)
            chol = st.number_input("Cholesterol", 100, 700, 200)
            fbs = st.selectbox("Fasting Blood Sugar", [0, 1])

        with col2:
            restecg = st.selectbox("Rest ECG", [0, 1, 2])
            thalch = st.number_input("Max Heart Rate", 50, 250, 150)
            exang = st.selectbox("Exercise Angina", [0, 1])
            oldpeak = st.number_input("Old Peak", 0.0, 10.0, 1.0)
            slope = st.selectbox("Slope", [0, 1, 2])
            ca = st.selectbox("CA", [0, 1, 2, 3, 4])
            thal = st.selectbox("Thal", [0, 1, 2, 3])

        submitted = st.form_submit_button("Predict", use_container_width=True)

    if not submitted:
        return None

    return {
        "age": age, "sex": sex, "cp": cp, "dataset": dataset,
        "trestbps": trestbps, "chol": chol, "fbs": fbs,
        "restecg": restecg, "thalch": thalch, "exang": exang,
        "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal,
    }
