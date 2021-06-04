#note to self this is the code needed to upload to github
#git config --global user.email "you@example.com"
#git config --global user.name "Your Name"

#imports falsk and sqlite3 
from flask import Flask,g,render_template,redirect,request
import sqlite3
app = Flask(__name__)

DATABASE = 'Robotics resource site.db'

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
        cursor = get_db().cursor()
        sql = "SELECT * FROM drive_train"
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template("Mechanisims.html", results=results)

@app.route("/Teams")
def Teams():
        cursor = get_db().cursor()
        sql = "SELECT * FROM team"
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template("Teams.html", results=results)

@app.route("/Editor")
def Editor():
        cursor = get_db().cursor()
        sql = "SELECT * FROM design"
        cursor.execute(sql)
        results1 = cursor.fetchall()

        cursor = get_db().cursor()
        sql = "SELECT * FROM team"
        cursor.execute(sql)
        results2 = cursor.fetchall()

        cursor = get_db().cursor()
        sql = "SELECT * FROM drive_train"
        cursor.execute(sql)
        results3 = cursor.fetchall()
        return render_template("Editor.html", results1=results1, results2=results2, results3=results3)

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route('/add_Robot', methods=["GET","POST"])
def add_Robot():
    if request.method == "POST":
        print("adding")
        cursor = get_db().cursor()
        new_id = request.form["id"]
        new_team_id = request.form["team_id"]
        new_year = request.form["year"]
        new_game = request.form["game"]
        new_train_id = request.form["drive_train_id"]
        sql = "INSERT INTO design(id,team_id,year,game,drive_train_id) VALUES (?,?,?,?,?)"
        cursor.execute(sql,(new_id,new_team_id,new_year,new_game,new_train_id))
        get_db().commit()
    return redirect('/Editor')

@app.route('/delete_Robot', methods=["GET","POST"])
def delete_Robot():
    if request.method == "POST":
        cursor = get_db().cursor()
        id = int(request.form["item_name"])
        sql = "DELETE FROM design WHERE id=?"
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect('/Editor') 

@app.route('/add_teams', methods=["GET","POST"])
def add_teams():
    try:
        if request.method == "POST":
            print("adding")
            cursor = get_db().cursor()
            new_team_id = request.form["id"]
            new_name = request.form["name"]
            sql = "INSERT INTO team (id,name) VALUES (?,?)"
            cursor.execute(sql,(new_team_id,new_name))
            get_db().commit()
    except:
        return redirect('/Error')
    return redirect('/Editor')

@app.route('/delete_teams', methods=["GET","POST"])
def delete_teams():
    if request.method == "POST":
        cursor = get_db().cursor()
        id = int(request.form["item_name"])
        sql = "DELETE FROM team WHERE id=?"
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect('/Editor') 

@app.route('/add_drive_train', methods=["GET","POST"])
def add_drive_train():
    try:
        if request.method == "POST":
            print("adding")
            cursor = get_db().cursor()
            new_drive_train_id = request.form["id"]
            new_type = request.form["type"]
            sql = "INSERT INTO drive_train (id,type) VALUES (?,?)"
            cursor.execute(sql,(new_drive_train_id,new_type))
            get_db().commit()
    except:
        return redirect('/Error')
    return redirect('/Editor')

@app.route('/delete_drive_train', methods=["GET","POST"])
def delete_drive_train():
    if request.method == "POST":
        cursor = get_db().cursor()
        id = int(request.form["item_name"])
        sql = "DELETE FROM drive_train WHERE id=?"
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect('/Editor')

@app.route("/Error")
def Error():
    return render_template("Error.html")

if __name__ == "__main__":
    app.run(debug=True)