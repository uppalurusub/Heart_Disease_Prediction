from typing import Any
import requests

API_BASE_URL = "http://localhost:8000/heart"
TIMEOUT = 30


def get_data(endpoint: str) -> dict[str, Any]:
    response = requests.get(f"{API_BASE_URL}/{endpoint}", timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


def predict_patient(payload: dict[str, Any]) -> dict[str, Any]:
    response = requests.post(
        f"{API_BASE_URL}/predict",
        json=payload,
        timeout=TIMEOUT,
    )
    response.raise_for_status()
    return response.json()
