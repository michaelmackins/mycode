import sqlite3

dbconnect= sqlite3.connect("demo.db")

dbconnect.execute("""CREATE TABLE IF NOT EXISTS MOVIES
                     

