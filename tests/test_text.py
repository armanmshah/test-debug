from shopkit.text import slugify


def test_simple_words():
    assert slugify("Blue Mug") == "blue-mug"


def test_already_a_slug():
    assert slugify("kettle") == "kettle"
