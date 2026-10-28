from decimal import Decimal

from shopkit.money import format_price


def test_cents_are_padded():
    assert format_price(Decimal("9.5")) == "$9.50"
