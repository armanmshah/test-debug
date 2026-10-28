"""The product catalog."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: Decimal
    category: str


CATALOG: list[Product] = [
    Product("MUG-BLU", "Blue Mug", Decimal("12.50"), "kitchen"),
    Product("MUG-RED", "Red Mug", Decimal("12.50"), "kitchen"),
    Product("KETTLE", "Stovetop Kettle", Decimal("39.00"), "kitchen"),
    Product("TEA-GRN", "Green Tea, 50 bags", Decimal("6.75"), "pantry"),
    Product("TEA-BLK", "Black Tea, 50 bags", Decimal("6.25"), "pantry"),
    Product("HONEY", "Wildflower Honey", Decimal("9.99"), "pantry"),
    Product("APRON", "Canvas Apron", Decimal("24.00"), "apparel"),
    Product("ESPRESSO", "Espresso Machine", Decimal("1299.00"), "kitchen"),
]


def get_product(sku: str) -> Product:
    for product in CATALOG:
        if product.sku == sku:
            return product
    raise KeyError(f"unknown SKU: {sku}")


def list_products(category: str | None = None) -> list[Product]:
    if category is None:
        return list(CATALOG)
    return [p for p in CATALOG if p.category == category]


def search_products(query: str) -> list[Product]:
    """Products whose name contains `query`, ignoring case."""
    q = query.strip().lower()
    return [p for p in CATALOG if q in p.name.lower()]
