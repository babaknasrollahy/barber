import sqlite3

def create_db():
    db = sqlite3.connect("./database.sql")
    cursor = db.cursor()
    return db,cursor


def after_user_insert():
    issucess = True
    try:
        db,cursor = create_db()
        query = """        
CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    IF NEW.role = 1 THEN
        INSERT INTO barbers (user_id)
        VALUES (NEW.user_id);
    END IF;
END //"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
    except Exception as e:
        issucess = False
        print("this is error : ---------\n", e)

    return issucess



def after_create_shop():
    issucess = True
    try:
        db,cursor = create_db()
        query = """        
CREATE TRIGGER after_create_shop
AFTER INSERT ON shops
FOR EACH ROW
BEGIN
        UPDATE barbers
        SET shop_id = NEW.shop_id
        WHERE user_id = (NEW.user_id);
END"""

        cursor.execute(query)
        print("after")
        db.commit()
        cursor.close()
    except Exception as e:
        issucess = False
        print("this is error : ---------\n", e)

    return issucess