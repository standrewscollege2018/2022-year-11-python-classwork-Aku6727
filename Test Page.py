"""Search for data on titanic passangers"""
# import the library
import sqlite3

# set a name for the database
DATABASE = "Titanic_search_passanger.db"
# make a connection
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()
# start the loop
keep_running = True
while keep_running == True:
    # ask what the user wants to do

    menu_choice = input(
        " Welcome to the titanic database \n================================\n Menu \n 1. Search by name \n 2. Search by Class \n 3. Exit (Press 0)  \n-------------------------------\nPlease enter either a letter with which \nwe can search for a passenger or their class \n"
    )

    if menu_choice == "1" or menu_choice == "2" or menu_choice == "3":
        int(menu_choice)

    # If they want to quit
    elif menu_choice == "0":
        keep_running = False
    else:
        print(f"You have entered the name {menu_choice}")
    if menu_choice.isalpha():
        name = "%" + menu_choice + "%"
        cursor.execute(
            "SELECT passenger_id, name, class, survived FROM titanic where name Like ?",
            (name,),
        )
        name_results = cursor.fetchall()
        # Print the results
        print(
            f"Results: \n======== \n{'ID':<4} {'Name':<70} {'Class':<10} {'Survival (1 for alive, 0 for dead)':<15}"
        )
        for name_result in name_results:
            print(
                f"{name_result[0]:4} {name_result[1]:70} {name_result[2]:<10} {name_result[3]:<15}"
            )
            name_validity = False
    # If they enter a number we assume they are trying to search by class
    elif menu_choice.isnumerical():
        # Get the results

        cursor.execute(
            "SELECT passenger_id, name, class, survived FROM titanic where class = ?",
            (menu_choice,),
        )
        class_results = cursor.fetchall()
        # Print the results
        print(
            f"Results: \n======== \n{'ID':<4} {'Name':<70} {'Class':<10} {'Survival (1 for alive, 0 for dead)':<15}"
        )
        for class_result in class_results:
            print(
                f"{class_result[0]:4} {class_result[1]:70} {class_result[2]:<10} {class_result[3]:<15}"
            )
    # If the user eneters an unexpected response
    else:
        print("Please enter a valid letter or a valid class")
