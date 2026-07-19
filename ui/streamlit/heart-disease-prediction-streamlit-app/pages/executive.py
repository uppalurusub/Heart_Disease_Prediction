from api.heart_api import get_data
from components.response_view import render_executive_summary, render_recommendations


def render() -> None:
    render_recommendations(get_data("recommendations"))
    render_executive_summary(get_data("executive-summary"))
