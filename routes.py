from app import app
from flask import render_template, request, redirect
from sqlalchemy.sql import text
import messages, users, threads
topics = ["musiikki", "ruoka", "yliopisto"]

@app.route("/")
def index():
    return render_template("index.html")

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
            return render_template("error.html", message="Väärä käyttäjätunnus tai salasana")

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
        
        if users.name_check(tunnus):
            return render_template("error.html", message="Käyttäjätunnus on jo otettu")
        if len(tunnus) < 2 or len(tunnus) > 15:
            return render_template("error.html", message="Käyttäjätunnuksen sallittu pituus on 2-15 merkkiä")
        if len(salasana1) < 8 or len(salasana1) > 30:
            return render_template("error.html", message="Salasanan sallittu pituus on 8-30 merkkiä")
        if salasana1 != salasana2:
            return render_template("error.html", message="Salasanat eivät täsmää")
        if users.register(tunnus, salasana1):
            return redirect("/")
        else:
            return render_template("error.html", message="Jokin meni pieleen")
    
@app.route("/musiikki")
def musiikki():
    list = threads.get_music_list()
    return render_template("musiikki.html", count=len(list), threads=list)

@app.route("/ruoka")
def ruoka():
    list = threads.get_food_list()
    return render_template("ruoka.html", count=len(list), threads=list)

@app.route("/yliopisto")
def yliopisto():
    list = threads.get_uni_list()
    return render_template("yliopisto.html", count=len(list), threads=list)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    if not users.login_check():
        return render_template("error.html", message="Sinun täytyy olla kirjatunut sisään")
    users.token_check(request.form["csrf_token"])
    
    opening = request.form["opening"]
    title = request.form["title"]
    topic_number = int(request.form["topic"])
    topic = topics[int(request.form["topic"]) - 1]
    if threads.new_thread(title, opening, topic_number):
        return redirect(f"/{topic}")
    else:
        return render_template("error.html", message="Jokin meni pieleen")

@app.route("/musiikki/<int:id>", methods=["POST"])
def choose_thread(id):
    sql = text("SELECT title FROM threads WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    thread = result.fetchone()
    sql = text("SELECT M.content FROM messages M, threads T WHERE M.thread=:id")
    result = db.session.execute(sql, {"M.thread":id})
    messages = result.fetchall()
    return render_template("musiikki.html", id=id, thread=thread, messages=messages)