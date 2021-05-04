#imports falsk and sqlite3 
from flask import Flask,g,render_template,redirect,request
import sqlite3
app = Flask(__name__)

DATABASE= 'Robotics resource site.db'

# need in all databases makes connection with database 
def get_db():
    db = getattr(g,'_database',None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# program will need this doesnt matter why it just does
@app.teardown_appcontext
def close_connnection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/Robots")
def Robots():
        cursor = get_db().cursor()
        sql = "SELECT * FROM design"
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template("Robots.html", results=results)

@app.route("/Mechanisims")
def Mechanisims():
    return render_template("Mechanisims.html")

@app.route("/Teams")
def Teams():
    return render_template("Teams.html")

if __name__ == "__main__":
    app.run(debug=True)

