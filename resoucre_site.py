#imports falsk and sqlite3 
from flask import Flask,g,render_template,redirect,request
import sqlite3
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/Robots")
def Robots():
    return render_template("Robots.html")

@app.route("/Mechanisims")
def Mechanisims():
    return render_template("Mechanisims.html")

if __name__ == "__main__":
    app.run(debug=True)

