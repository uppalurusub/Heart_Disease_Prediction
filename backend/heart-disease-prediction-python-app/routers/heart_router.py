# app/routers/heart_router.py

from fastapi import APIRouter

from services.heart_service import (
    HeartService
)

from schemas.prediction_request import (
    HeartPredictionRequest
)

router = APIRouter(
    prefix="/heart",
    tags=["Heart Disease Prediction"]
)

service = HeartService()

# =====================================================
# Dashboard
# =====================================================

@router.get("/dashboard")
def dashboard():

    return service.dashboard()


# =====================================================
# EDA Summary
# =====================================================

@router.get("/eda-summary")
def eda_summary():

    return service.eda_summary()


# =====================================================
# Descriptive Analysis
# =====================================================

@router.get("/descriptive-analysis")
def descriptive_analysis():

    return service.descriptive_analysis()


# =====================================================
# Diagnostic Analysis
# =====================================================

@router.get("/diagnostic-analysis")
def diagnostic_analysis():

    return service.diagnostic_analysis()


# =====================================================
# Predictive Analysis
# =====================================================

@router.get("/predictive-analysis")
def predictive_analysis():

    return service.predictive_analysis()


# =====================================================
# Prescriptive Analysis
# =====================================================

@router.get("/prescriptive-analysis")
def prescriptive_analysis():

    return service.prescriptive_analysis()


# =====================================================
# Risk Analysis
# =====================================================

@router.get("/risk-analysis")
def risk_analysis():

    return service.risk_analysis()


# =====================================================
# KPI Dashboard
# =====================================================

@router.get("/kpis")
def kpis():

    return service.kpis()


# =====================================================
# Feature Importance
# =====================================================

@router.get("/feature-importance")
def feature_importance():

    return service.feature_importance()


# =====================================================
# Patient Segments
# =====================================================

@router.get("/patient-segments")
def patient_segments():

    return service.patient_segments()


# =====================================================
# Recommendations
# =====================================================

@router.get("/recommendations")
def recommendations():

    return service.recommendations()


# =====================================================
# Executive Summary
# =====================================================

@router.get("/executive-summary")
def executive_summary():

    return service.executive_summary()


# =====================================================
# Single Prediction
# =====================================================

@router.post("/predict")
def predict(
    payload: HeartPredictionRequest
):

    return service.predict(
        payload.model_dump()
    )


# =====================================================
# Batch Prediction
# =====================================================

@router.post("/batch-predict")
def batch_predict(
    payload: list[HeartPredictionRequest]
):

    records = [
        item.model_dump()
        for item in payload
    ]

    return service.batch_predict(
        records
    )