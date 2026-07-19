from api.heart_api import get_data
from components.response_view import render_risk_segmentation


def render() -> None:
    render_risk_segmentation(get_data("patient-segments"))
