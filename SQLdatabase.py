
import sqlite3
from sqlite3.dbapi2 import Cursor, connect
connection = sqlite3.connect("test_database.db")
print(type(connection))
cursor = connection.cursor()
print(type(cursor))
query = "SELECT datetime('now', 'localtime');"
results = cursor.execute(query)
print(results)
row = results.fetchone()
print("row = ", row)
time = row[0]
print("time = ",time)
print("time2 = ",time)
connection.close()



# with sqlite3.connect("test_database.db") as connection:
#         cursor = connection.cursor()
#         query = "SELECT datetime('now', 'localtime');"
#         print("This is the query", query)
#         results = cursor.execute(query)
#         print("These are the results", results)
#         row = results.fetchone()
#         print("This the row", row)
#         time = row[0]

#         print(time)
# import sqlite3
# sql = """
# DROP TABLE IF EXISTS People;
# CREATE TABLE People(
#     First Name TEXT,
#     Last Name TEXT,
#     Age INT
# );
# INSERT INTO People VALUES(
#     ('Jeff', 'Blau', 65),
#     ('Larry', 'Switzer', 61),
#     ('Joe', 'Biden', 78)
# );"""



