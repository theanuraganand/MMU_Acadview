import MySQLdb
from spyDetails import spy


def create_spy():
    print "Creating"
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "qwe321", "SPY")
    print "Connected"
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    print "2 Conn"
    try:
        print ( str(spy['name']), str(spy['salutation']), str(spy['age']), str(spy['rating']), str(spy['is_online']))
        # Execute the SQL comman
        insertstmt = ("INSERT INTO SPY VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (str(spy['name']), str(spy['salutation']), str(spy['age']), str(spy['rating']), str(spy['is_online']), str(spy['pass'])))
        cursor.execute(insertstmt)
        # Commit your changes in the database
        print "Before Commit"
        db.commit()
        print "After Commit"
    except:
        print "Error"
        # Rollback in case there is any error
        # db.rollback()

    # disconnect from server
    db.close()

def read_spy(name):
    print("ok")
    print "Creating"
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "qwe321", "SPY")
    print "Connected"
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    print "2 Conn"
    sql = 'SELECT * FROM SPY WHERE NAME = "a"'
    try:
        # Execute the SQL command
        print "3 con"
        cursor.execute(sql)
        print "4 conn"
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        print "5 conn"
        for row in results:
            print row[0], row[1], row[3], row[4], row[5]
            spy['name'] = str(row[0])
            print "6 conn"
            spy['salutation'] = str(row[1])
            print "7 conn"
            spy['age'] = int(row[2])
            print "8 conn"
            spy['rating'] = float(row[3])
            print "9 conn"
            spy['is_online'] = bool(row[4])
            print "10 conn"
            spy['pass'] = str(row[5])
            print "11 conn"
            # Now print fetched result
        print spy['name']
    except:
        print "Error: unable to fecth data"

        # disconnect from server
    db.close()
