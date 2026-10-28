import pytest

from shopkit.catalog import get_product, list_products, search_products


def test_get_product():
    assert get_product("KETTLE").name == "Stovetop Kettle"


def test_unknown_product():
    with pytest.raises(KeyError):
        get_product("NOPE")


def test_list_by_category():
    assert {p.sku for p in list_products("apparel")} == {"APRON"}


def test_search_ignores_case():
    assert [p.sku for p in search_products("KETTLE")] == ["KETTLE"]
