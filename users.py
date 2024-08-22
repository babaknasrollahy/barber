import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor


def create_table():
    issucess = True
    try:
        db,cursor = create_db()
        query = """CREATE TABLE users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_name VARCHAR(50) UNIQUE NOT NULL,
                            avatar VARCHAR(1000) ,
                            number INTEGER UNIQUE NOT NULL,
                            email VARCHAR(100),
                            password VARCHAR(25),
                            gender INTEGER,
                            full_name VARCHAR(50),
                            role INTEGER,
                            create_time TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
                            );"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
    except:
        issucess = False

    return issucess


def create_user(user_name, avatar, number, email, password, gender, full_name, role):
    is_success = True
    db , cursor = create_db()
    try:
        query = """INSERT INTO users (user_name, avatar, number, email, password, gender, full_name, role)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ? );"""
        cursor.execute(query, (user_name, avatar, number, email, password, gender, full_name, role))
        db.commit()
        cursor.close()
        db.close()
    except:
        is_success = False

    return is_success


def get_all_info_of_user():
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT * from users"""
        result = cursor.execute(query).fetchall()
        db.commit()
        cursor.close()
        db.close()
    except:
        is_success = False

    return result


def user_info(user_id):
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT user_id, avatar ,user_name , number, email, gender, full_name, role from users
                    WHERE number = ?"""
        result = cursor.execute(query, (user_id,)).fetchall()
        db.commit()
        cursor.close()
        db.close()
    except:
        is_success = False

    return result


def check_login(number):
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT password from users
                    WHERE number = ?"""
        result = cursor.execute(query, (number,)).fetchall()[0][0]
        db.commit()
        cursor.close()
        db.close()
    except:
        is_success = False
        return False
    return result


def get_all_users():
    is_success = True
    db , cursor = create_db()
    try:
        query = """SELECT user_id, avatar ,user_name , number, email, gender,password, full_name, role from users"""
        result = cursor.execute(query).fetchall()
        db.commit()
        cursor.close()
        db.close()
    except:
        is_success = False

    return result


def get_user_id_and_role_by_number(number):
    try:
        db , cursor = create_db()
        query = """SELECT user_id,role from users
          WHERE number = ?;
"""
        result = cursor.execute(query,(number,)).fetchall()[0]
        cursor.close()
        db.close()

    except Exception as e:
        return f"error == {e}"

    return result

def get_user_id_by_number(number):
    try:
        db , cursor = create_db()
        query = """SELECT user_id from users
          WHERE number = ?;
"""
        result = cursor.execute(query,(number,)).fetchall()[0]
        cursor.close()
        db.close()

    except Exception as e:
        return f"error == {e}"

    return result