from flask import Flask, render_template, request, redirect, abort
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('base.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run()