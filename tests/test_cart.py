from decimal import Decimal

import pytest

from shopkit.cart import Cart


def test_add_accumulates():
    cart = Cart()
    cart.add("MUG-BLU")
    cart.add("MUG-BLU", 2)
    assert cart.items == {"MUG-BLU": 3}
    assert cart.item_count() == 3


def test_add_unknown_sku():
    with pytest.raises(KeyError):
        Cart().add("NOPE")


def test_remove_last_unit():
    cart = Cart()
    cart.add("HONEY")
    cart.remove("HONEY")
    assert cart.items == {}


def test_subtotal():
    cart = Cart()
    cart.add("MUG-BLU", 2)
    cart.add("TEA-GRN")
    assert cart.subtotal() == Decimal("31.75")
