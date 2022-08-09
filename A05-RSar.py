# ------------------------------- #
# Title: Assignment05
# Dev: RSar
# Desc: Working with Dictionaries and Files
#       When the program starts, load each "row" of data in
#       "ToDoToDoList.txt" into a python Dictionary.
#       Add each dictionary "row" to a python list "table"
# ChangeLog: (when, who, what)
#               2022/08/08, RSar, Created File
# ------------------------------- #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
# strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary
# {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries
# rows (like Lab 5-2)

f = open(objFile, "r")  # open text file

print("\nWelcome to To Do List v1.0!"
      "\n\n\tOpened file: " + objFile)

objFileData = len(open(objFile).readlines())  # counts rows in file

if objFileData >= 1:  # if file has data

    print("\t" + str(objFileData) + " row(s) of data found.")

    for row in f:  # Add row from file to dictionary row
        lstData = row.split(",")
        dicRow = {"Task": lstData[0], "Priority": lstData[1].strip()}
        lstTable.append(dicRow)

else:  # if file does not have data
    print("\tNo data found.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("\n\t" + "="*40 +
          "\n\tMenu of Options" +
          "\n\t" + "=" * 40 +
          """
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
          """)
    strChoice = str(input("Which option would you like to perform? "
                          "[1 to 5]: "))

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':

        if len(lstTable) > 0:  # Display tasks

            print("\n\tDisplaying current data.")

            print("\n\t" + "-" * 40)
            print("\tTask | Priority")
            print("\t" + "-" * 40)

            for row in lstTable:
                print("\t" + row["Task"], row["Priority"], sep=" | ")

            print("\n\t/end of data")

        else:  # Alert user if there is no data collected
            print("\n\tNo data found.")

        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':

        while True:  # Continue to ask user for more data until they
            # return to the menu

            # Instruct user and collect user input

            print("\n\tEnter a Task and its Priority."
                  "\n\tEnter \"M\" at anytime to return to the Menu.")

            strTask = input("\nWhat is the task? ")
            if strTask.lower() == "m":
                break

            strPriority = input("What is the priority of task \'"
                                + strTask + "\' ? ")

            if strPriority.lower() == "m":
                break

            # Store data in a two-dimensional list, which each item
            # and price is a row of data
            # Add user input as new list in table

            dicRow = {"Task": strTask, "Priority": strPriority}
            lstTable.append(dicRow)

        continue

    # Step 5 - Remove an item from the list/Table
    elif strChoice.strip() == '3':

        while True:

            if len(lstTable) > 0:  # Display tasks

                print("\n\tDisplaying current data.")

                print("\n\t" + "-" * 40)
                print("\tTask | Priority")
                print("\t" + "-" * 40)

                for row in lstTable:
                    print("\t" + row["Task"], row["Priority"],
                          sep=" | ")

                print("\n\t/end of data")

                print("\n\tEnter the task you want removed."
                      "\n\tEnter \"M\" to return to the [M]enu.")

                r = input("\nWhat task do you want to remove? ")

                if r.lower() == "m":
                    break

                for row in range(len(lstTable)):  # Remove task
                    if lstTable[row]["Task"].lower() == r.lower():
                        del lstTable[row]
                        print("\n\tRemoved task \'" + r + "\'.")
                        break

            else:
                print("\n\tNo data found.")
                break

        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':

        if len(lstTable) > 0:  # Display user inputs to user
            f = open(objFile, "w")
            for row in lstTable:
                f.writelines(str(row["Task"]) + "," +
                             str(row["Priority"]) + "\n")
            f.close()
            print("\n\tData saved to: " + objFile)

        else:
            print("\n\tNo data found.")

        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("\n\tEnter \"Q\" to Quit"
              "\n\tPress ENTER key to return to the Menu.")
        c = input("\nAre you sure you want to quit? ")
        if c.lower() == "q":
            print("\n\tGoodbye!")
            input("\n[Press the ENTER key to quit.]")
            break  # and Exit the program
