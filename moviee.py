# importing the module
import sqlite3
# creating an connection
conn = sqlite3.connect("movie.db") # db - database
# Cursor object
cursor = conn.cursor()# importing the module
#create table
cursor.execute("""CREATE TABLE MOVIES (id INTEGER PRIMARY KEY,movie_name VARCHAR(20)
,lead_actor VARCHAR(20),lead_actress VARCHAR(20),director_name VARCHAR(20),release_year VARCHAR(20)""")
#insert movie list in the table
cursor.execute(""" INSERT INTO MOVIES VALUES(1,'Wonder Woman 1984','Gal Gadot',' Kristen Wiig',
' Patty Jenkins','December 25th 2020')""")
cursor.execute(""" INSERT INTO MOVIES VALUES(2,'Cinderella ',' Denzel Washington',' Rami Malek',
' Kay Cannon','February 5th 2021')""")
cursor.execute(""" INSERT INTO MOVIES VALUES(3,' Tom & Jerry: The Movie',' Chloë Grace Moretz', 'Michael Peña',
' Tim Story','February 26th 2021')""")
cursor.execute(""" INSERT INTO MOVIES VALUES(4,'Everybody's Talking About Jamie',' Lauren Patel', 'Sarah Lancashire',
' Jonathan Butterell','February 26th 2021')""")
cursor.execute(""" INSERT INTO MOVIES VALUES(5 ,'Nobody',' Bob Odenkirk',' Aleksey Serebryakov',
'  Ilya Naishuller','February 26th 2021')""")

#query all data in the table
cursor.execute("SELECT * FROM MOVIES")
#query only lead actor name in the movie list 
cursor.execute("SELECT lead_actor FROM MOVIES")
# saving the changes using commit method of connection
conn.commit()
# closing the connection
conn.close()
