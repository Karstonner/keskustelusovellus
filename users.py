from db import db
from sqlalchemy.sql import text
from flask import session, abort
import secrets
from werkzeug.security import check_password_hash, generate_password_hash

def login(tunnus, salasana):
    sql = text("SELECT id, salasana FROM users WHERE tunnus=:tunnus")
    result = db.session.execute(sql, {"tunnus":tunnus})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.salasana, salasana):
            session["user_id"] = user_id
            session["tunnus"] = tunnus
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["tunnus"]
    del session["csrf_token"]

def register(tunnus, salasana):
    hash_value = generate_password_hash(salasana)
    try:
        sql = text("INSERT INTO users (tunnus,salasana) VALUES (:tunnus,:salasana)")
        db.session.execute(sql, {"tunnus":tunnus, "salasana":hash_value})
        db.session.commit()
    except:
        return False
    return login(tunnus, salasana)

def user_id():
    return session.get("user_id", 0)

def login_check():
    return "user_id" in session

def token_check(csrf_token):
    if session["csrf_token"] != csrf_token:
        abort(403)

def name_check(tunnus):
    sql = text("SELECT tunnus FROM users WHERE tunnus=:tunnus")
    result = db.session.execute(sql, {"tunnus":tunnus})
    if result.fetchone():
        return True
    else:
        return False