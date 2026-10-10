import sqlite3

class Database:
    def __init__(self):
        self.conn=sqlite3.connect("finance.db")
        self.conn.row_factory=sqlite3.Row
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS data(username TEXT,pin TEXT,balance NUMBER)")
    def add_user(self,username,pin):
        self.cur.execute("INSERT INTO data(username,pin,balance) VALUES(?,?,0)",(username,pin,))
        self.conn.commit()
        self.conn.close()
    def check_user(self,username):
        pin=self.cur.execute("SELECT pin FROM data WHERE username=?",(username,)).fetchone()
        self.conn.close()
        if pin is None:
            return pin
        else:
            return pin["pin"]
    def get_data(self,username,field):
        data=self.cur.execute(f"SELECT {field} FROM data WHERE username=?",(username,)).fetchone()
        self.conn.close()
        return data[field]
    def add_balance(self,username,amount):
        self.cur.execute("UPDATE data SET balance=balance+? WHERE username=?",(amount,username))
        self.conn.commit()
        self.conn.close()
    def reduce_bal(self,username,amount):
        self.cur.execute("UPDATE data SET balance=balance-? WHERE username=?",(amount,username))
        self.conn.commit()
        self.conn.close()




