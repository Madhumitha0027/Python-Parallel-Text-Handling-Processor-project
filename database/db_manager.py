import sqlite3

DB_NAME = "texts.db"

def create_table():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS texts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_chunk TEXT,
            score INTEGER,
            tag TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute(
        "CREATE INDEX IF NOT EXISTS idx_tag ON texts(tag)"
    )

    conn.commit()
    conn.close()


# -------------------------------------------------
# SINGLE INSERT
# -------------------------------------------------
def insert_result(text, score, tag):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO texts(text_chunk,score,tag) VALUES(?,?,?)",
        (text, score, tag)
    )

    conn.commit()
    conn.close()


# -------------------------------------------------
# BULK INSERT (executemany)
# -------------------------------------------------
def bulk_insert(rows):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO texts(text_chunk,score,tag) VALUES(?,?,?)",
        rows
    )

    conn.commit()
    conn.close()


# -------------------------------------------------
# FETCH ALL DATA
# -------------------------------------------------
def fetch_all():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM texts")
    data = cursor.fetchall()

    conn.close()
    return data

def clear_table():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM texts")

    conn.commit()
    conn.close()
