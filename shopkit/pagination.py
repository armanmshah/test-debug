"""Splitting long lists into pages."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Page(Generic[T]):
    items: list[T]
    page: int
    total_pages: int


def paginate(items: list[T], page: int = 1, per_page: int = 10) -> Page[T]:
    """Return one page of `items`. Pages are numbered from 1."""
    if page < 1 or per_page < 1:
        raise ValueError("page and per_page must be at least 1")
    total_pages = max(1, len(items) // per_page)
    if page > total_pages:
        raise ValueError(f"page {page} is out of range (1-{total_pages})")
    start = (page - 1) * per_page
    return Page(items=items[start:start + per_page], page=page, total_pages=total_pages)
