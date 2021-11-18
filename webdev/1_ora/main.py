import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/oldal")
def get_oldal():
    return "Megtaláltad a titkos oldalt"

@app.route("/matek")
def osszeadas():
    return f"5*4={5*4}"


if __name__ == '__main__':
    app.run(use_reloader=True, port=5001)
