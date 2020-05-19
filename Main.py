from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    global rows1
    global rows
    rows1 = []
    rows = []
    con = sqlite3.connect("q12.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Feedback")
    rows = cur.fetchall()
    return render_template("View.html", rows=rows, rows1=rows1)


@app.route("/viewTable", methods=["POST"])
def viewTable():
	phase=[]
	AssignedDevloper=[]
	projectName = request.form["tab"]
	print()
	con = sqlite3.connect("q12.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select * from Steps_Table LEFT OUTER JOIN Feedback ON Steps_Table.Feedback_id = Feedback.id  where Feedback.name = '{0}'".format(projectName))
	rows1 = cur.fetchall()
	cur.execute("select * from  Feedback where Feedback.name = '{0}'".format(projectName))
	rows0 = cur.fetchall()
	
	for i in rows1:
		phase.append(i[2])
		AssignedDevloper.append(i[3])
	
	return render_template("view.html", rows0=rows0,rows=rows, rows1=rows1,phase=phase,AssignedDevloper=AssignedDevloper)

	

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9091)
