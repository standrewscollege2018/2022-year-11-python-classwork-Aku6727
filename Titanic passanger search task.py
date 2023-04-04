'''Search for data on titanic passangers'''
#import the library
import sqlite3
#set a name for the database
DATABASE = 'Titanic_search_passanger.db'
#make a connection
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()
# start the loop
keep_running = True
while keep_running == True:
    #ask what the user wants to do
    ask_at_menu = True
    while ask_at_menu == True:
        try:
            menu_choice = int(input(" Welcome to the titanic database \n================================\n Menu \nOptions: \n 1. Search by name \n 2. Search by Class \n 3. Exit \n "))
            if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
                ask_at_menu = False
                print("Ok")
            else:
                print("Please enter a valid action")
        except ValueError:
            print("Please enter a number")

    #Execute option 1
    if menu_choice == 1:
        name_validity = True
        while name_validity == True:
            name = input("What is the name of the person? ")
            if name.isalpha():
                #Execute the querie
                name = "%" + name + "%"
                cursor.execute("SELECT passenger_id, name, class, survived FROM titanic where name Like ?",(name,))
                name_results = cursor.fetchall()
                #Print the results
                print(f"Results: \n======== \n{'ID':<4} {'Name':<70} {'Class':<10} {'Survival (1 for alive, 0 for dead)':<15}")
                for name_result in name_results:
                    print(f"{result[0]:4} {result[1]:70} {result[2]:<10} {result[3]:<15}")
                print("=========================================\n \n")
                name_validity = False

            else:
                print("Enter a valid name or part of a name")
    #Execute option 2
    elif menu_choice == 2:
        #Get and validate the class
        class_validity = True
        while class_validity == True:
            passenger_class=input("Enter a class (1-3 or 0 to quit): ")
            if passenger_class == 0:
                class_validity = False
                keep_running = False
            elif passenger_class.isnumeric():
                #Get the results
                cursor.execute("SELECT passenger_id, name, class, survived FROM Titanic where class = ?",(passenger_class,))
                class_results = cursor.fetchall()
                #Print the results
                print(f"Results: \n======== \n{'ID':<4} {'Name':<70} {'Class':<10} {'Survival (1 for alive, 0 for dead)':<15}")
                for class_result in class_results:
                    print(f"{class_result[0]:4} {class_result[1]:70} {class_result[2]:<10} {class_result[3]:<15}")
                class_validity = False
                print("=======================================\n \n")
            else:
                print("Enter a valid class")

    #Execute option 3 and exit
    elif menu_choice == 3:
        keep_running = False
    else:
        print("Please enter a valid action ")

'''Search for data on titanic passangers'''
#import the library
import sqlite3
#set a name for the database
DATABASE = 'Titanic_search_passanger.db'
#make a connection
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()
# start the loop
keep_running = True
while keep_running == True:
    #ask what the user wants to do
    ask_at_menu = True
    while ask_at_menu == True:
        try:
            menu_choice = int(input(" Welcome to the titanic database \n================================\n Menu \nOptions: \n 1. Search by name \n 2. Search by Class \n 3. Exit \n "))
            if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
                ask_at_menu = False
                print("Ok")
            else:
                print("Please enter a valid action")
        except ValueError:
            print("Please enter a number")

    #Execute option 1
    if menu_choice == 1:
        name_validity = True
        while name_validity == True:
            name = input("What is the name of the person? ")

            if name.isnumeric():
                print("Must enter some text")
            elif name.strip(" ") == "":
                print("Must enter something")
            else:
                #Execute the querie
                name = "%" + name + "%"
                cursor.execute("SELECT passenger_id, name, class, survived FROM titanic where name Like ?",(name,))
                name_results = cursor.fetchall()
                #Print the results
                print(f"Results: \n======== \n{'ID':<4} {'Name':<70} {'Class':<10} {'Survival (1 for alive, 0 for dead)':<15}")
                for name_result in name_results:
                    print(f"{result[0]:4} {result[1]:70} {result[2]:<10} {result[3]:<15}")
                print("=========================================\n \n")
                name_validity = False

    #Execute option 2
    elif menu_choice == 2:
        #Get and validate the class
        class_validity = True
        while class_validity == True:
            passenger_class=input("Enter a class (1-3 or 0 to quit): ")
            if passenger_class == 0:
                class_validity = False
                keep_running = False
            elif passenger_class.isnumeric():
                #Get the results
                cursor.execute("SELECT passenger_id, name, class, survived FROM titanic where class = ?",(passenger_class,))
                class_results = cursor.fetchall()
                #Print the results
                print(f"Results: \n======== \n{'ID':<4} {'Name':<70} {'Class':<10} {'Survival (1 for alive, 0 for dead)':<15}")
                for class_result in class_results:
                    print(f"{class_result[0]:4} {class_result[1]:70} {class_result[2]:<10} {class_result[3]:<15}")
                class_validity = False
                print("=======================================\n \n")
            else:
                print("Enter a valid class")

    #Execute option 3 and exit
    elif menu_choice == 3:
        keep_running = False
    else:
        print("Please enter a valid action ")

