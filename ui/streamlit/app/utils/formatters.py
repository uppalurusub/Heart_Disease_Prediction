from typing import Any


def format_percent(value: Any, decimals: int = 1) -> str:
    try:
        return f"{float(value):.{decimals}f}%"
    except (TypeError, ValueError):
        return "0.0%"


def format_number(value: Any) -> str:
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return "0"
