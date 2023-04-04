""" Rental Cars Task """

# Cars and details
cars = [
    "Suzuki Van",
    "Toyota Corolla",
    "Honda CRV",
    "Suzuki Swift",
    "Mitsubishi Airtek",
    "Nissan DC Ute",
    "Tayota Previa",
    "Toyota Hi Ace",
    "Toyota Hi Ace",
]
seat_number = ["2", "4", "4", "4", "4", "4", "7", "12", "12"]
status_of_availiability = [
    "Availiable",
    "Availiable",
    "Availiable",
    "Availiable",
    "Availiable",
    "Availiable",
    "Availiable",
    "Availiable",
    "Availiable",
]

keep_working = True
while keep_working == True:

    # Display th list of cars
    for i in range(len(cars)):
        print(
            f"{i+1:<5}. {cars[i]:<20}  Seats in the car: {seat_number[i]:<5}  {status_of_availiability[i]:<20}"
        )


    # Hire the car
    ask_for_a_car = True
    while ask_for_a_car == True:
        try:
            car_select = int(
                input(
                    "Please enter the number of the car you want to hire (0 to exit):  "
                )
            )
            if car_select == 0:
                break
            elif car_select > len(cars) or car_select < 0:
                print("That is not valid")
            else:
                print("Thank you")
                ask_for_a_car = False
        except ValueError:
            print("Enter an integer")


    if car_select != 0:
        # Get the last name and check it
        check_last_name = True
        while check_last_name == True:
            try:
                car_rent_last_name = input("What is your last name: ")

                if car_rent_last_name == "0":
                    break
                elif car_rent_last_name.isalpha():
                    check_last_name = False
                    # Change the car availiability
                    if status_of_availiability[car_select - 1] == "Unavailiable":
                        print("You cannot rent this car")
                    else:
                        status_of_availiability[car_select - 1] = "Unavailiable"
                        print("Ok")
                        print(f"You have selected {cars[car_select-1]}")

                    ask_for_a_car = False
                else:
                    print("Error")


            except:
                print("Error")


    # User has quit
    else:
        keep_working = False
        for i in range(len(cars)):
            print(
                f"{i+1:<5}. {cars[i]:<20}  Seats in the car: {seat_number[i]:<5}  {status_of_availiability[i]:<20}"
            )




