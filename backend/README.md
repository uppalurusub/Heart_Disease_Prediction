# ❤️ Heart Disease Risk Prediction System

A production-ready **Machine Learning + FastAPI** application that predicts the likelihood of heart disease using patient clinical information. The application follows a clean layered architecture with separate modules for API routing, business logic, preprocessing, model training, and inference.

---

# Overview

The Heart Disease Risk Prediction System provides REST APIs for predicting cardiovascular disease risk, performing exploratory data analysis (EDA), generating descriptive and diagnostic analytics, and serving executive dashboard metrics.

The system is designed using:

- FastAPI
- Scikit-Learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib
- Pydantic

---

# Features

## Machine Learning

- Heart Disease Prediction
- Batch Prediction
- Risk Probability Calculation
- Risk Score Generation
- Feature Importance
- Model Serialization
- Preprocessing Pipeline
- Random Forest Classification

---

## REST APIs

- Single Prediction
- Batch Prediction
- Dashboard
- EDA Summary
- Descriptive Analysis
- Diagnostic Analysis
- Predictive Analysis
- Prescriptive Analysis
- Risk Analysis
- Executive Reporting

---

## Data Processing

- Missing Value Handling
- Numerical Feature Scaling
- Categorical Encoding
- Data Validation
- Automatic ID Column Removal
- Data Transformation Pipeline

---

## Model Training

- Dataset Loading
- Feature Engineering
- Train/Test Split
- Model Training
- Performance Evaluation
- Model Saving
- Preprocessor Saving

---

# Project Structure

```
heart-disease-prediction-python-app/
│
├── config/
│   └── settings.py
│
├── implementations/
│   └── heart_impl.py
│
├── models/
│   └── train_model.py
│
├── routers/
│   └── heart_router.py
│
├── schemas/
│   └── prediction_request.py
│
├── services/
│   └── heart_service.py
│
├── utils/
│   ├── data_loader.py
│   └── preprocessing.py
│
├── data/
│   └── heart_disease.csv
│
├── outputs/
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

# Architecture

```
               Client
                  │
                  ▼
           FastAPI Router
                  │
                  ▼
            Service Layer
                  │
                  ▼
       Business Implementation
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
 Machine Learning       Analytics Engine
      ▼                       ▼
 Preprocessor          Dashboard APIs
      ▼
 Trained Model
```

---

# Technology Stack

| Technology | Purpose |
|------------|----------|
| Python 3.10+ | Programming Language |
| FastAPI | REST API |
| Scikit-Learn | Machine Learning |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Joblib | Model Serialization |
| Pydantic | Request Validation |
| Uvicorn | API Server |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git

cd heart-disease-prediction
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Train the Machine Learning Model

Run

```bash
python models/train_model.py
```

This generates:

```
models/
    heart_model.pkl
    preprocessor.pkl
    feature_importance.pkl
```

---

# Run the API

```bash
uvicorn main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

## Prediction APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /heart/predict | Predict Heart Disease |
| POST | /heart/batch-predict | Batch Prediction |

---

## Analytics APIs

| Method | Endpoint |
|----------|-----------------------------|
| GET | /heart/dashboard |
| GET | /heart/eda-summary |
| GET | /heart/descriptive-analysis |
| GET | /heart/diagnostic-analysis |
| GET | /heart/predictive-analysis |
| GET | /heart/prescriptive-analysis |
| GET | /heart/risk-analysis |
| GET | /heart/executive-report |

---

# Sample Prediction Request

```json
{
    "age": 58,
    "sex": 1,
    "dataset": 0,
    "cp": 2,
    "trestbps": 140,
    "chol": 250,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.2,
    "slope": 1,
    "ca": 0,
    "thal": 2
}
```

---

# Sample Response

```json
{
    "prediction": 1,
    "risk_probability": 0.87,
    "risk_score": "High",
    "prediction_time": "2026-07-19T09:00:00"
}
```

---

# Machine Learning Pipeline

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Missing Value Imputation
   │
   ▼
Categorical Encoding
   │
   ▼
Feature Scaling
   │
   ▼
Train/Test Split
   │
   ▼
Random Forest Training
   │
   ▼
Model Evaluation
   │
   ▼
Save Model (.pkl)
```

---

# Evaluation Metrics

The training module evaluates the model using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

---

# Request Validation

The application validates every request using **Pydantic**.

Examples include:

- Age Range
- Blood Pressure Range
- Cholesterol Range
- Chest Pain Type
- Blood Sugar
- ECG Results
- Exercise Induced Angina
- Maximum Heart Rate

Invalid requests automatically return descriptive validation errors.

---

# Design Patterns Used

- Layered Architecture
- Service Layer Pattern
- Dependency Separation
- Data Validation Pattern
- ML Pipeline Pattern

---

# Advantages

- Modular Design
- Easily Extendable
- Production Ready
- Strong Input Validation
- Reusable Services
- Scalable Architecture
- Machine Learning Pipeline
- RESTful APIs
- Swagger Documentation

---

# Future Enhancements

- XGBoost Model
- LightGBM
- CatBoost
- Explainable AI (SHAP)
- MLflow Integration
- Docker Support
- Kubernetes Deployment
- Authentication
- Database Integration
- CI/CD Pipeline
- Model Monitoring
- Drift Detection
- Automated Retraining

---

# Author

Developed using:

- Python
- FastAPI
- Scikit-Learn
- Machine Learning
- REST API Development

---

# License

This project is intended for educational, research, and demonstration purposes.