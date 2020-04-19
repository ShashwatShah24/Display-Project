from flask import *
import sqlite3  
  
app = Flask(__name__)  

@app.route("/")  
def index():
	global rows1
	global rows
	rows1 =[]
	rows =[]
	con = sqlite3.connect("DisplayProject.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	cur.execute("SELECT * FROM ProjectTable")
	rows=cur.fetchall()
	return render_template("View.html",rows=rows,rows1=rows1)

@app.route("/viewTable",methods =["POST"])  
def viewTable():
  projectName = request.form["tab"]
  print()
  con = sqlite3.connect("DisplayProject.db")
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute("select * from ProjectTable where Name = '{0}'".format(projectName))
  rows1=cur.fetchall()
  for i in rows1:
  	a=i[0]
  	b=i[1]
  	c=i[2]
  	d=i[3]
  return render_template("view.html",rows=rows,rows1=rows1,a=a,b=b,c=c,d=d) 


if __name__ == "__main__":
	app.run(host='127.0.0.1', port=9091)  
