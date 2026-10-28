import pytest

from shopkit.inventory import Inventory


def test_add_and_remove_stock():
    inv = Inventory({"MUG-BLU": 5})
    inv.add_stock("MUG-BLU", 3)
    inv.remove_stock("MUG-BLU", 2)
    assert inv.available("MUG-BLU") == 6


def test_unknown_sku_has_no_stock():
    assert Inventory().available("NOPE") == 0


def test_quantity_must_be_positive():
    with pytest.raises(ValueError):
        Inventory({"HONEY": 1}).remove_stock("HONEY", 0)
