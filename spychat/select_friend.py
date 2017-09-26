# importing older friend if exist
from spy_details import friends

#from globals import friends

# importing termcolor for colorful output
from termcolor import colored

# function to select friend from friend list.
def select_friend():

    # indexing position of friend.
    counter = 1

    # to select a friend with indexing
    for friend in friends:
        print str(counter) + ". " + friend.name + "Age : " + str(friend.age)

        counter = counter + 1

    # ask user which friend he wants to select to chat with
    friend_choice = int(raw_input(colored("\nSelect from the list : ", 'magenta')))
    #  selected friend to perform action
    friend_chosen = int(friend_choice) - 1

    # Check if user has out of index choice.
    if friend_chosen + 1> len(friends):
        print (colored("Sorry, this friend is not present.", "green"))
        exit()
    else:
        # returns the selected friend to perform actions
        return friend_chosen