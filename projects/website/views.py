from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@views.route("/generic.html", methods=["GET"])
def generic():
    return render_template("generic.html")

@views.route("/elements.html", methods=["GET"])
def elements():
    return render_template("elements.html")