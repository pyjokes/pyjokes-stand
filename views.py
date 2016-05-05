from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import pyjokes

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def index():
    return render_template('index.html',
                           basque   =   pyjokes.get_joke(language="en"),
                           spanish  =   pyjokes.get_joke(language="es"))


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8080"),
        debug=True
    )