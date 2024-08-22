import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor

# tags => SET
def create_table():
    issucess = True
    try:
        db,cursor = create_db()
        query = """CREATE TABLE comments (
                            comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            tags VARCHAR(500),
                            shop_id INTEGER,
                            comment VARCHAR(800),
                            create_time TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
                            );"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
    except:
        issucess = False

    return issucess