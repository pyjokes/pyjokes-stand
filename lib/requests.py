"""Sets API for home page requests."""

from enum import Enum


class Request(Enum):
    """Class represents web request."""

    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    DELETE: str = "DELETE"
