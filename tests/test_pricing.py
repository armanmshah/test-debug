from decimal import Decimal

import pytest

from shopkit.pricing import InvalidCouponError, quote


def test_no_discount():
    q = quote(Decimal("50.00"), item_count=2)
    assert q.discount == Decimal("0.00")
    assert q.tax == Decimal("4.00")
    assert q.total == Decimal("54.00")


def test_coupon_applied_before_tax():
    q = quote(Decimal("100.00"), item_count=1, coupon="SAVE10")
    assert q.discount == Decimal("10.00")
    assert q.tax == Decimal("7.20")
    assert q.total == Decimal("97.20")


def test_bulk_discount_for_large_orders():
    q = quote(Decimal("200.00"), item_count=12)
    assert q.discount == Decimal("10.00")


def test_unknown_coupon():
    with pytest.raises(InvalidCouponError):
        quote(Decimal("10.00"), item_count=1, coupon="FREESTUFF")
