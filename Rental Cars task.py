''' Rental Cars Task '''

# Cars and details
cars = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtek", "Nissan DC Ute", "Tayota Previa", "Toyota Hi Ace", "Toyota Hi Ace"]
seat_number = ["2", "4", "4", "4", "4", "4", "7", "12", "12"]
status_of_availiability = ["Availiable", "Availiable", "Availiable", "Availiable", "Availiable", "Availiable", "Availiable", "Availiable", "Availiable"]

keep_working = True
while keep_working == True:

    for i in range(len(cars)):
        print(f"{i+1:<5}. {cars[i]:<20}  Seats in the car: {seat_number[i]:<5}  {status_of_availiability[i]:<20}")

    keep_asking = True
    while keep_asking == True:
        try:
            car_rent_name = input("What is your name (type EXIT to exit):  ")



        except ValueError:
            print(f"{car_rent_name} is not valid. Please try again")

        if car_rent_name == "EXIT":
            for i in range(len(cars)):
                print(f"{i+1:<5}. {cars[i]:<20}  Seats in the car: {seat_number[i]:<5}  {status_of_availiability[i]:<20}")
                print("Ok, please restart to continue")
        else:
            print(f"Would you like to rent a car {car_rent_name}")
            input("Yes/No:  ")











