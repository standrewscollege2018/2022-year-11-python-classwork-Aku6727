''' Ask & Answer '''
while True:

    keep_asking= True
    while keep_asking==True:
        try:
            a = int(input("Enter a number: "))

            b = int(input("Enter a second number: "))
            keep_asking=False
        except ValueError:
            print("Not a valid number, please try again")


    print(f"You entered {a} and {b}")

    if a>b:
        print(f"the greater number is {a}")
    elif b>a:
        print(f"the greater number is {b}")
    else:
        print(f"Neither number is greater. They are both equal {a}={b}")

    print(f"the sum of the two number is: {a+b}")
