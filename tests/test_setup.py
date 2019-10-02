import pytest
from lib.setup import _Folder, ServerConfig, Language


@pytest.fixture(scope="module")
def folder() -> _Folder:
    return _Folder(static="static", templates="templates")


@pytest.fixture(scope="module")
def config() -> ServerConfig:
    return ServerConfig()


def test_folder_static(folder: _Folder) -> None:
    assert folder.static == "static"


def test_folder_templates(folder: _Folder) -> None:
    assert folder.templates == "templates"


def test_config_name(config: ServerConfig) -> None:
    assert config.name == "lib.setup"


def test_config_host(config: ServerConfig) -> None:
    assert config.host == "0.0.0.0"


def test_config_port(config: ServerConfig) -> None:
    assert config.port == 4444


def test_config_allow_debug(config: ServerConfig) -> None:
    assert not config.allow_debug


def test_config_folder(config: ServerConfig) -> None:
    assert isinstance(config.folder, _Folder)


def test_language_from_str() -> None:
    assert Language.from_str("de") is Language.DEUTSCH


def test_language_code() -> None:
    assert Language.ENGLISH.code() == "en"
