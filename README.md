# ❤️ Heart Disease Prediction System

## Overview

The **Heart Disease Prediction System** is an end-to-end Machine Learning application designed to predict the likelihood of heart disease using patient clinical information.

The solution consists of:

* **FastAPI Backend**

  * REST APIs
  * Machine Learning Prediction
  * Analytics Services
  * Dashboard APIs
  * Feature Importance
  * Risk Segmentation

* **React Frontend**

  * Modern TypeScript UI
  * Dashboard
  * Prediction Form
  * Analytics Visualization
  * API Integration

* **Streamlit Dashboard**

  * Executive Dashboard
  * Feature Importance
  * Risk Analysis
  * Prediction Interface

---

# Architecture

```
                   +----------------------+
                   |   React Frontend     |
                   |  (TypeScript + Vite) |
                   +----------+-----------+
                              |
                              |
                     REST API Calls
                              |
                              ▼
                 +------------------------+
                 |     FastAPI Backend    |
                 |------------------------|
                 | Prediction API         |
                 | Dashboard API          |
                 | Analytics API          |
                 | Feature Importance     |
                 | Risk Segmentation      |
                 +-----------+------------+
                             |
                             |
               +-------------+--------------+
               | Machine Learning Pipeline  |
               |----------------------------|
               | Preprocessor               |
               | Trained Model              |
               | Feature Importance         |
               +-------------+--------------+
                             |
                             ▼
                    Heart Disease Dataset
```

---

# Project Structure

```
Heart_Disease_Prediction/

│
├── backend/
│   │
│   ├── data/
│   │      heart_disease.csv
│   │
│   ├── models/
│   │      heart_model.pkl
│   │      preprocessor.pkl
│   │      feature_importance.pkl
│   │
│   └── heart-disease-prediction-python-app/
│          │
│          ├── config/
│          ├── implementations/
│          ├── models/
│          ├── routers/
│          ├── schemas/
│          ├── services/
│          ├── utils/
│          └── main.py
│
├── ui/
│
│   ├── reactjs/
│   │      heart-disease-prediction-react-app/
│   │
│   └── streamlit/
│          heart-disease-prediction-streamlit-app/
│
├── requirements.txt
└── README.md
```

---

# Technology Stack

## Backend

* Python
* FastAPI
* Scikit-Learn
* Pandas
* NumPy
* Joblib
* Pickle
* Uvicorn

---

## Frontend

* React 19
* TypeScript
* Vite
* Axios
* React Router
* Chart.js
* Recharts

---

## Streamlit

* Streamlit
* Plotly/Charts
* Pandas

---

# Features

## Prediction

* Individual Patient Prediction
* Disease Probability
* Risk Classification
* Confidence Score

---

## Dashboard

* Executive Dashboard
* KPI Dashboard
* Population Statistics
* Disease Distribution

---

## Analytics

### Exploratory Data Analysis

* Dataset Summary
* Missing Values
* Feature Distribution
* Correlation

---

### Descriptive Analytics

* Patient Demographics
* Clinical Statistics
* Heart Disease Distribution

---

### Diagnostic Analytics

* Root Cause Analysis
* Feature Relationships
* Clinical Insights

---

### Predictive Analytics

* ML Predictions
* Risk Scores
* Probability Distribution

---

### Risk Analytics

* Patient Risk Categories
* High Risk Population
* Moderate Risk Population
* Low Risk Population

---

### Feature Importance

* Most Important Clinical Features
* Model Explainability

---

### Patient Segmentation

* Risk Groups
* Population Clusters
* Health Categories

---

### Recommendations

* Lifestyle Recommendations
* Clinical Recommendations
* Preventive Measures

---

# Backend APIs

| Method | Endpoint                       | Description               |
| ------ | ------------------------------ | ------------------------- |
| GET    | `/heart/dashboard`             | Dashboard Summary         |
| GET    | `/heart/eda-summary`           | Exploratory Data Analysis |
| GET    | `/heart/descriptive-analysis`  | Descriptive Analytics     |
| GET    | `/heart/diagnostic-analysis`   | Diagnostic Analytics      |
| GET    | `/heart/predictive-analysis`   | Predictive Analytics      |
| GET    | `/heart/prescriptive-analysis` | Prescriptive Analytics    |
| GET    | `/heart/risk-analysis`         | Risk Analytics            |
| GET    | `/heart/kpis`                  | KPI Dashboard             |
| GET    | `/heart/feature-importance`    | Feature Importance        |
| GET    | `/heart/patient-segments`      | Risk Segmentation         |
| GET    | `/heart/recommendations`       | Clinical Recommendations  |
| GET    | `/heart/executive-summary`     | Executive Summary         |
| POST   | Prediction Endpoint            | Heart Disease Prediction  |

---

# Backend Setup

## 1. Clone Repository

```bash
git clone <repository_url>

cd Heart_Disease_Prediction
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start FastAPI

```bash
cd backend/heart-disease-prediction-python-app

uvicorn main:app --reload
```

Application

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# React Frontend

## Install

```bash
cd ui/reactjs/heart-disease-prediction-react-app

npm install
```

---

## Run

```bash
npm run dev
```

Application

```
http://localhost:5173
```

---

## Production Build

```bash
npm run build
```

---

## Preview

```bash
npm run preview
```

---

# Streamlit Dashboard

## Install

```bash
cd ui/streamlit/heart-disease-prediction-streamlit-app

pip install -r requirements.txt
```

---

## Run

```bash
streamlit run app.py
```

Application

```
http://localhost:8501
```

---

# Machine Learning Assets

The backend uses pre-trained models located in:

```
backend/models/
```

Included artifacts

* heart_model.pkl
* preprocessor.pkl
* feature_importance.pkl

These artifacts are automatically loaded during prediction.

---

# Input Features

Typical prediction inputs include clinical information such as:

* Age
* Gender
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* ST Depression
* ST Slope
* Number of Major Vessels
* Thalassemia

---

# Frontend Pages

## React

* Dashboard
* Prediction
* Analytics

---

## Streamlit

* Prediction
* Executive Dashboard
* Analytics
* Feature Importance
* Risk Segments

---

# API Workflow

```
User

↓

React UI

↓

Axios API

↓

FastAPI

↓

Preprocessor

↓

ML Model

↓

Prediction

↓

Response

↓

Dashboard/UI
```

---

# Future Enhancements

* Authentication & Authorization
* Model Monitoring
* MLflow Integration
* Explainable AI (SHAP/LIME)
* Docker Support
* Kubernetes Deployment
* CI/CD Pipeline
* Cloud Deployment (Azure/AWS/GCP)
* Batch Prediction
* Model Versioning
* Real-Time Monitoring
* PDF Report Generation

---

# License

This project is intended for educational, research, and healthcare analytics purposes. Ensure appropriate clinical validation before using predictions in real-world medical decision-making.

---

# Author

**Heart Disease Prediction System**

A full-stack Machine Learning solution combining **FastAPI**, **React**, and **Streamlit** to deliver intelligent heart disease risk prediction, interactive dashboards, analytics, and clinical decision support.
