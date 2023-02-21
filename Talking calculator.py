''' Making a Virtual Assistant'''
while True:
    keep_asking=True

    while keep_asking==True:
        try:
            answer1=str(input("Can I help you with calculating something? Please answer yes or no:   "))

            if answer1=="yes":
                ask_again=True

                while ask_again==True:
                    try:
                        Operation=str(input("would you like to +,-,*,/ or any power (**):  "))

                        numb_1=int(input("Give me the first Number or the Base number: "))

                        numb_2=int(input("Give me the second Number or the exponent: "))





                        if Operation=="+":
                            print(f"Ok. {numb_1}+{numb_2}={numb_1+numb_2}")
                        elif Operation=="-":
                            print(f"Ok. {numb_1}-{numb_2}={numb_1-numb_2}")
                        elif Operation=="*":
                            print(f"Ok. {numb_1}*{numb_2}={numb_1*numb_2}")
                        elif Operation=="/":
                            print(f"Ok. {numb_1}/{numb_2}={numb_1/numb_2}")
                        elif Operation[0:2]=="**":
                            print(f"Ok.{numb_1}**{numb_2}={numb_1**numb_2}")
                        else:
                            print(f"{Operation} is not a valid response. Please enter a different response")

                        ask_again=False

                    except ValueError:
                        print(f"I didn't understand that, please answer again.")


            elif answer1=="no":
                print("Ok, I will go back to sleep.")

            else:
                print("Sorry I didnt understand that. Please try Again.")

            keep_asking=False



        except ValueError:
            print("I didn't understand {answer1}, please answer again.")
