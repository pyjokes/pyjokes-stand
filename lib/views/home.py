"""Sets API for home page routes."""
from enum import Enum
import pyjokes
from flask import render_template
from lib.applications import pyjokes_app
from lib.requests import Request
from lib.routes import Route
from lib.setup import Language


class Template(Enum):
    """Class represents template entity."""

    INDEX: str = "index.html"


@pyjokes_app.route(Route.ROOT.value, methods=(Request.GET.value,))
def index() -> str:
    """Sets route for index page."""
    return render_template(
        Template.INDEX.value,
        spanish=pyjokes.get_joke(language=Language.SPANISH.code()),
        deutsch=pyjokes.get_joke(language=Language.DEUTSCH.code()),
        english=pyjokes.get_joke(language=Language.ENGLISH.code()),
    )
