import requests
import streamlit as st

from api.heart_api import predict_patient
from components.request_form import render_prediction_form
from components.response_view import render_prediction_result


def render() -> None:
    payload = render_prediction_form()
    if payload is None:
        return

    try:
        with st.spinner("Predicting patient risk..."):
            result = predict_patient(payload)
        render_prediction_result(result)
    except requests.RequestException as exc:
        st.error(f"Prediction API error: {exc}")
