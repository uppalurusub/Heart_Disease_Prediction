# app/services/heart_service.py

from implementations.heart_impl import (
    HeartImplementation
)


class HeartService:

    def __init__(self):

        self.impl = HeartImplementation()

    # =====================================================
    # Prediction APIs
    # =====================================================

    def predict(self, payload: dict):

        return self.impl.predict(payload)

    def batch_predict(self, records: list):

        return self.impl.batch_predict(records)

    # =====================================================
    # Dashboard
    # =====================================================

    def dashboard(self):

        return self.impl.dashboard()

    # =====================================================
    # EDA Summary
    # =====================================================

    def eda_summary(self):

        return self.impl.eda_summary()

    # =====================================================
    # Descriptive Analysis
    # =====================================================

    def descriptive_analysis(self):

        return self.impl.descriptive_analysis()

    # =====================================================
    # Diagnostic Analysis
    # =====================================================

    def diagnostic_analysis(self):

        return self.impl.diagnostic_analysis()

    # =====================================================
    # Predictive Analysis
    # =====================================================

    def predictive_analysis(self):

        return self.impl.predictive_analysis()

    # =====================================================
    # Prescriptive Analysis
    # =====================================================

    def prescriptive_analysis(self):

        return self.impl.prescriptive_analysis()

    # =====================================================
    # Risk Analysis
    # =====================================================

    def risk_analysis(self):

        return self.impl.risk_analysis()

    # =====================================================
    # KPI Dashboard
    # =====================================================

    def kpis(self):

        return self.impl.kpis()

    # =====================================================
    # Feature Importance
    # =====================================================

    def feature_importance(self):

        return self.impl.feature_importance_report()

    # =====================================================
    # Patient Segmentation
    # =====================================================

    def patient_segments(self):

        return self.impl.patient_segments()

    # =====================================================
    # Recommendations
    # =====================================================

    def recommendations(self):

        return self.impl.recommendations()

    # =====================================================
    # Executive Summary
    # =====================================================

    def executive_summary(self):

        return self.impl.executive_summary()