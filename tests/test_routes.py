from lib.routes import Route


def test_route_root() -> None:
    assert isinstance(Route.ROOT, Route)


def test_template_index_value() -> None:
    assert Route.ROOT.value == "/"
