from flask import Flask, render_template
import pyjokes

jokes_app: Flask = Flask(__name__)


@jokes_app.route("/", methods=["GET"])
def index() -> None:
    return render_template(
        "index.html",
        basque=pyjokes.get_joke(language="eu"),
        spanish=pyjokes.get_joke(language="es"),
        deutsch=pyjokes.get_joke(language="de"),
        english=pyjokes.get_joke(language="en"),
    )


if __name__ == "__main__":
    jokes_app.run(host="0.0.0.0", port=8080)
