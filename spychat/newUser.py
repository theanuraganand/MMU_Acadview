from spyDetails import spy
import re


def new_spy():
    spy['name'] = raw_input("Hey! Whats your name?")
    # check for null string
    if len(spy['name']) > 0:
        match_obj = re.match('^[a-zA-Z\s]+$', spy['name'])
        if match_obj:
            # salutation based on Gender and Marrital Status
            gender = raw_input("Gender? M/F")
            gender.capitalize()
            if gender == 'M':
                spy['salutation'] = "Mr."
            elif gender == "F":
                married = raw_input("Are you Married? Y?N")
                married.capitalize()
                if married == "Y":
                    spy['salutation'] = "Mrs."
                elif married == "N":
                    spy['salutation'] = "Ms."
                else:
                    print "Invalid Input Try Again"
            else:
                print "Invalid input Try Again"
        else:
            print "Invalid Characters for Name"
    else:
        print "Invalid Length of Name"

    while True:
        try:
            # converts age-String to int
            spy['age'] = int(raw_input("Enter your age. ?"))
            break
        except ValueError:
            print "Invalid Age Input. Try again."

    # concats sal and name
    spy['name'] = spy['salutation'] + " " + spy['name']

    while True:
        try:
            # converts rating-String to float
            spy['rating'] = float(raw_input("What is your spy rating?"))
            break
        except ValueError:
            print "Invalid Rating Input. Try again."
    # Sets Spy is Online
    spy['is_online'] = True
    spy['pass'] = raw_input("Enter New Password")
    print spy['name'] + str(spy['age']) + str(spy['rating'])
