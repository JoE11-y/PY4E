import sqlite3

conn = sqlite3.connect("MyMusic.sqlite")
cur = conn.cursor()

cur.execute("INSERT INTO Music_List (Artist, No_of_Song) VALUES (?, ?)", ("Eminem", 20))
cur.execute("INSERT INTO Music_List (Artist, No_of_Song) VALUES (?, ?)", ("Asa", 31))
conn.commit()

cur.execute('SELECT Artist, No_of_Song FROM Music_List')
for row in cur:
    print(row)

cur.execute('DELETE FROM Music_List WHERE No_of_Song < 100')
conn.commit()


cur.close()
