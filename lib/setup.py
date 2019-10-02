"""A module provides API to work with configuration setup."""
import os
from dataclasses import dataclass
from enum import Enum

_SOURCE_DIR: str = os.path.abspath(os.path.dirname(__name__))


class LanguageCodeError(Exception):
    """Custom exception for language code."""

    pass


@dataclass(frozen=True)
class _Folder:
    """Represents setup folder."""

    static: str = f"{_SOURCE_DIR}/static/"
    templates: str = f"{_SOURCE_DIR}/templates/"


@dataclass(frozen=True)
class ServerConfig:
    """Represents setup configuration."""

    name: str = __name__
    host: str = "0.0.0.0"
    port: int = 4444
    allow_debug: bool = False
    folder: _Folder = _Folder()


class Language(Enum):
    """Represents language enumeration."""

    SPANISH: str = "es"
    DEUTSCH: str = "de"
    ENGLISH: str = "en"

    @classmethod
    def from_str(cls, language: str) -> "Language":
        """Returns language from string type."""
        for next_language in cls:  # type: Language
            if next_language.code() == language:
                return next_language
        raise LanguageCodeError(f'No language code was found for given "{language}"!')

    def code(self) -> str:
        """Returns language code."""
        return self.value
