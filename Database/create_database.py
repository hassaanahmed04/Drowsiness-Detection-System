import sqlite3

connection =sqlite3.connect('AccountSystem.db')
cur=connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS AccountDB(ID INTEGER PRIMARY KEY, FirstName TEXT,LastName TEXT,EMAIL TEXT,Password TEXT)")
connection.commit()
connection.close()