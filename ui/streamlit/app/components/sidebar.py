import streamlit as st


def render_sidebar() -> None:
    with st.sidebar:
        st.title("❤️ Heart Analytics")
        st.caption("Heart Disease Risk Prediction")
        st.info("Use the dashboard tabs to review risk, analytics, predictions, and executive insights.")
