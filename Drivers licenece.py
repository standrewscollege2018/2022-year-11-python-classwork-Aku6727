''' Drivers Licence '''

names = ["Fraser", "Josh  ", "Cayden", "Sean  "]

stat_of_lic= ["No Licence", "Learners", "Restricted", "Full"]

while True:


    for i in range(len(names)):
        print(f"{i+1}.  {names[i]}       {stat_of_lic[i]}")


    status_change_name = int(input("Whos status would you like to change (1-4) "))
    print(f"You have selected {names [status_change_name-1]}")
    status_change_lic = input(f"What would you like {names[status_change_name -1]} new status to be  ")

    print(f" NAME: {names[status_change_name-1]} NEW STATUS: {status_change_lic}")

    if status_change_lic == str
        stat_of_lic[status_change_name-1]=status_change_lic

    else:
        print(f"{status_change_lic} is not a valid licence status, please start again")


    for i in range(len(names)):
        print(f"{i+1}.  {names[i]}       {stat_of_lic[i]}")

    print("Finished______________________________")




