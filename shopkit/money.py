"""Formatting money."""

from __future__ import annotations

from decimal import Decimal


def format_price(amount: Decimal) -> str:
    """US dollars with cents and thousands separators: Decimal("1299") -> "$1,299.00"."""
    return f"${amount:.2f}"
