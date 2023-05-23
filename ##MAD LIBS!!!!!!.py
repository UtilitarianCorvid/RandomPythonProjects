####MAD LIBS!!!!!!
###To Do: 
#make at least 2/3 templates tonight at home from a mad lib of mine
#make themes?
import time

##Seperator function
print("\n\n\n\n\n\n")

print("This is Mad Libs!")
###Choose which template to use - START
templatechoice = input("Choose an integer between 1 and 10! #Pls just use 1 for now#")

##START verifies the templatechoice is a valid number
templatechoicelist = ["1","2","3","4","5","6","7","8","9","10"] 
numbertemplateverify = templatechoicelist.count("{}".format(templatechoice))
#this function helps debug: print("{}".format(numbertemplateverify))
if numbertemplateverify == 1:
    templatename = "The End of the world!"
    print("You have chosen: {}".format(templatename))
else:
    ##Seperator function
    print("\n\n") 
    #End seperator function
    print("Template selection failed.\n\nPlease restart and choose an integer between 1 and 10")

##END verifies the templatechoice is a valid number

### Choose which template to use - END


#Ask for word inputs
if numbertemplateverify == 1:
    adjective1 = input("Print a adjective:")
    famousperson1 = input("Print a famous person:")
    verb1 = input("Print a verb:")
    country1 = input("Print a country:")
    emotion1 = input("Print an emotion:")
    place1 = input("Print a non-country place:")
    pluralnoun1 = input("Print a plural noun:")
    adjective2 = input("Print another adjective:")
    pluralnoun2 = input("Print another plural noun:")
    lengthoftime1 = input("Please input a length of time:")
    adjective3 = input("Print a third adjective:")
    pluralfood1 = input("Print a plural food:")
    drink1 = input("Please input a liquid:")
    noun1 = input("Please input a noun:")
    pluralnoun3 = input("Please print a third plural noun:")
    sound1 = input("Please print a sound:")
    sound2 = input("Please print another sound:")
    print("\n\n") 
    print("After a(n){} presedential election, the American people have elected {} to the office of the President of the United States.\nTheir first executive order: {} all of the nation's nuclear weapons.\nUnfortunately, {} saw this as an act of {} and deployed their military to {}.".format(adjective1, famousperson1, verb1, country1, emotion1, place1))
    print("The stock market crashed.")
    print("People went without {} for {}.".format(pluralnoun1, lengthoftime1))
    print("Some left their homes and took to the road, only to end up {} on the highway...others hid in underground {}.".format(adjective2, pluralnoun2))
    print("Where there had once been the sound of sirens and jets soaring overhead, there was now a(n) {} silence.".format(adjective3))
    print("{} and {} were scarce.".format(pluralfood1,drink1))
    print("Those who had survived would go days on end without seeing another {}, with only their {} to keep them company.".format(noun1,pluralnoun3))
    print("Perhaps they were reminded of an old poem: \n'This is the way the world ends. Not with a(n) {} but a(n) {}'".format(sound1,sound2))
#Print whole function
##Seperator function
time.sleep(5)
print("\n\n\n")
##Storage
