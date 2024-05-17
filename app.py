from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    test_list = [(35.722344529568815,51.420510209408484), (35.722344529568815 ,51.0510209408484 )]
    return render_template("test.html", test=test_list)



if __name__ == "__main__":
    app.run(debug=True)