''' Barcode task '''


#ask for a code
keep_asking = True
while keep_asking== True:
    try:
        barcode=str(input("Please enter a barcode: "))


        if len(barcode)==13:
            print("correct number of digits")

            int(barcode)

            keep_asking=False

        else:
            print("Error: Wrong number or digits")




    except ValueError:
        print(f"{barcode} is not a valid barcode, please try again")

country_code= barcode[0:2]
manufacturer_code= barcode[2:7]
product_code= barcode[7:12]
check_digit= barcode[12]
print(f"The country code is: {country_code}")
print(f"The manufacturer code is: {manufacturer_code}")
print(f"The product code is: {product_code}")
print(f"The check digit is: {check_digit}")
