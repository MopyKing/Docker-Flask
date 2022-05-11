from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/ping')
def pong():
    return "<h1>PONG<h1>"


@app.route("/")
def home():
    return "<h1>HELLO ! THIS IS THE HOME PAGE<h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

