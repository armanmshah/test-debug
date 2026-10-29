"""Discounts, coupons and tax."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

TAX_RATE = Decimal("0.08")
BULK_THRESHOLD = 10        # orders of this many items or more get the bulk discount
BULK_PERCENT = 5
COUPONS = {"SAVE10": 10, "WELCOME5": 5}
CENT = Decimal("0.01")


class InvalidCouponError(ValueError):
    pass


@dataclass(frozen=True)
class Quote:
    subtotal: Decimal
    discount: Decimal
    tax: Decimal
    total: Decimal


def coupon_percent(code: str) -> int:
    """The discount for a coupon code. Codes are not case-sensitive."""
    percent = COUPONS.get(code.strip().upper())
    if percent is None:
        raise InvalidCouponError(f"unknown coupon: {code}")
    return percent


def discount_percent(item_count: int, coupon: str | None = None) -> int:
    """Total discount: 5% for orders of 10 or more items, plus any coupon."""
    percent = 0
    if item_count > BULK_THRESHOLD:
        percent += BULK_PERCENT
    if coupon:
        percent += coupon_percent(coupon)
    return percent


def quote(subtotal: Decimal, item_count: int, coupon: str | None = None) -> Quote:
    """Price an order. Tax is applied after discounts."""
    percent = discount_percent(item_count, coupon)
    discount = (subtotal * percent / 100).quantize(CENT, ROUND_HALF_UP)
    taxable = subtotal - discount
    tax = (taxable * TAX_RATE).quantize(CENT, ROUND_HALF_UP)
    return Quote(subtotal=subtotal, discount=discount, tax=tax, total=taxable + tax)
