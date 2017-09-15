from spy_details import Spy, friends
import re
from termcolor import colored

# meathod to add new frnd
def add_friend():
    # using class spy
    new_friend = Spy(" ", " ", 0, 0.0) #initializing default values

    # input from  user for name and salutation of friend
    new_friend.name = raw_input("Please add your friend's name: ")
    # regular pattern to check input
    pattern_n = '^[a-zA-Z\s]+s'

    new_friend.salutation= raw_input("What to call Mr. or Ms.?: ")
    # regular pattern to check input
    pattern_s = '^[a-zA-Z\s]+s'

    # concatination for full name
    new_friend.name = new_friend.salutation + " " + new_friend.name

    # ask for age of friend, int represents type casting in int
    new_friend.age = int(raw_input("Age? "))
    # regular pattern to check input
    pattern_a = '^[0-9]+$'

    #ask for rating of friend, float represents type casting in float
    new_friend.rating = float(raw_input("Spy rating? "))
    # regular pattern to check input
    pattern_r = '^[0-9]+\.[0-9]+$'

    # users input validations using if
    if len(new_friend.name) > 0 and new_friend.name.isdigit() == False and re.match(pattern_n,new_friend.name)!=None and re.match(pattern_s,new_friend.salutation)!=None and new_friend.age > 12 and new_friend.rating < 50 and re.match(pattern_a,new_friend.age)!=None and new_friend.salutation.isalpha() ==  True and new_friend.rating >= 0 and re.match(pattern_r,new_friend.rating)!=None:

        # add friend if conditions is true
        friends.append(new_friend)
        print (colored('Friend Added!', 'magenta'))
    else:
        #else display msg and re display menu
        print (colored('Sorry! Invalid entry. We can\'t add spy with the details you provided\n ', 'blue'))
    print (colored('The convention to follow is: \n ', 'blue'))
    print (colored('1. Name can be alphabets only.\n ', 'blue'))
    print (colored('2. Age can be digits only.\n ', 'blue'))
    print (colored('3. Do not use (.) after salutation, it can be alphabets only too.\n ', 'blue'))
    print (colored('Keep in mind and Try Again\n\n ', 'blue'))

    # returning total no of friends.
    return len(friends)