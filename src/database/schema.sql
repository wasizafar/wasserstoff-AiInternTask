-- schema.sql

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    sender TEXT,
    recipient TEXT,
    subject TEXT,
    timestamp TEXT,
    body TEXT,
    cleaned_body TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
