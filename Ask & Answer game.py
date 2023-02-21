''' Ask & Answer '''
while True:

    keep_asking= True
    while keep_asking==True:
        try:
            numb_a = int(input("Enter a number: "))

            numb_b = int(input("Enter a second number: "))

            oper= str(input("Multiplication, Division, Minus, Plus, Squared or Square root of?")

            keep_asking=False
        except ValueError:
            print("Not a valid number, please try again")


    print(f"You entered {a} and {b}")


