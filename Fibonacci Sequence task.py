n_1 = "1"
n_2 = "2"
print(f"{n_1}")
print(f"{n_2}")
keep_running = True
while keep_running == True:
    n_3 = n_1 + n_2
    print(f"{n_3}")
    n_1=n_2
    n_2=n_3

