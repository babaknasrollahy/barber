from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data_list = [ {"x": 35.722344529568815,"y": 51.420510209408484}, {"x":35.722344529568815 ,"y":51.0510209408484 }]
    return render_template("test.html", data=data_list)

if __name__ == "__main__":
    app.run(debug=True)