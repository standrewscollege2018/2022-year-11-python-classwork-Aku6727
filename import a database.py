'''import a database'''
#import the library
import sqlite3
#set a name for the database
DATABASE = 'Cars.db'
#make a connection
connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()

cursor.execute("SELECT car_id, car_plate FROM cars")
result = cursor.fetchall()



for car in result:
    print(f"{car[0]:<3} {car[1]}")

