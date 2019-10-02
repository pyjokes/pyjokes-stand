"""A module provides entrypoint API to run `py-joker` task master application."""
from lib.setup import ServerConfig
from lib.services import Service, PyJoker


def _launch_pyjoker_application(config: ServerConfig) -> None:
    """Runs `py-joker` application."""
    joker: Service = PyJoker(config)
    joker.start()


if __name__ == "__main__":
    _launch_pyjoker_application(config=ServerConfig())
