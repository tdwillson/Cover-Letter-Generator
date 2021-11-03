from flask import render_template, Flask, request
import sqlite3

app = Flask(__name__)

# Index - Where you will input info for cover letter
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        company = request.form.get("company")
        if not company:
            return "No company entered"
        position = request.form.get("position")
        if not position:
            return "No position entered"
        addon = request.form.get("addon")
        db = sqlite3.connect("letter.db")
        c = db.cursor()
        c.execute(f"INSERT INTO letters (company, position, addon) VALUES ('{company}','{position}','{addon}'")
        c.commit()
        return render_template("coverletter.html", company=company, position=position, addon=addon)