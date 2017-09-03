from newUser import new_spy
from spy_dao import create_spy
print ("Spy Chat Started")
answer = raw_input("Do you want to continue using Default User (Y/N")
if answer == "Y":
    print "OK"
elif answer == "N":
    new_spy()
    create_spy()