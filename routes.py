from app import app
from flask import render_template, request, redirect
from sqlalchemy.sql import text
import messages, users
topics = ["musiikki", "ruoka", "yliopisto"]

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        tunnus = request.form["tunnus"]
        salasana = request.form["salasana"]
        if users.login(tunnus, salasana):
            return redirect("/")
        else:
            return render_template("error.html", message="Jokin meni pieleen")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        tunnus = request.form["tunnus"]
        salasana1 = request.form["salasana1"]
        salasana2 = request.form["salasana2"]
        if salasana1 != salasana2:
            return render_template("error.html", message="Jokin meni pieleen")
        if users.register(tunnus, salasana1):
            return redirect("/")
        else:
            return render_template("error.html", message="Jokin meni pieleen")
    
@app.route("/musiikki")
def musiikki():
    list = messages.get_music_list()
    return render_template("musiikki.html", count=len(list), messages=list)

@app.route("/ruoka")
def ruoka():
    list = messages.get_food_list()
    return render_template("ruoka.html", count=len(list), messages=list)

@app.route("/yliopisto")
def yliopisto():
    list = messages.get_uni_list()
    return render_template("yliopisto.html", count=len(list), messages=list)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    topic = topics[int(request.form["topic"]) - 1]
    if messages.send(content, topic):
        return redirect(f"/{topic}")
    else:
        return render_template("error.html", message="Jokin meni pieleen")