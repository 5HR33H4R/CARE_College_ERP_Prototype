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


@app.route("/maintenance")
def maintenance():
    return render_template("maintenance.html")

@app.route("/Branch_details")
def branchDetails():
    return render_template("Branch_details.html")

@app.route("/Branch_master")
def branchMaster():
    return render_template("Branch_master.html")

if __name__ == '__main__':
    app.run(debug=True)
