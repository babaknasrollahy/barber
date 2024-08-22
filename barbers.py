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
                            create_time TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
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


def get_all_barbers():
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT * from barbers """
        result = cursor.execute(query).fetchall()
        cursor.close()
        db.close()
    except:
        is_success = False

    return result

def get_all_info_of_barbers(user_id):
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT image, national_code,age , experience , about from barbers WHERE user_id = ?"""
        result = cursor.execute(query, (user_id,)).fetchall()[0]
        cursor.close()
        db.close()
    except Exception as e:
        is_success = False
        print("---------------\n", e)

    return result

def get_nessecury_info_of_barber(user_id):
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT image, national_code,age , experience from barbers
                    WHERE user_id= ?"""
        result = cursor.execute(query, (user_id,)).fetchall()[0]
        cursor.close()
        db.close()
    except:
        is_success = False

    return result


def update_barber_info(user_id,image,national_code, age , experience, about):
    is_success = True
    db , cursor = create_db()
    try:
        query = """UPDATE barbers
                    SET image = ? , national_code = ?  , age = ? , experience = ? , about = ?
                    WHERE user_id = ?"""
        cursor.execute(query, (image,national_code, age , experience, about,user_id))
        db.commit()
        cursor.close()
        db.close()
    except:
        is_success = False

    return is_success