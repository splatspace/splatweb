from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
