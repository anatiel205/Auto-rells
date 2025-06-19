crud.py

import sqlite3

DB_PATH = "database.db"

def init_db(): conn = sqlite3.connect(DB_PATH) c = conn.cursor() c.execute('''CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, instagram_id TEXT NOT NULL, access_token TEXT NOT NULL, search_term TEXT, caption TEXT, post_interval INTEGER DEFAULT 15, is_authorized INTEGER DEFAULT 0 )''') conn.commit() conn.close()

def add_user(instagram_id, access_token, search_term, caption, post_interval=15): conn = sqlite3.connect(DB_PATH) c = conn.cursor() c.execute("INSERT INTO users (instagram_id, access_token, search_term, caption, post_interval) VALUES (?, ?, ?, ?, ?)", (instagram_id, access_token, search_term, caption, post_interval)) conn.commit() conn.close()

def get_user(user_id): conn = sqlite3.connect(DB_PATH) c = conn.cursor() c.execute("SELECT * FROM users WHERE id = ?", (user_id,)) user = c.fetchone() conn.close() return user

def list_users(): conn = sqlite3.connect(DB_PATH) c = conn.cursor() c.execute("SELECT * FROM users") users = c.fetchall() conn.close() return users

def authorize_user(user_id): conn = sqlite3.connect(DB_PATH) c = conn.cursor() c.execute("UPDATE users SET is_authorized = 1 WHERE id = ?", (user_id,)) conn.commit() conn.close()

def update_caption(user_id, new_caption): conn = sqlite3.connect(DB_PATH) c = conn.cursor() c.execute("UPDATE users SET caption = ? WHERE id = ?", (new_caption, user_id)) conn.commit() conn.close()

