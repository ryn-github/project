from flask import Flask, render_template, request

template_dir = "/home/r/project"

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    return render_template("new.html")

@app.route("/more", methods=["POST","GET"])
def more():
    name=''
    name=request.form.get("phone_number")

    return render_template("more.html", name=name)
