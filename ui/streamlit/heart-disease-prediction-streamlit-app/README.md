# Heart Disease Risk Prediction Dashboard

Modular Streamlit frontend for the Heart Disease FastAPI service.

## Structure

- `api/` - API client functions
- `components/` - reusable forms, response views, and sidebar
- `utils/` - formatting helpers
- `pages/` - dashboard feature modules
- `.streamlit/` - Streamlit configuration
- `dashboard.py` - application entry point

## Run

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

The API is expected at `http://localhost:8000/heart`.
