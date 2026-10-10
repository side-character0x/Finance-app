import sqlite3

class Database:
    def __init__(self):
        self.conn=sqlite3.connect("finance.db")
        self.conn.row_factory=sqlite3.Row
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username TEXT,pin TEXT)")
    def add_user(self,username,pin):
        self.cur.execute("INSERT INTO users(username,pin) VALUES(?,?)",(username,pin))
        self.conn.commit()
        self.conn.close()
    def check_user(self,username):
        pin=self.cur.execute("SELECT pin FROM users WHERE username=?",(username,)).fetchone()
        return pin["pin"]




