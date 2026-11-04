from api.heart_api import get_data
from components.response_view import render_feature_importance


def render() -> None:
    render_feature_importance(get_data("feature-importance"))
