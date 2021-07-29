import sqlite3
conn = sqlite3.connect('movies.db')

c = conn.cursor()

c.execute("""CREATE TABLE Movies (
         name TEXT,
         actor TEXT,
         actress TEXT,
         director TEXT,
         year_released INTEGER  
) """)

c.execute("""INSERT INTO Movies VALUES ("Malik","Fahad Fasil","Nimisha","Mahesh Narayanan",2021)""")

c.execute("""INSERT INTO Movies VALUES ("Sara's","Sunny Wein","Anna Ben","Jude Antony",2021)""")

c.execute("""INSERT INTO Movies VALUES ("1983","Nivin Poly","Srinda","Abrid Shine",2014)""")

c. execute("""SELECT * FROM Movies""")

c. execute("""SELECT * FROM Movies WHERE actor = "Nivin Poly"""")
conn.commit()
conn.close()


