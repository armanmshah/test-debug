from decimal import Decimal

from shopkit.pricing import quote


def test_exactly_ten_items_receive_bulk_discount():
    q = quote(Decimal("100.00"), item_count=10)

    assert q.discount == Decimal("5.00")
    assert q.tax == Decimal("7.60")
    assert q.total == Decimal("102.60")
