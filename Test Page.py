Operation=str(input("would you like to +,-,*,/ or any power (**):  "))

numb_1=int(input("Give me the first Number. : "))

numb_2=int(input("Give me the second Number. "))





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


