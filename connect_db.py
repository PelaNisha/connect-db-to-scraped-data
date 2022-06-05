import sqlite3

connct =  sqlite3.connect('first.db')
c = connct.cursor()

# c.execute('''CREATE TABLE newTable(name TEXT, age INT, profession TEXT)''')

name = 'Aditya'
age = 15
profession = 'Student'

c.execute('''INSERT INTO newTable VALUES(?,?,?)''',(name, age, profession))
connct.commit()

c.execute('''SELECT * FROM newTable''')
results = c.fetchall()
print(results)