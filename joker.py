from lib.setup import ServerConfig
from lib.services import Service, PyJoker


def _launch_pyjoker() -> None:
    joker: Service = PyJoker(ServerConfig())
    joker.start()


if __name__ == "__main__":
    _launch_pyjoker()
