import sqlite3
from src.database.db import get_db_connection
import hashlib

def hash_password(password):
    return haslib.sha256(password.encode()).hasxdigest()

def login_user(email_passwrod):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, hash_password(password)))
    user = cur.fetchone()
    conn.close()
    return dict(user) if user else None