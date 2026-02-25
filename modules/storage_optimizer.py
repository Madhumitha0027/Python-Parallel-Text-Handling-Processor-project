import sqlite3

def create_index():
    conn = sqlite3.connect("texts.db")
    cursor = conn.cursor()

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_score ON texts(score)")
    conn.commit()
    conn.close()