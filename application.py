from flask import Flask, render

app = Flask(__name__,template_folder=)

@app.route("/")
def index():
    return "Hjello"
