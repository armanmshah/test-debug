"""Stock levels."""

from __future__ import annotations


class OutOfStockError(Exception):
    pass


class Inventory:
    def __init__(self, stock: dict[str, int] | None = None) -> None:
        self._stock = dict(stock or {})

    def available(self, sku: str) -> int:
        return self._stock.get(sku, 0)

    def add_stock(self, sku: str, quantity: int) -> None:
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        self._stock[sku] = self.available(sku) + quantity

    def remove_stock(self, sku: str, quantity: int) -> None:
        """Take units out of stock. Raises OutOfStockError if not enough are available."""
        if quantity < 1:
            raise ValueError("quantity must be at least 1")
        self._stock[sku] = self.available(sku) - quantity
