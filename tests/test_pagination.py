import pytest

from shopkit.pagination import paginate


def test_even_split():
    items = list(range(20))
    page = paginate(items, page=2, per_page=10)
    assert page.items == list(range(10, 20))
    assert page.total_pages == 2


def test_empty_list_has_one_page():
    page = paginate([], page=1)
    assert page.items == [] and page.total_pages == 1


def test_page_out_of_range():
    with pytest.raises(ValueError):
        paginate(list(range(20)), page=3, per_page=10)
