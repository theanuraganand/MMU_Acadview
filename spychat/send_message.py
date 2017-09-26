# importing existing friend, steganography library, and datetime.
from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import friends, ChatMessage

#importing regular expression for proper validation
import re

# importing termcolor for colorful output.
from termcolor import colored

# function to send a secret message.
def send_message():

    # choose a friend from the list to communicate
    friend_choice = select_friend()

    # select an image in which you want to hide a secret message.
    original_image = raw_input("Provide the name of the image to hide the message : ")
    pattern_i = '^[a-zA-Z]+\.jpg$'
    # User validation for image files.
    if(re.match(pattern_i,original_image)!=None):
        print # Do Nothing here
    else:
        # Provide suggestions to user
        print colored("Please provide (.jpg) image type.","red")

    # name the output file
    output_image = raw_input("Provide the name of the output image  : ")
    pattern_o = '^[a-zA-Z]+\.jpg$'
    # User validation for image files.
    if (re.match(pattern_o,output_image) != None):
        print # Do Nothing here
    else:
        # Provide suggestion to user.
        print colored("We can extract in only (.jpg) image type, please go for (.jpg).","red")

    # write the secret message
    text = raw_input("Enter your message here : ")
    # Encrypt the message using Steganography library
    Steganography.encode(original_image, output_image, text)

    # the message will be stored in chat message class
    new_chat = ChatMessage(text, True)

    # along the name of friend with whom we add message
    friends[friend_choice].chats.append(new_chat)

    # Successful message after encoding
    print (colored("Your message encrypted successfully.", 'red'))

    # name of the friend along which we add message.
    friends[friend_choice].chats.append(new_chat)
    print (colored("your secret message is ready.",'yellow'))