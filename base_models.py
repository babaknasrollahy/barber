import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor


def create_table():
    issucess = True
    try:
        db,cursor = create_db()
        query = """CREATE TABLE base_models (
                            base_model_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            base_model_name VARCHAR(100),
                            create_time TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
                            );"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
    except:
        issucess = False

    return issucess



def create_base_model(model_name):
    issucess = True
    try:
        db , cursor = create_db()
        query = """INSERT INTO base_models (base_model_name)
                   VALUES (?)
"""
        cursor.execute(query, (model_name,))
        db.commit()
        cursor.close()
        db.close()
    except:
        issucess = False

    return issucess


def get_base_model():
    issucess = True
    try:
        db , cursor = create_db()
        query = """SELECT base_model_name FROM base_models"""
        result = cursor.execute(query).fetchall()
        db.commit()
        cursor.close()
        db.close()
        print(result)
    except:
        issucess = False

    return result


def get_base_model_id(base_model_name):
    issucess = True
    try:
        db , cursor = create_db()
        query = """SELECT base_model_id FROM base_models WHERE base_model_name = ?"""
        result = cursor.execute(query, (base_model_name,)).fetchall()[0][0]
        print("============"+result)
        db.commit()
        cursor.close()
        db.close()
        print(result)
    except:
        issucess = False

    return result