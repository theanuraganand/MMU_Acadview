from newUser import new_spy
from spy_dao import create_spy
from spy_dao import read_spy
from spyDetails import spy
from start_chat import start_chat
from termcolor import colored

print (colored("\nSpy Chat Started","blue"))
answer = raw_input("Sign In / Sign Up (1/2)")
if answer == "1":
    print "OK"
    name = raw_input("Enter your Spy-name")
    read_spy(name)
    print spy['name'], spy['pass'], "main"
    if spy['name'] == name:
        pas = raw_input("Enter password")
        if spy['pass'] == pas:
            print "login sucess"
            read_spy(name)
            # starting chat application.
            start_chat(spy.name, spy.age, spy.rating, spy.is_online)
        else:
            print "invalid password"
    else:
        print "invalid spy-name"

elif answer == "2":
    new_spy()
    create_spy()
    # starting chat application.
    start_chat(spy.name, spy.age, spy.rating, spy.is_online)