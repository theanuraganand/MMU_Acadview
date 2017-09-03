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
        insertstmt = ("INSERT INTO SPY VALUES ('%s', '%s', '%s', '%s', '%s')" % (str(spy['name']), str(spy['salutation']), str(spy['age']), str(spy['rating']), str(spy['is_online'])))
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
