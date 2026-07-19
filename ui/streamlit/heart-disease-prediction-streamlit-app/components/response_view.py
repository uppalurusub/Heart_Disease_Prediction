from typing import Any
import pandas as pd
import plotly.express as px
import streamlit as st

from utils.formatters import format_percent, format_number


def render_kpis(data: dict[str, Any]) -> None:
    kpis = data.get("kpis", {})
    cols = st.columns(5)
    values = [
        ("Total Patients", format_number(kpis.get("total_patients", 0))),
        ("High Risk", format_number(kpis.get("high_risk_patients", 0))),
        ("Disease Rate %", format_percent(kpis.get("heart_disease_rate", 0))),
        ("Accuracy %", format_percent(kpis.get("model_accuracy", 0))),
        ("ROC-AUC %", format_percent(kpis.get("model_auc", 0))),
    ]
    for col, (label, value) in zip(cols, values):
        col.metric(label, value)


def render_risk_segmentation(data: dict[str, Any]) -> None:
    df = pd.DataFrame({
        "Risk Level": ["High", "Medium", "Low"],
        "Patients": [data.get("high_risk", 0), data.get("medium_risk", 0), data.get("low_risk", 0)],
    })
    fig = px.pie(df, values="Patients", names="Risk Level", title="Risk Distribution", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)


def render_feature_importance(data: dict[str, Any]) -> None:
    features = data.get("top_risk_factors", {})
    if not features:
        st.info("No feature importance data available.")
        return
    df = pd.DataFrame(features)
    fig = px.bar(df, x="importance", y="feature", orientation="h", title="Top Risk Factors")
    st.plotly_chart(fig, use_container_width=True)


def render_descriptive(data: dict[str, Any]) -> None:
    st.subheader("📊 Descriptive Analysis")
    cols = st.columns(4)
    metrics = [
        ("Average Age", f"{data.get('average_age', 0):.1f} Years"),
        ("Average Cholesterol", f"{data.get('average_cholesterol', 0):.1f}"),
        ("Average Resting BP", f"{data.get('average_resting_bp', 0):.1f}"),
        ("Heart Disease Rate", format_percent(data.get("heart_disease_rate", 0))),
    ]
    for col, (label, value) in zip(cols, metrics):
        col.metric(label, value)


def render_diagnostic(data: dict[str, Any]) -> None:
    st.subheader("🔍 Diagnostic Analysis")
    st.markdown("### Root Causes")
    for item in data.get("root_causes", []):
        st.error(item)
    st.markdown("### Key Insights")
    for item in data.get("insights", []):
        st.info(item)
    st.markdown("### Recommended Actions")
    for item in data.get("actions", []):
        st.success(item)


def render_predictive(data: dict[str, Any]) -> None:
    st.subheader("📈 Predictive Analysis")
    col1, col2 = st.columns(2)
    col1.metric("Expected High Risk Growth", data.get("high_risk_growth", "0%"))
    col2.metric("Forecast Status", "Increasing Risk")
    st.markdown("### Forecast")
    st.warning(data.get("forecast", "No Forecast Available"))


def render_recommendations(data: dict[str, Any]) -> None:
    st.subheader("💡 Recommendations")
    columns = st.columns(3)
    sections = [
        ("### 🏥 Clinical", "clinical", st.success),
        ("### ⚙️ Operational", "operational", st.info),
        ("### 💰 Financial", "financial", st.warning),
    ]
    for col, (title, key, renderer) in zip(columns, sections):
        with col:
            st.markdown(title)
            for item in data.get(key, []):
                renderer(item)


def render_executive_summary(summary: dict[str, Any]) -> None:
    st.subheader("📋 Executive Summary")
    st.markdown(f"### {summary.get('project', '')}\n\n**Objective**\n\n{summary.get('objective', '')}")
    st.divider()

    performance = summary.get("model_performance", {})
    col1, col2 = st.columns(2)
    col1.metric("Model Accuracy", format_percent(performance.get("accuracy", 0)))
    col2.metric("ROC-AUC", format_percent(performance.get("auc", 0)))
    st.divider()

    st.markdown("### 🎯 Top Risk Factors")
    factors = summary.get("top_factors", [])
    if factors:
        for col, factor in zip(st.columns(len(factors)), factors):
            col.metric("Risk Factor", factor)
    else:
        st.info("No top risk factors available.")

    st.divider()
    st.markdown("### 🚀 Expected Benefit")
    st.success(summary.get("expected_benefit", ""))


def render_prediction_result(result: dict[str, Any]) -> None:
    st.success(f"Risk Level: {result.get('risk_level', 'Unknown')}")
    st.metric("Risk Score", format_percent(result.get("risk_score", 0)))
