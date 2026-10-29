from decimal import Decimal

from shopkit.pricing import quote


def test_lowercase_save10_matches_uppercase_coupon():
    uppercase = quote(Decimal("100.00"), item_count=1, coupon="SAVE10")
    lowercase = quote(Decimal("100.00"), item_count=1, coupon="save10")

    assert lowercase == uppercase
    assert lowercase.discount == Decimal("10.00")
