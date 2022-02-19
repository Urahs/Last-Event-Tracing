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



key = "0"
while True:
    if key == "0":
        print("""
1 - Display
2 - Add
3 - Delete
4 - Event
5 - Exit
""")
        key = input("What do u want to do my friend?\n>>> ")
    
    # DISPLAY
    if key == "1":
        os.chdir("C:\\Users\\"+a+"\\Last Event Save File\\")
        file = open("save.txt", "r")
        lines = file.readlines()
        if lines == []:
            print("You don't have any event. Go create some...")
            continue
        else:


            # find the max length of string
            max_length = 0
            for i in lines:
                temp_len = len(i.split(" ")[0])
                if temp_len > max_length:
                    max_length = temp_len
            print("\n------ Your Events ------")
            for entity in lines:
    
                event = entity.split(" ")
                event_name = event[0]
                #print event name1

                print(event_name, end="")
                for i in range(0, max_length - len(event_name)):
                    print(" ", end="")
                
                
                #print last time
                #https://www.geeksforgeeks.org/python-program-to-find-number-of-days-between-two-given-dates/#:~:text=Using%20Python%20datetime%20module%3A,days%20between%20the%20two%20dates.
                

                print()
            print("-------------------------")
        key = "0"

    # ADD
    elif key == "2":
        add_event = input("Please enter a new event\n>>> ")
        # open txt file with append, then enter add new event like this (event_name 1000 24:00)
        key = "0"

    # DELETE
    elif key == "3":
        delete_event = input("Please enter the name of event you wanna delete\n>>> ")
        #open txt read all shit, find that then delete it. Finally write all shit again
        key = "0"

    # EVENT
    elif key == "4":
        # read and print all shit
        event = input("Please select the event\n>>> ")
        # find that shit and update
        key = "0"

    # EXIT
    elif key == "5":
        exit()

    # SECRET ONE
    elif key == "6":
        print("This app is made by Selim Sarialtin, you don't want to stole it...")
