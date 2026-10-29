import pytest

from shopkit.cart import Cart


@pytest.mark.parametrize("quantity", [None, 2])
def test_remove_preserves_remaining_units(quantity):
    cart = Cart()
    cart.add("MUG-BLU", 3)

    if quantity is None:
        cart.remove("MUG-BLU")
        expected = 2
    else:
        cart.remove("MUG-BLU", quantity=quantity)
        expected = 3 - quantity

    assert cart.items == {"MUG-BLU": expected}
