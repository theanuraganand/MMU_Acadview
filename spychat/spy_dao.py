import MySQLdb
from spyDetails import spy
from globals import friends

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
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "qwe321", "SPY")
    print "Connected"
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = 'SELECT * FROM SPY WHERE NAME = "' + name +'"'
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            print row[0], row[1], row[3], row[4], row[5]
            spy['name'] = str(row[0])
            spy['salutation'] = str(row[1])
            spy['age'] = int(row[2])
            spy['rating'] = float(row[3])
            spy['is_online'] = bool(row[4])
            spy['pass'] = str(row[5])
            # Now print fetched result
            print spy['name']
    except:
        print "Error: unable to fecth data"

        # disconnect from server
    db.close()

def read_all(name):
    # Open database connection
    db = MySQLdb.connect("localhost", "root", "qwe321", "SPY")
    print "Connected"
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = 'SELECT * FROM SPY_FRIEND where friendname = ' + name
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            print row[0], row[1], row[3], row[4], row[5]
            spy['name'] = str(row[0])
            spy['salutation'] = str(row[1])
            spy['age'] = int(row[2])
            spy['rating'] = float(row[3])
            spy['is_online'] = bool(row[4])
            spy['pass'] = str(row[5])
            # Now print fetched result
            friends.append(spy)
        #print spy['name']
    except:
        print "Error: unable to fecth data"

        # disconnect from server
    db.close()

def add_spyfriend(name):
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
        insertstmt = ("INSERT INTO SPY_FRIENDS VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (str(friends['name']), str(friends['salutation']), str(friends['age']), str(friends['rating']), str(friends['is_online']), str(friends['pass']), name))
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
