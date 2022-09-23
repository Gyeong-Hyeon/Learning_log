import os
import sqlite3

def connect_db():
    db_name = 'questions.db'
    db_path = os.path.join(os.path.dirname(__file__), db_name)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    return conn, cur

def return_history() -> list:
    conn, cur = connect_db()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY,
            name VARCHAR(32),
            question TEXT NOT NULL,
            answer TEXT
        )
        """)
    histories = cur.execute("SELECT * FROM history").fetchall()
    cur.close()
    conn.close()
    return histories

def insert_question(name:str, question:str) -> None:
    conn, cur = connect_db()
    cur.execute("INSERT INTO history (name, question) VALUES (?,?)",(name,question))
    conn.commit()
    cur.close()
    conn.close()
    return None

def update_answer(ques_id, answer:str) -> None:
    conn, cur = connect_db()
    cur.execute("UPDATE history SET answer = ? WHERE id = ?",(answer,ques_id))
    conn.commit()
    cur.close()
    conn.close()
    return None
