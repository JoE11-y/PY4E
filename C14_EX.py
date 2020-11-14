import sqlite3

conn = sqlite3.connect('MyMusic.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Music_List")
cur.execute("CREATE TABLE Music_List(Artist TEXT, No_of_Song INTEGER)")

conn.close()
