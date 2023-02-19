''' Fizz Buzz '''

keep_asking = True
while keep_asking == True:
    try:
    # get the max number
        max=int(input("enter a whole number please: "))
        keep_asking = False

    except ValueError:
        #if the number is not valid, keep asking)
        print("Not and integer, please try again")

# count and display the numbers
for i in range( 1, max+1):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else: print(i)

print("all done!")


