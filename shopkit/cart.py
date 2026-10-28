"""Shopping carts."""

from __future__ import annotations

from decimal import Decimal

from shopkit import pricing
from shopkit.catalog import get_product


class Cart:
    def __init__(self) -> None:
        self.items: dict[str, int] = {}

    def add(self, sku: str, quantity: int = 1) -> None:
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        get_product(sku)  # raises KeyError for unknown SKUs
        self.items[sku] = self.items.get(sku, 0) + quantity

    def remove(self, sku: str, quantity: int = 1) -> None:
        """Remove `quantity` units of a product; the line goes away when none are left."""
        if sku not in self.items:
            raise KeyError(f"{sku} is not in the cart")
        del self.items[sku]

    def item_count(self) -> int:
        return sum(self.items.values())

    def subtotal(self) -> Decimal:
        return sum((get_product(sku).price * qty for sku, qty in self.items.items()),
                   Decimal(0))

    def quote(self, coupon: str | None = None) -> pricing.Quote:
        return pricing.quote(self.subtotal(), self.item_count(), coupon)
