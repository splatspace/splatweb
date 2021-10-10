from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/membership")
def membership():
    return render_template("membership.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/contributors")
def contributors():
    return render_template("contributors.html")

@app.route("/currentmembers")
def currentmembers():
    return render_template("currentmembers.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/equipment")
def equipment():
    return render_template("equipment.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
