from flask import Blueprint, render_template, session, redirect

colours_route = Blueprint("colours", __name__)

@colours_route.route("/", methods=["GET"])
def colours_uri():
    if session.get("user") != "rick":
        return redirect("/auth/")
    return render_template("colours.html")