import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor


def create_table():
    issucess = True
    try:
        db,cursor = create_db()
        query = """CREATE TABLE open_times (
                            open_time_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            shop_id INTEGER,
                            day VARCHAR(50),
                            start VARCHAR(50),
                            end VARCHAR(50),
                            create_time TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
                            );"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
        db.close()
    except:
        issucess = False

    return issucess



def create_open_time(shop_id,day,start,end):
    is_sucess = True
    db, cursor = create_db()
    try:
        query = """INSERT INTO open_times (shop_id,day,start,end)
                   VALUES (? , ? , ? , ? )
"""
        cursor.execute(query, (shop_id, day , start, end))
        db.commit()
        cursor.close()
        db.close()

    except:
        is_sucess = False
    return is_sucess





def get_open_time_by_shop_id(shop_id):
    is_sucess = True
    db, cursor = create_db()
    try:
        query = """SELECT day, start, end FROM open_times WHERE shop_id = ?
"""
        result = cursor.execute(query, (shop_id,)).fetchall()
        cursor.close()
        db.close()
        print(result)
    except:
        is_sucess = False
    return result

