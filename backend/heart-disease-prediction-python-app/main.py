# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.heart_router import (
    router as heart_router
)

# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="Heart Disease Risk Prediction API",
    description="""
    Heart Disease Risk Prediction System

    Features:
    - Heart Disease Prediction
    - Batch Prediction
    - Dashboard Analytics
    - EDA Summary
    - Descriptive Analysis
    - Diagnostic Analysis
    - Predictive Analysis
    - Prescriptive Analysis
    - Risk Analysis
    - Executive Reporting
    """,
    version="1.0.0"
)

# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# =====================================================
# Register Routers
# =====================================================

app.include_router(
    heart_router
)

# =====================================================
# Root Endpoint
# =====================================================

@app.get("/")
def root():

    return {
        "application":
            "Heart Disease Risk Prediction",

        "version":
            "1.0.0",

        "status":
            "running"
    }

# =====================================================
# Health Check
# =====================================================

@app.get("/health")
def health():

    return {

        "status": "healthy",

        "service":
            "Heart Disease Risk Prediction API"
    }

