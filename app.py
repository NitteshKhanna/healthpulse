from flask import Flask, request, jsonify, render_template,redirect
import sqlite3
app=Flask(__name__)

con=sqlite3.connect("db.db")
con.execute("CREATE TABLE IF NOT EXISTS users (fname VARCHAR(25),lname VARCHAR(25),ph int,mail VARCHAR(100), message VARCHAR(300))")
con.commit()
con.close() 

@app.route("/")
def default():
    return render_template("index.html")

@app.route("/db")
def dis():
    con=sqlite3.connect("db.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM users")
    a=cur.fetchall()
    con.close()
    return a

@app.route("/db",methods=['POST'])
def defualt():
    fname=request.form.get('fname')
    lname=request.form.get('lname')
    ph=request.form.get('ph')
    mail=request.form.get('mail')
    message=request.form.get('message')
    query=f"INSERT INTO users VALUES ('{fname}','{lname}','{ph}','{mail}','{message}')"
    con=sqlite3.connect("db.db")
    con.execute(query)
    con.commit()
    con.close()
    return redirect("/")

@app.route("/del")
def dele():
    con=sqlite3.connect("db.db")
    con.execute("DELETE FROM users")
    con.commit()
    return "DELETED"

if __name__=="__main__":
    app.run(debug=True)