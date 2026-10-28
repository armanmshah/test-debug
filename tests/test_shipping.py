from datetime import date

import pytest

from shopkit.shipping import estimate_delivery

MONDAY = date(2026, 3, 2)


def test_express_midweek():
    assert estimate_delivery(MONDAY, "express") == date(2026, 3, 4)


def test_unknown_method():
    with pytest.raises(ValueError):
        estimate_delivery(MONDAY, "teleport")
