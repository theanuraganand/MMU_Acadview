from globals import status

# updated status message.
updated_status_message = None

def add_status(current):
    if current != None:
        print 'Current Message %s \n' % (current)
    else:
        print "No Current Msg \n"

    opt = raw_input("Choose from earlier status (y/n)? ")

    if opt.upper() == "N":
        new_message = raw_input("New Message:\n")

        # validations

        if len(new_message) > 0:
            status.append(new_message)
            new_status = new_message
            print 'Updated Status: %s' % (new_status)
        else:
            print "Null Input."
    elif opt.upper() == 'Y':
        count = 1

        # print all msg by loop
        for temp_msg in status:
            print '%d. %s' % (count, temp_msg)
            count = count + 1

        msg_opt = int(raw_input("\nEnter Choice !! \n"))

        # validate

        if len(status) >= 0:
            new_status = status[msg_opt - 1]
            print 'Updated Status: %s' % new_status
        else:
            print "Invalid Input "
    else:
        print 'Only Y/N'

    return new_status