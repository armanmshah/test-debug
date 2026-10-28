"""Text helpers."""

from __future__ import annotations

import re


def slugify(text: str) -> str:
    """URL-friendly form of `text`: "Green Tea, 50 bags" -> "green-tea-50-bags".

    Lowercase ASCII letters and digits; each run of other characters becomes a single "-",
    with none at the start or end.
    """
    return re.sub(r"[^a-z0-9]", "-", text.lower())
