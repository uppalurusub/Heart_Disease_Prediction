from api.heart_api import get_data
from components.response_view import render_descriptive, render_diagnostic, render_predictive


def render() -> None:
    render_descriptive(get_data("descriptive-analysis"))
    render_diagnostic(get_data("diagnostic-analysis"))
    render_predictive(get_data("predictive-analysis"))
