"""A module provides API to work with services."""
from abc import ABC, abstractmethod
from typing import Sequence
from lib.applications import pyjokes_app
from lib.setup import ServerConfig


class Service(ABC):
    """The class represents abstract interface for some service."""

    @abstractmethod
    def start(self) -> None:
        """Starts abstract service."""
        pass


class PyJoker(Service):
    """The class represents `py-joker` service."""

    __slots__: Sequence[str] = ("_server_config",)

    def __init__(self, server_config: ServerConfig) -> None:
        self._server_config: ServerConfig = server_config

    def start(self) -> None:
        """Starts py-joker service."""
        pyjokes_app.run(
            host=self._server_config.host, port=self._server_config.port, debug=self._server_config.allow_debug
        )
