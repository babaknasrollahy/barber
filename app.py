from flask import Flask, render_template
import barbers
import sqlite3

app = Flask(__name__)

@app.route("/table")
def create_table():
    test = barbers.create_table()
    return f"{test}"

@app.route("/status")
def status():
    db = sqlite3.connect('./database.sql')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = cursor.fetchall()
    print(result)
    return result

@app.route("/write")
def write_data():
    for item in range(1,3000000):
        barbers.create_barber(item,f"{item}", item, item, item , f"{item}", item , item)
    return "finish"

@app.route("/")
def home():
    data_list = [ {"x": 35.722344529568815,"y": 51.420510209408484}, {"x":35.722344529568815 ,"y":51.0510209408484 }]
    return render_template("test.html", data=data_list)

@app.route("/print")
def print_test():
    test = barbers.get_all_procuts()
    test = len(test)
    return f"{test}"
if __name__ == "__main__":
    app.run(debug=True)
