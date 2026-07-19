# Heart Disease Clinical Analytics & AI Prediction Dashboard

A modern **React.js + TypeScript healthcare analytics application** for exploring heart disease data, analyzing clinical risk factors, visualizing healthcare KPIs, and performing AI-powered heart disease risk prediction.

The frontend integrates with a **FastAPI backend** and dynamically retrieves the prediction request schema from the FastAPI OpenAPI specification. This reduces frontend/backend request mismatches and helps prevent `422 Unprocessable Entity` errors caused by missing prediction fields.

---

## Overview

The **Heart Disease Clinical Analytics & AI Prediction Dashboard** provides an interactive user interface for:

* Heart disease analytics
* Exploratory Data Analysis (EDA)
* Descriptive analytics
* Diagnostic analytics
* Predictive analytics
* Prescriptive analytics
* Clinical risk analysis
* Healthcare KPI monitoring
* Feature importance analysis
* Patient segmentation
* Clinical recommendations
* Executive summaries
* AI-powered heart disease risk prediction

The application uses reusable React components to automatically transform API JSON responses into:

* KPI cards
* Metric cards
* Bar charts
* Donut charts
* Risk priority bars
* Progress indicators
* Responsive tables
* Numbered clinical insight lists
* Nested analytics sections

---

# Key Features

## Heart Disease Analytics Dashboard

The dashboard retrieves heart disease analytics from the backend and automatically renders the response using reusable visualization components.

The dashboard supports:

* Patient population metrics
* Heart disease distribution
* Risk-group analysis
* Clinical performance metrics
* Model performance indicators
* Healthcare KPIs

---

## Exploratory Data Analysis

The EDA module provides summarized information about the heart disease dataset.

Supported endpoint:

```text
GET /heart/eda-summary
```

The interface automatically displays structured JSON responses using cards, tables, charts, and analytics sections.

---

## Descriptive Analytics

Provides statistical summaries describing the patient population and clinical attributes.

Supported endpoint:

```text
GET /heart/descriptive-analysis
```

Example analytical areas may include:

* Patient demographics
* Age distribution
* Blood pressure statistics
* Cholesterol statistics
* Heart rate characteristics
* Clinical attribute distributions

---

## Diagnostic Analytics

Diagnostic analytics helps identify possible factors associated with heart disease.

Supported endpoint:

```text
GET /heart/diagnostic-analysis
```

The application can display:

* Clinical risk factors
* Risk scores
* Disease-associated attributes
* Patient risk characteristics
* Diagnostic findings

Risk-related numeric data is automatically sorted from highest to lowest priority.

---

## Predictive Analytics

The predictive analytics module displays model-generated analytical insights.

Supported endpoint:

```text
GET /heart/predictive-analysis
```

The frontend supports visualization of:

* Prediction rates
* Model accuracy
* AUC metrics
* Patient risk volumes
* Model performance indicators

Performance values are displayed using visual progress indicators.

---

## Prescriptive Analytics

Provides actionable clinical or healthcare recommendations based on analytical results.

Supported endpoint:

```text
GET /heart/prescriptive-analysis
```

Recommendations returned as arrays are automatically rendered as structured numbered insight lists.

---

## Clinical Risk Analysis

The Risk Analysis module displays prioritized heart disease risk factors.

Supported endpoint:

```text
GET /heart/risk-analysis
```

Risk factors are automatically:

1. Converted into readable labels
2. Sorted by numeric risk value
3. Ranked from highest to lowest
4. Displayed using priority bars

Example:

```text
#1 Chest Pain Risk
Highest Priority

#2 Cholesterol Risk
High Priority

#3 Blood Pressure Risk
Priority Risk Factor
```

Priority visualization uses different risk severity styles.

---

## Healthcare KPI Dashboard

The KPI module provides healthcare and model performance indicators.

Supported endpoint:

```text
GET /heart/kpis
```

Numeric values are automatically categorized into:

### Patient and Clinical Counts

Examples:

* Total Patients
* High Risk Patients
* Moderate Risk Patients
* Low Risk Patients

These values are displayed using:

* Metric cards
* Patient Risk Overview bar chart

### Performance Metrics

Examples:

* Prediction Accuracy
* Heart Disease Rate
* Model AUC
* Risk Percentage

Performance metrics are displayed using progress bars and qualitative performance indicators.

Example classifications:

```text
>= 90%    Excellent
>= 80%    Strong
>= 70%    Good
< 70%     Needs Attention
```

---

## Feature Importance Analysis

Displays model feature importance information.

Supported endpoint:

```text
GET /heart/feature-importance
```

The visualization framework automatically renders feature importance values using prioritized risk-style bars when the API response contains numeric feature scores.

---

## Patient Segmentation

Provides patient grouping and segmentation analytics.

Supported endpoint:

```text
GET /heart/patient-segments
```

Patient segmentation information may include:

* Low-risk patients
* Moderate-risk patients
* High-risk patients
* Heart disease patients
* Healthy patients
* Clinical risk cohorts

Structured arrays are displayed using responsive data tables.

---

## Clinical Recommendations

Displays clinical and analytical recommendations.

Supported endpoint:

```text
GET /heart/recommendations
```

Recommendations are displayed as readable numbered cards instead of raw JSON.

Example:

```text
1. Monitor patients with elevated cholesterol levels.

2. Prioritize high-risk patients for cardiovascular screening.

3. Evaluate patients with exercise-induced angina.

4. Monitor abnormal resting blood pressure.
```

---

## Executive Summary

Provides a high-level analytical summary suitable for healthcare leadership and decision-makers.

Supported endpoint:

```text
GET /heart/executive-summary
```

The reusable response visualization engine automatically converts nested API responses into executive dashboard sections.

---

# AI Heart Disease Risk Prediction

The application provides an interactive clinical prediction form.

Supported endpoint:

```text
POST /heart/predict
```

The prediction page does **not hardcode the request fields**.

Instead, the React application retrieves the FastAPI OpenAPI schema.

```text
GET /openapi.json
```

The application reads the request model associated with:

```text
/heart/predict
```

The prediction request schema is dynamically discovered from:

```text
components.schemas
```

This enables the frontend to generate prediction form fields directly from the FastAPI request model.

---

## Dynamic FastAPI Schema Integration

The prediction page performs the following workflow:

```text
React Prediction Page
        |
        v
GET /openapi.json
        |
        v
Find /heart/predict
        |
        v
Read POST requestBody
        |
        v
Resolve JSON Schema $ref
        |
        v
Load FastAPI Request Model
        |
        v
Generate React Form Fields
        |
        v
Submit Prediction Request
```

This architecture significantly reduces request schema mismatch issues.

For example:

```text
422 Unprocessable Entity
```

may occur when required fields are missing from a prediction payload.

By reading the FastAPI OpenAPI schema, the frontend automatically identifies required fields.

---

# Prediction Form Features

The prediction form supports:

* Dynamic field generation
* Required field detection
* Numeric input fields
* String input fields
* Enum-based dropdown fields
* Minimum values
* Maximum values
* Default values
* FastAPI schema synchronization

Required fields are visually identified using:

```text
*
```

Example:

```text
Age *
Sex *
Chest Pain Type *
Resting Blood Pressure *
Cholesterol *
```

---

# Prediction Error Handling

FastAPI validation errors are automatically parsed.

Example FastAPI validation response:

```json
{
  "detail": [
    {
      "loc": [
        "body",
        "age"
      ],
      "msg": "Field required"
    }
  ]
}
```

The React application converts the error into a readable message.

Example:

```text
Prediction Request Error

age: Field required
```

Multiple FastAPI validation errors are combined and displayed in the error banner.

---

# Data Visualization

The application uses **Recharts** for healthcare analytics visualization.

Supported visualizations include:

* Bar charts
* Donut charts
* Progress bars
* Risk priority bars
* KPI cards
* Metric cards
* Responsive tables

---

## Heart Disease Target Distribution

Heart disease target distribution is displayed using a donut chart.

Example categories:

```text
Heart Disease
Healthy
```

The center of the chart displays:

```text
Total Patients
```

The distribution summary displays:

```text
Heart Disease    526
54.7% of patients

Healthy          435
45.3% of patients
```

The chart is automatically displayed when the API response contains a target distribution section.

---

## Patient Risk Overview

Patient count KPIs are displayed using a Recharts bar chart.

Example metrics:

```text
Total Patients
High Risk Patients
Moderate Risk Patients
Low Risk Patients
```

Each bar uses a distinct visualization color.

Numeric values are displayed above the bars using `LabelList`.

---

## Clinical Risk Priority Visualization

Risk values are automatically sorted in descending order.

Example:

```text
Highest Risk
    |
    v
#1 Risk Factor
#2 Risk Factor
#3 Risk Factor
#4 Risk Factor
```

Risk priority styles include:

```text
Priority 1 -> Critical Risk
Priority 2 -> High Risk
Priority 3 -> Moderate Risk
Priority 4 -> Standard Risk
```

This ensures the highest clinical risk is always displayed first.

---

# Reusable Response Visualization Engine

The `ResponseView` component provides a generic JSON visualization engine.

File:

```text
src/components/common/ResponseView.tsx
```

The component analyzes the API response type and automatically determines the appropriate visualization.

---

## Primitive Values

Primitive values are displayed as metric cards.

Supported values:

```text
string
number
boolean
null
```

---

## JSON Objects

JSON objects are analyzed based on their keys.

Example:

```json
{
  "total_patients": 1000,
  "high_risk_patients": 250
}
```

Displayed as:

```text
Total Patients
1,000

High Risk Patients
250
```

---

## Arrays of Objects

Arrays containing JSON objects are displayed using responsive tables.

Example:

```json
[
  {
    "feature": "age",
    "importance": 0.82
  },
  {
    "feature": "cholesterol",
    "importance": 0.67
  }
]
```

Displayed as:

```text
Feature        Importance
Age            0.82
Cholesterol    0.67
```

---

## Arrays of Text

Text arrays are displayed as numbered analytical insights.

Example:

```json
[
  "Monitor cholesterol levels",
  "Evaluate blood pressure",
  "Perform cardiovascular screening"
]
```

Displayed as:

```text
1  Monitor cholesterol levels

2  Evaluate blood pressure

3  Perform cardiovascular screening
```

---

## Nested JSON Objects

Nested API responses are recursively rendered.

Example:

```json
{
  "clinical_analysis": {
    "risk_factors": {
      "cholesterol": 82,
      "blood_pressure": 75
    }
  }
}
```

The visualization engine automatically generates nested analytics sections.

---

# Technology Stack

## Frontend

* React.js
* TypeScript
* Vite
* React Router
* Axios
* Recharts
* CSS Grid
* Responsive CSS

## Backend Integration

* FastAPI
* REST API
* OpenAPI
* JSON Schema

## Data Visualization

* Recharts
* ResponsiveContainer
* BarChart
* PieChart
* Tooltip
* Legend
* LabelList

---

# Project Structure

```text
src/
│
├── api/
│   ├── heartApi.ts
│   └── http.ts
│
├── components/
│   │
│   ├── common/
│   │   └── ResponseView.tsx
│   │
│   └── layout/
│       └── Sidebar.tsx
│
├── hooks/
│   └── useApi.ts
│
├── pages/
│   ├── AnalysisPage.tsx
│   ├── DashboardPage.tsx
│   └── PredictionPage.tsx
│
├── styles/
│   └── global.css
│
├── types/
│   └── heart.ts
│
├── App.tsx
└── main.tsx
```

---

# Architecture

```text
                       React Application
                              |
                              v
                        React Router
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
    Dashboard Page      Analysis Page       Prediction Page
          |                   |                   |
          +-------------------+-------------------+
                              |
                              v
                         API Layer
                              |
                    +---------+---------+
                    |                   |
                    v                   v
               heartApi.ts          http.ts
                    |                   |
                    +---------+---------+
                              |
                              v
                         Axios Client
                              |
                              v
                         FastAPI API
                              |
               +--------------+--------------+
               |                             |
               v                             v
       Analytics Endpoints             Prediction API
               |                             |
               v                             v
        JSON API Response               ML Prediction
               |
               v
          ResponseView
               |
     +---------+----------+----------+
     |                    |          |
     v                    v          v
 KPI Cards             Charts      Tables
     |                    |
     v                    v
Progress Bars        Risk Visuals
```

---

# API Configuration

The Axios client is configured in:

```text
src/api/http.ts
```

Default API URL:

```text
http://127.0.0.1:8000
```

The application supports environment-based configuration using:

```text
VITE_API_BASE_URL
```

Create a `.env` file in the React project root.

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

For production:

```env
VITE_API_BASE_URL=https://api.example.com
```

---

# Supported API Endpoints

| Module                | Method | Endpoint                       |
| --------------------- | ------ | ------------------------------ |
| Dashboard             | GET    | `/heart/dashboard`             |
| EDA Summary           | GET    | `/heart/eda-summary`           |
| Descriptive Analysis  | GET    | `/heart/descriptive-analysis`  |
| Diagnostic Analysis   | GET    | `/heart/diagnostic-analysis`   |
| Predictive Analysis   | GET    | `/heart/predictive-analysis`   |
| Prescriptive Analysis | GET    | `/heart/prescriptive-analysis` |
| Risk Analysis         | GET    | `/heart/risk-analysis`         |
| KPIs                  | GET    | `/heart/kpis`                  |
| Feature Importance    | GET    | `/heart/feature-importance`    |
| Patient Segments      | GET    | `/heart/patient-segments`      |
| Recommendations       | GET    | `/heart/recommendations`       |
| Executive Summary     | GET    | `/heart/executive-summary`     |
| Prediction            | POST   | `/heart/predict`               |
| Batch Prediction      | POST   | `/heart/batch-predict`         |
| OpenAPI Schema        | GET    | `/openapi.json`                |

---

# API Layer

The centralized Heart API client is implemented in:

```text
src/api/heartApi.ts
```

Example:

```typescript
const get = (path: string) =>
  http.get(`/heart/${path}`)
    .then(response => response.data);
```

The API service exposes reusable functions.

```typescript
heartApi.dashboard()

heartApi.edaSummary()

heartApi.descriptiveAnalysis()

heartApi.diagnosticAnalysis()

heartApi.predictiveAnalysis()

heartApi.prescriptiveAnalysis()

heartApi.riskAnalysis()

heartApi.kpis()

heartApi.featureImportance()

heartApi.patientSegments()

heartApi.recommendations()

heartApi.executiveSummary()

heartApi.predict(payload)

heartApi.batchPredict(payload)
```

---

# Routing

React Router is configured in:

```text
src/App.tsx
```

Application routes:

```text
/
    |
    v
/dashboard
```

Available routes:

```text
/dashboard

/analysis/eda-summary

/analysis/descriptive-analysis

/analysis/diagnostic-analysis

/analysis/predictive-analysis

/analysis/prescriptive-analysis

/analysis/risk-analysis

/analysis/kpis

/analysis/feature-importance

/analysis/patient-segments

/analysis/recommendations

/analysis/executive-summary

/predict
```

Dynamic analysis routing is implemented using:

```typescript
<Route
  path="/analysis/:endpoint"
  element={<AnalysisPage />}
/>
```

This prevents creating a separate React page for every analytical endpoint.

---

# Sidebar Navigation

The sidebar provides access to all analytical modules.

Navigation options include:

```text
Dashboard
EDA Summary
Descriptive
Diagnostic
Predictive
Prescriptive
Risk Analysis
KPIs
Feature Importance
Patient Segments
Recommendations
Executive Summary
Predict
```

Active routes are automatically highlighted using `NavLink`.

---

# Custom API Hook

The application provides a reusable API loading hook.

File:

```text
src/hooks/useApi.ts
```

The hook manages:

* API response data
* Loading state
* Error state

Example:

```typescript
const {
  data,
  loading,
  error
} = useApi(heartApi.dashboard);
```

Returned state:

```typescript
{
  data,
  loading,
  error
}
```

---

# TypeScript Types

Heart disease prediction types are defined in:

```text
src/types/heart.ts
```

The `HeartPredictionRequest` interface includes commonly used heart disease model attributes.

```typescript
interface HeartPredictionRequest {
  age: number;
  sex: number;
  cp: number;
  trestbps: number;
  chol: number;
  fbs: number;
  restecg: number;
  thalach: number;
  exang: number;
  oldpeak: number;
  slope: number;
  ca: number;
  thal: number;
}
```

The prediction page additionally uses the FastAPI OpenAPI schema to dynamically generate the actual request form.

---

# Installation

## Prerequisites

Install the following software:

```text
Node.js >= 18
npm >= 9
```

The FastAPI backend should also be running.

Default backend URL:

```text
http://127.0.0.1:8000
```

---

## Install Dependencies

Navigate to the React project directory.

```bash
cd heart-disease-dashboard
```

Install dependencies.

```bash
npm install
```

Required major packages include:

```bash
npm install react react-dom
npm install react-router-dom
npm install axios
npm install recharts
```

Development dependencies:

```bash
npm install -D typescript
npm install -D vite
npm install -D @types/react
npm install -D @types/react-dom
```

---

# Run the Application

Start the Vite development server.

```bash
npm run dev
```

The application is typically available at:

```text
http://localhost:5173
```

Open the application in a browser.

---

# Backend Requirements

The FastAPI backend must expose the heart disease router.

Example API prefix:

```text
/heart
```

FastAPI should expose the OpenAPI specification.

```text
/openapi.json
```

Verify the OpenAPI schema using the browser.

```text
http://127.0.0.1:8000/openapi.json
```

Verify the FastAPI Swagger documentation.

```text
http://127.0.0.1:8000/docs
```

---

# CORS Configuration

The FastAPI backend must allow the React frontend origin.

Example FastAPI configuration:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

# Build for Production

Create an optimized production build.

```bash
npm run build
```

The production output is generated in:

```text
dist/
```

Preview the production build.

```bash
npm run preview
```

---

# Responsive Design

The application supports:

* Desktop displays
* Laptop displays
* Tablet displays
* Mobile displays

Responsive layouts are implemented using:

```text
CSS Grid
auto-fit
minmax
Media Queries
ResponsiveContainer
```

The sidebar and dashboard layout automatically adjust for smaller screens.

---

# Error Handling

The application supports:

* Axios request errors
* FastAPI validation errors
* Prediction errors
* OpenAPI schema loading errors
* API connection failures

Example error message:

```text
Prediction Request Error

age: Field required
```

If the OpenAPI schema cannot be loaded:

```text
Unable to load prediction schema from FastAPI OpenAPI.
```

---

# Design Principles

The frontend follows several architectural principles.

## Separation of Concerns

```text
API Communication    -> api/
Reusable UI          -> components/
API State Logic      -> hooks/
Application Pages    -> pages/
Type Definitions     -> types/
Application Styling  -> styles/
```

## Reusable Visualization

`ResponseView` is responsible for automatically converting JSON responses into visual components.

## Dynamic Backend Integration

Prediction fields are generated from the FastAPI OpenAPI request schema.

## Responsive Healthcare UI

The dashboard uses responsive cards, grids, charts, and tables.

## API-Centric Architecture

React pages remain lightweight while API communication is centralized.

---

# Recommended Future Enhancements

Potential future improvements include:

* React Query or TanStack Query integration
* Zustand or Redux Toolkit state management
* Authentication and authorization
* Role-based access control
* Clinical user roles
* Patient drill-down pages
* Patient-level risk profiles
* SHAP feature explanations
* Model confidence visualization
* Prediction history
* Batch prediction interface
* CSV upload
* PDF clinical reports
* Export to Excel
* Dark mode
* Theme management
* Toast notifications
* Skeleton loaders
* Error boundaries
* Unit testing
* Component testing
* End-to-end testing
* Docker deployment
* Kubernetes deployment
* Azure deployment
* CI/CD pipeline

---

# Recommended Enterprise Architecture

For a production healthcare AI platform, the frontend can evolve into:

```text
src/
│
├── api/
│   ├── clients/
│   ├── endpoints/
│   └── interceptors/
│
├── assets/
│
├── components/
│   ├── charts/
│   ├── common/
│   ├── forms/
│   ├── kpi/
│   └── layout/
│
├── config/
│
├── features/
│   ├── analytics/
│   ├── dashboard/
│   ├── prediction/
│   ├── risk/
│   └── patients/
│
├── hooks/
│
├── pages/
│
├── routes/
│
├── services/
│
├── store/
│
├── styles/
│
├── types/
│
├── utils/
│
├── App.tsx
└── main.tsx
```

This feature-oriented architecture is recommended as the application grows into a larger clinical analytics platform.

---

# Healthcare Disclaimer

This application is intended for:

* Healthcare analytics
* Clinical data exploration
* AI/ML demonstration
* Research
* Educational purposes
* Decision-support prototyping

AI-generated predictions should **not be used as a substitute for professional medical diagnosis or clinical judgment**.

Clinical decisions should always be reviewed by qualified healthcare professionals.

---

# Summary

The **Heart Disease Clinical Analytics & AI Prediction Dashboard** provides a reusable React and TypeScript architecture for healthcare analytics and machine learning applications.

The key architectural capabilities are:

* React.js with TypeScript
* FastAPI REST API integration
* Dynamic FastAPI OpenAPI schema discovery
* AI heart disease risk prediction
* Reusable JSON visualization engine
* Recharts-based healthcare visualizations
* Risk-priority ranking
* KPI performance visualization
* Dynamic analytical routing
* Responsive healthcare dashboard design
* Structured FastAPI validation error handling

The application demonstrates how a modern React frontend can integrate with a FastAPI machine learning backend to build an interactive **Healthcare AI Clinical Analytics and Risk Prediction Platform**.
