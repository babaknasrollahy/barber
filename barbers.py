import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor


def create_table():
    issucess = True
    try:
        db,cursor = create_db()
        query = """CREATE TABLE barbers (
                            barber_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            image VARCHAR(500),
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



def create_barber(user_id , image , national_code , age, experience, about , shop_id , count):
    issucess = True
    try:
        db,cursor = create_db()
        add_product = """INSERT INTO barbers (user_id, image, national_code, age, experience, about , shop_id)
                        VALUES ( ?, ?, ? , ? , ? , ? , ?)"""

        cursor.execute(add_product , (user_id , image , national_code , age, experience, about , shop_id))
        db.commit()
        cursor.close()
    except:
        issucess = False
    return issucess


def get_all_procuts():
    is_success = True
    db, sql_cursor = create_db()
    try:
        get_all = """SELECT * FROM barbers"""
        test = sql_cursor.execute(get_all)
        result = test.fetchall()
    except Exception as e:
        print(e)
        is_success = False
    finally:
        sql_cursor.close()
        db.close()

    return result