from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "This is a simple server test\n"


@app.route("/version")
def version():
    return "Version 1.0\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9898)
