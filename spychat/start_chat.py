from add_status import add_status
from add_friend import add_friend
from select_friend import select_friend

# meathod to start chat
def start_chat(name, age, rating, status):
    if not (age > 12 and age < 50):
        # invalid age.
        error_message = "Invalid age."
        print error_message
    else:
        msg = "Authentication complete. Welcome\n Name : " + name + "\nAge: " + str(
            age) + "\nRating: " + str(rating) + "\nGlad to have you back"
        print msg
        choice = 1
        while not (choice == 6):
            menu = "What do you want to do? \n " \
                        "1. Add a status update \n " \
                        "2. Add a friend \n " \
                        "3. Send a secret message \n " \
                        "4. Read a secret message \n " \
                        "5. Read Chats from a user \n " \
                        "6. Close Application \n"
            choice = int(raw_input(menu))

            # validate users input
            if (choice == 1):
                current_msg = None
                current_msg = add_status(current_msg)
            elif (choice == 2):
                no_of_friends = add_friend()
                print 'You have %d friends' % (no_of_friends)
            elif (choice == 3):
                print select_friend()
            elif (choice == 6):
                print "Bye"
            else:
                print "Invalid choice"