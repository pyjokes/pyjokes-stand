import pytest
from lib.requests import Request


@pytest.mark.parametrize("init_request", [Request.GET, Request.POST, Request.PUT, Request.DELETE])
def test_requests(init_request: Request) -> None:
    assert isinstance(init_request, Request)


@pytest.mark.parametrize(
    "init_request, result",
    [(Request.GET, "GET"), (Request.POST, "POST"), (Request.PUT, "PUT"), (Request.DELETE, "DELETE")],
)
def test_requests_value(init_request: Request, result: str) -> None:
    assert init_request.value == result
