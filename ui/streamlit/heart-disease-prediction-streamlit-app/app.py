import requests
import streamlit as st

from api.heart_api import get_data
from components.response_view import render_kpis
from components.sidebar import render_sidebar
from pages import analytics, executive, feature_importance, prediction, risk_segments


st.set_page_config(
    page_title="Heart Disease Risk Prediction",
    page_icon="❤️",
    layout="wide",
)


def main() -> None:
    render_sidebar()
    st.title("❤️ Heart Disease Risk Prediction Dashboard")

    try:
        render_kpis(get_data("dashboard"))
    except requests.RequestException as exc:
        st.error(f"Dashboard API error: {exc}")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Risk Segments",
        "Feature Importance",
        "Analytics",
        "Prediction",
        "Executive",
    ])

    page_renderers = [
        (tab1, risk_segments.render),
        (tab2, feature_importance.render),
        (tab3, analytics.render),
        (tab4, prediction.render),
        (tab5, executive.render),
    ]

    for tab, renderer in page_renderers:
        with tab:
            try:
                renderer()
            except requests.RequestException as exc:
                st.error(f"API request failed: {exc}")


if __name__ == "__main__":
    main()
