import sqlite3

DB_PATH = "data/emails.db"

def create_table():
    # create the emails thable if not exists
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
                   id TEXT PRIMARY KEY,
                   subject TEXT,
                   sender TEXT,
                   recipient TEXT,
                   date TEXT,
                   body TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_email(email_data):
    """Save email to database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO emails (id, subject, sender, recipient, date, body) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (email_data["id"], email_data["subject"], email_data["from"], email_data["to"], email_data["date"], email_data["body"]))
    conn.commit()
    conn.close()

# Create the table when this script runs
if __name__ == "__main__":
    create_table()
    print("Database setup completed!")
