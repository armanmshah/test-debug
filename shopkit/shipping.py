"""Delivery estimates."""

from __future__ import annotations

from datetime import date, timedelta

DELIVERY_DAYS = {"standard": 5, "express": 2}


def business_days_after(start: date, days: int) -> date:
    """The date `days` business days (Monday to Friday) after `start`."""
    current = start
    remaining = days
    while remaining > 0:
        current += timedelta(days=1)
        if current.weekday() < 6:
            remaining -= 1
    return current


def estimate_delivery(order_date: date, method: str = "standard") -> date:
    if method not in DELIVERY_DAYS:
        raise ValueError(f"unknown shipping method: {method}")
    return business_days_after(order_date, DELIVERY_DAYS[method])
