from db import db
from sqlalchemy.sql import text

def get_music_list():
    sql = text("SELECT content, sent_at FROM messages WHERE topic = 'musiikki' ORDER BY sent_at DESC")
    result = db.session.execute(sql)
    return result.fetchall()

def get_food_list():
    sql = text("SELECT content, sent_at FROM messages WHERE topic = 'ruoka' ORDER BY sent_at DESC")
    result = db.session.execute(sql)
    return result.fetchall()

def get_uni_list():
    sql = text("SELECT content, sent_at FROM messages WHERE topic = 'yliopisto' ORDER BY sent_at DESC")
    result = db.session.execute(sql)
    return result.fetchall()
    
def send(content, thread):
    sql = text("INSERT INTO messages (content, topic, sent_at) VALUES (:content, :topic, NOW())")
    db.session.execute(sql, {"content":content, "topic":topic})
    db.session.commit()
    return True