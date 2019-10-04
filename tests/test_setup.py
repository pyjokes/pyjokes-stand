import pytest
from lib.setup import _Folder, ServerConfig, Language, LanguageCodeError


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


@pytest.mark.parametrize(
    "language, result", [(Language.ENGLISH, "en"), (Language.DEUTSCH, "de"), (Language.SPANISH, "es")]
)
def test_language_code(language: Language, result: str) -> None:
    assert language.code() == result


def test_count_languages() -> None:
    assert len(Language) == 3


def test_language_error() -> None:
    with pytest.raises(LanguageCodeError):
        Language.from_str("eu")
