"""A module provides API to work with applications."""
from abc import ABC, abstractmethod
from typing import Any
from flask import Flask
from lib.setup import ServerConfig


class Application(ABC):
    """The class represents an abstract application."""

    @abstractmethod
    def run(self, host: str, port: int, debug: bool, **options: Any) -> None:
        """Runs an application."""
        pass

    @abstractmethod
    def route(self, rule: str, **option: Any) -> None:
        """Sets route for given rule."""
        pass

    @abstractmethod
    def __call__(self, *args: Any, **kwargs) -> Flask:
        """Calls an application."""
        pass


class WebApplication(Application):
    """The class represents web application."""

    def __init__(self, module: str, static_dir: str, template_dir: str) -> None:
        self._engine: Flask = Flask(import_name=module, static_folder=static_dir, template_folder=template_dir)

    def run(self, host: str, port: int, debug: bool, **options: Any) -> None:
        """Runs web application."""
        return self._engine.run(host, port, debug, **options)

    def route(self, rule: str, **option: Any) -> None:
        """Sets route for given web application rule."""
        self._engine.route(rule, **option)

    def __call__(self, *args: Any, **kwargs: Any) -> Flask:
        """Calls web application."""
        return self._engine


class PyJokerApplication(Application):
    """The class represents `py-joker` application."""

    def __init__(self, config: ServerConfig) -> None:
        self._application: Application = WebApplication(config.name, config.folder.static, config.folder.templates)

    def run(self, host: str, port: int, debug: bool, **options: Any) -> None:
        """Runs `py-joker` application."""
        self._application.run(host, port, debug, **options)

    def route(self, rule: str, **option: Any) -> None:
        """Sets route for given `py-joker` rule."""
        self._application.route(rule, **option)

    def __call__(self, *args: Any, **kwargs) -> Flask:
        """Calls `py-joker` application."""
        return self._application(*args, **kwargs)


def _engine_of(*, application: Application) -> Flask:
    """Returns engine of given application."""
    return application()


pyjokes_app: Flask = _engine_of(application=PyJokerApplication(ServerConfig()))
