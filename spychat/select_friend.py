from globals import friends

def select_friend():
    count = 1
    for friend in friends:
        print str(count) + ". " + friend['salutation'] + " " + friend['name']
        count += 1

    user_input = int(raw_input("Choose the friend from the list : "))
    if user_input <= count:
        return user_input - 1
    else:
        print "Invalid choice. Try again"
        exit(-1)
