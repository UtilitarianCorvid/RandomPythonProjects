import time
print("\n\n\n")
print("This is the username and password function")
time.sleep(.5)
loopvar = "Yes" 
while loopvar == "Yes":
    username = input("What's your username? ")
    time.sleep(1.5)
    password = input("What's your password? ")
    time.sleep(1.5)
    confirmusernametag = input("Confirm your username: (repeat the input) :")
    time.sleep(1.5)
    confirmpasswordtag = input("Confirm your password: (repeat the input) :")
    time.sleep(1.5)
    if confirmusernametag == username:
        if confirmpasswordtag == password:
            print("{} has been registered with the password of {}!".format(username, password))
    elif confirmusernametag != username and confirmpasswordtag != password:
        print("There was an error with confirming both of your inputs.\nCapitalization Counts!")
    elif confirmusernametag != username:
        print("There was an error with the confirmation of your username.\nCapitalization Counts!")
    elif confirmpasswordtag != password:
        print("There was an error with the confirmation of your password.\nCapitalization Counts!")
    else:
        print("This is a true error message. I ****ed up. Contact me.")
    loopvar = input("Do you want to repeat? (Yes/No)")
if loopvar != "Yes":
    print("\n\nShutting Down!\n\n")





