import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor


def create_table():
    issucess = True
    try:
        db,cursor = create_db()
        query = """CREATE TABLE shops (
                            shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            national_code INTEGER ,
                            age INTEGER,
                            experience INTEGER,
                            about VARCHAR(800),
                            shop_id INTEGER,
                            message_time TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
                            );"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
    except:
        issucess = False

    return issucess