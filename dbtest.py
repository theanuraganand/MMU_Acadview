

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","qwe321","Spy" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# # execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")
#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
#
# print "Database version : %s " % data

# Create table as per requirement
sql = """CREATE TABLE SPY (
         NAME  CHAR(20) NOT NULL,
         SALUTATION  CHAR(20),
         AGE INT,
         RATING FLOAT,  
         ISONLINE CHAR(1))"""

cursor.execute(sql)


# disconnect from server
db.close()