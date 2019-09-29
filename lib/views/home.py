import pyjokes
from flask import render_template
from lib.applications import pyjokes_app
from lib.setup import Language


@pyjokes_app.route("/", methods=["GET"])
def index() -> None:
    return render_template(
        "index.html",
        spanish=pyjokes.get_joke(language=Language.SPANISH.code()),
        deutsch=pyjokes.get_joke(language=Language.DEUTSCH.code()),
        english=pyjokes.get_joke(language=Language.ENGLISH.code()),
    )
