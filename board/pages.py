from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    return render_template("pages/home.html")


@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/just")
def just():
    return render_template("pages/just.html")

@bp.route("/garden")
def garden():
    return render_template("pages/garden.html")

@bp.route("/Pruning")
def pruning():
    return render_template("pages/pruning.html")

@bp.route("/triclimbing")
def triclimbing():
    return render_template("pages/triclimbing.html")

@bp.route("/contacts us")
def contacts_us():
    return render_template("pages/contacts us.html")

#python -m flask --app board run --debug 