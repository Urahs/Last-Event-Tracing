import os, time


# create save file if it is the first time user executes the app
try:
    a = [os.path.expanduser('~')][0][9:]
    os.makedirs("C:\\Users\\"+a+"\\Event Tracer\\")
    os.chdir("C:\\Users\\"+a+"\\Event Tracer\\")
    ofile = open("save.txt", "w")
    ofile.close()
    print("""
Hi! This is the first time you run this app.
This app is created to track the events like god damn uni classes, but
you can use for everything like go_gym, tidy_room, feed_yourself etc.

I didn't take care of all the bugs, so plz don't be a silly and use it properly

--- How to use ---
KEY 1:
    It displays the events you have added
KEY 2:
    Add event
KEY 3:
    Delete event
KEY 4:
    Update the last time of the event to the current local datetime
KEY 5:
    Exit from the world's most useful app!

You wont see this message everytime you open this app, dont worry :)
You can only see this message again just typing 'info' to the console...

Btw, if you want to support me and donate some bitcoin here is my public key :)
139nvyb364H9JMJC1Aywn31PopzSye2x4j
""")
except:
    None



def Time_Diff(x, current_time):
    # returns the difference of hours between time two datetimes
    event_last_time = eval("time.struct_time(" + x + ")")
    res = (time.mktime(current_time) - time.mktime(event_last_time)) // 3600
    day = int(res // 24)
    hour = int(res - day * 24)
    return_as_string = str(day) + "-" + str(hour)
    

    return return_as_string 


os.chdir("C:\\Users\\"+a+"\\Event Tracer\\")
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
        current_time = time.localtime()
        file = open("save.txt", "r")
        lines = file.readlines()
        file.close()
        if lines == []:
            print("\nYou don't have any event. Go create some...")
            key = "0"
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
                print("\t", end="")

                time_data = event[1].replace("\n", "")
                if(time_data != "null"):
                    last_time = Time_Diff(time_data, current_time).split("-")
                    if (last_time[0] == "0" and last_time[1] == "0"):
                        print("You have just taken care of that shit :)")
                    elif last_time[0] == "":
                        print(last_time[1] + " hours")
                    elif last_time[1] == "":
                        print(last_time[0] + " days")
                    else:
                        print(last_time[0] + " days " + last_time[1] + " hours")
                else:
                    print("null")
            print("-------------------------")
        key = "0"

    # ADD
    elif key == "2":

        file = open("save.txt", "r")
        content = file.read()
        file.close()


        add_event = input("Please enter a new event (without using space)\n>>> ")
        if " " in add_event:
            print("I said don't use this damn space blank, you silly!")
        else:
            if content == "":
                file = open("save.txt", "a")
                file.write(add_event + " null")
                file.close()
            else:
                file = open("save.txt", "a")
                file.write("\n" + add_event + " null")
                file.close()
        key = "0"

    # DELETE
    elif key == "3":
        delete_event = input("Please enter the name of event you wanna delete\n>>> ")

        file = open("save.txt", "r")
        lines = file.readlines()
        file.close()

        #I used counter in case user wants to delete the last event in the list (it cause an error, dont ask what)
        counter = 0
        file = open("save.txt", "w")
        for line in lines:
            if delete_event != line.split(" ")[0]:
                if counter == 0:
                    counter += 1
                else:
                    file.write("\n")
                event = line.replace("\n", "")
                file.write(event)
        file.close()
        key = "0"

    # EVENT
    elif key == "4":
        taken_event_name = input("Please select the event\n>>> ")
        current_time = time.localtime()
        
        file = open("save.txt", "r")
        lines = file.readlines()
        file.close()

        index = -1
        for i in range(len(lines)):
            event_name = lines[i].split(" ")[0]
            if event_name == taken_event_name:
                index = i
        
        if index == -1:
            print("Damn man! You should enter an currently exist event!")
        else:
            file = open("save.txt", "w")

            current_time_data = "("
            counter = 0
            for i in current_time:
                if counter == 1:
                    current_time_data += ","    
                else:
                    counter += 1
                current_time_data += str(i)
            current_time_data += ")"


            current_one = lines[index].replace("\n", "")
            current_one = current_one.split(" ")
            file.write(current_one[0] + " " + current_time_data)

            for i in range(len(lines)):
                if i == index:
                    continue

                file.write("\n")
                event = lines[i].replace("\n", "")
                file.write(event)


            file.close()

        # find that shit and update
        key = "0"

    # EXIT
    elif key == "5":
        print("\nby then...")
        time.sleep(0.5)
        exit()

    # SECRET ONE
    elif key == "6":
        print("\nThis app is made by Selim Sarialtin, you don't want to stole it...")
        key = "0"

    elif key == "info":
        print("""
This app is created to track the events like god damn uni classes, but
you can use for everything like go_gym, tidy_room, feed_yourself etc.
--- How to use ---
KEY 1:
    It displays the events you have added
KEY 2:
    Add event
KEY 3:
    Delete event
KEY 4:
    Update the last time of the event to the current local datetime
KEY 5:
    Exit from the world's most useful app!

Donation key (bitcoin):
139nvyb364H9JMJC1Aywn31PopzSye2x4j

I assumed that you are a smart person so that i didn't take care of all the bugs,
Please don't be a silly and use it properly...
""")
        key = "0"



"""
pino (2022,2,25,15,10,26,1,53,0)
isp null
"""