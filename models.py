import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor


def create_table():
    issucess = True
    try:
        db,cursor = create_db()
        query = """CREATE TABLE models (
                            model_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            model_name VARCHAR(100),
                            price INTEGER,
                            shop_id INTEGER,
                            time VARCHAR(800),
                            create_time TIMESTAMP DEFAULT (DATETIME('now', 'localtime')),
                            base_model_id INTEGER
                            );"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
        db.close()
    except:
        issucess = False

    return issucess




def create_model(model_name, price, shop_id, time, base_model_id):
    issucess = True
    try:
        db,cursor = create_db()
        query = """INSERT INTO models (model_name, price, shop_id, time, base_model_id)
                    VALUES (?,?,?,?,?)"""

        cursor.execute(query,(model_name, price, shop_id, time, base_model_id))
        print("after")
        db.commit()
        cursor.close()
        db.close()
    except:
        issucess = False

    return issucess



def get_all_models():
    issucess = True
    try:
        db,cursor = create_db()
        query = """SELECT model_name, price, time FROM models"""
        result = cursor.execute(query).fetchall()
        print("after")
        db.commit()
        cursor.close()
        db.close()
    except:
        issucess = False

    return result



def get_models_for_a_shop(shop_id):
    issucess = True
    try:
        db,cursor = create_db()
        query = """SELECT m.model_name, m.price, m.time , s.shop_name , m.model_id, s.shop_id
                    FROM models as m
                    JOIN shops as s
                        ON m.shop_id = s.shop_id
                    WHERE m.shop_id = ?
"""
        result = cursor.execute(query, (shop_id,)).fetchall()
        print("after")
        db.commit()
        cursor.close()
        db.close()
    except:
        issucess = False

    return result