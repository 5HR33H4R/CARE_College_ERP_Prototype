from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_student")
def add_student():
    return render_template("add_student.html")


@app.route("/edit")
def edit():
    return render_template("edit.html")


if __name__ == '__main__':
    app.run(debug=True)
