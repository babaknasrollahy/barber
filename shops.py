import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor

# location => SET
# open_time => SET
def create_table():
    issucess = True
    try:
        db,cursor = create_db()
        query = """CREATE TABLE shops (
                            shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            image VARCHAR(1000) ,
                            location VARCHAR(500),
                            shop_name VARCHAR(100),
                            about VARCHAR(800),
                            create_time TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
                            );"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
    except:
        issucess = False

    return issucess


def get_all_info_of_shops(user_id):
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT image, location,shop_name , about from shops WHERE user_id = ?"""
        result = cursor.execute(query, (user_id,)).fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        is_success = False
        print("---------------\n", e)
    return result


def update_shop_info(user_id,image,location, shop_name ,about):
    is_success = True
    db , cursor = create_db()
    try:
        query = """UPDATE shops
                    SET image = ? , location = ?  , shop_name = ? , about = ?
                    WHERE user_id = ?"""
        cursor.execute(query, (image,location, shop_name, about,user_id))
        db.commit()
        cursor.close()
        db.close()
    except:
        is_success = False

    return is_success

def is_shop_exist(user_id):
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT * from shops WHERE user_id = ?"""
        print("before res")
        res = cursor.execute(query, (user_id,)).fetchall()[0]
        print("after res")
        cursor.close()
        db.close()
    except Exception as e :
        is_success = False
        print(e)

    return is_success


def create_shop(user_id,image,location, shop_name, about):
    is_success = True
    db , cursor = create_db()
    try:
        query = """INSERT INTO shops (user_id, image,location, shop_name, about)
                    VALUES (? , ? ,? , ?, ?)"""
        cursor.execute(query, (user_id,image,location, shop_name, about))
        db.commit()
        cursor.close()
        db.close()
    except:
        is_success = False

    return is_success


def get_shop_id_by_user_id(user_id):
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT shop_id FROM shops WHERE user_id = ?"""
        result = cursor.execute(query, (user_id,)).fetchall()[0][0]
        cursor.close()
        db.close()
    except Exception as e:
        is_success = False
        print("---------------\n", e)
    return result


def get_all_shops():
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT s.shop_id, u.user_name, s.image, s.shop_name 
                    FROM shops as s
                    JOIN users as u
                        ON  s.user_id = u.user_id"""
        result = cursor.execute(query).fetchall()
        cursor.close()
        db.close()
    except Exception as e:
        is_success = False
        print("---------------\n", e)
    return result