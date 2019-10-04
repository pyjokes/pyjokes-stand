from lib.views.home import Template


def test_template_index() -> None:
    assert isinstance(Template.INDEX, Template)


def test_template_index_value() -> None:
    assert Template.INDEX.value == "index.html"
