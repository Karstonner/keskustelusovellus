from db import db
from sqlalchemy.sql import text

def get_music_list():
    sql = text("SELECT H.title, H.opening FROM threads H, topics O WHERE H.topic = O.id AND O.name = 'musiikki'")
    result = db.session.execute(sql)
    return result.fetchall()

def get_food_list():
    sql = text("SELECT H.title, H.opening FROM threads H, topics O WHERE H.topic = O.id AND O.name = 'ruoka'")
    result = db.session.execute(sql)
    return result.fetchall()

def get_uni_list():
    sql = text("SELECT H.title, H.opening FROM threads H, topics O WHERE H.topic = O.id AND O.name = 'yliopisto'")
    result = db.session.execute(sql)
    return result.fetchall()

def new_thread(title, opening, topic):
    sql = text("INSERT INTO threads (title, opening, topic) VALUES (:title, :opening, :topic)")
    db.session.execute(sql, {"title":title, "opening":opening, "topic":topic})
    db.session.commit()
    return True