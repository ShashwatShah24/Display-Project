from flask import *  
import sqlite3  
  
app = Flask(__name__)   

@app.route("/")  
def index():  
    return render_template("feedback.html")

@app.route("/savedetails121",methods = ["POST"])  
def saveDetails121():
	msg="msg"
	name = request.form["Name"]
	print(name)
	authors = request.form["Author"]
	print(authors)
	Description = request.form["Feedback"]
	print(Description)
	with sqlite3.connect("DisplayProject.db") as con:
		cur = con.cursor()
		cur.execute("INSERT into ProjectTable (Name,authors,Description) values (?,?,?)",(name,authors,Description))
		print("execute")
		con.commit()
		print("commit")
		msg="feedback success"
		return render_template("success01.html",msg=msg)






if __name__ == "__main__":
	app.run(host='127.0.0.1', port=7071)  