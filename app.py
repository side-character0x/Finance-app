from flask import Flask,render_template,request,session
from db import Database
import os
import sys
import webbrowser
import threading
import time

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(base_path, 'templates')
app = Flask(__name__, template_folder=template_folder)
app.secret_key = "secret"
@app.route("/")
def base():
    return render_template("base.html")
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("name")
        pin=request.form.get("pin")
        db_pin=Database().check_user(username)
        if db_pin!=pin or pin is None:
            return render_template("login.html",error=True)
        else:
            session["username"]=username
            return render_template("home.html",balance=Database().get_data(username,"balance"),username=username)
    return render_template("login.html")

@app.route("/signin", methods=["GET","POST"])
def signin():
    if request.method=="POST":
        username=request.form.get("name")
        session["username"]=username
        pin=request.form.get("pin")
        if len(pin)!=4 or not pin.isdigit():
            return render_template("entry.html",error=True)
        Database().add_user(username,pin)
        return render_template("home.html",balance=Database().get_data(username,"balance"),username=username)
    return render_template("entry.html")
@app.route("/home",methods=["POST"])
def home():
    username=session.get("username")
    action=request.form.get("action")
    income_amount=request.form.get("income")
    expense_amount=request.form.get("expense")
    if action=="income":
        return render_template("home.html",income=True,balance=Database().get_data(username,"balance"),username=username)
    elif action=="back":
        return render_template("login.html")
    elif action=="expense":
        return render_template("home.html",expense=True,balance=Database().get_data(username,"balance"),username=username)
    if income_amount is not None:
        Database().add_balance(username,income_amount)
    if expense_amount is not None:
        Database().reduce_bal(username,expense_amount)
    return render_template("home.html",balance=Database().get_data(username,"balance"),username=username)

def open_browser():
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=open_browser, daemon=True).start()
    app.run()
