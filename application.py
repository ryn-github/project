from flask import Flask, render_template

template_dir = "/home/r/project"

app = Flask(__name__, template_folder=template_dir)

lsit = ["uno","dos","tres","quadro"]

@app.route("/")
def index():
    return render_template("primary.html")

@app.route("/speedwagon")
def speedwagon():
    return render_template("speedwagon.html")
