import os


# create save file if it is the first time user executes the app
try:
    a = [os.path.expanduser('~')][0][9:]
    os.makedirs("C:\\Users\\"+a+"\\Last Event Save File\\")
    os.chdir("C:\\Users\\"+a+"\\Last Event Save File\\")
    ofile = open("save.txt", "w")
    ofile.close()
except:
    None


"""
1 - Display
2 - Add
3 - Delete
4 - Event
5 - Exit
"""


key = 0
while True:
    if key == 0:
        # print main menu
        key = input("What do u want to do my friend?\n>>> ")
    
    elif key == 1:
        # open txt read all shit then print
        key = 0
    elif key == 2:
        add_event = input("Please enter a new event\n>>> ")
        # open txt file with append, then enter add new event like this (event_name 1000 24:00)
        key = 0
    elif key == 3:
        delete_event = input("Please enter the name of event you wanna delete\n>>> ")
        #open txt read all shit, find that then delete it. Finally write all shit again
        key = 0
    elif key == 4:
        # read and print all shit
        event = input("Please select the event\n>>> ")
        # find that shit and update
        key = 0
    elif key == 5:
        exit()
    elif key == 6:
        print("This app is made by Selim Sarialtin, you don't want to stole it...")
