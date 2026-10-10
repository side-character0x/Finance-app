from flask import Flask,render_template,request
from db import Database
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("name")
        pin=request.form.get("pin")
        db_pin=Database().check_user(username)
        if db_pin!=pin:
            return render_template("login.html",error=True)
    return render_template("login.html")

@app.route("/signin", methods=["GET","POST"])
def signin():
    if request.method=="POST":
        username=request.form.get("name")
        pin=request.form.get("pin")
        if len(pin)!=4 or not pin.isdigit():
            return render_template("entry.html",error=True)
        Database().add_user(username,pin)
    return render_template("entry.html")
app.run(debug=True)
