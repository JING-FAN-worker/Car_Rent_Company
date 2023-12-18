from datetime import datetime,timedelta
import math
# Display all available rental cars.
def function1(file_name1,file_name2):
    # Open and read the file containing the list of all cars
    with open(file_name1, 'r') as carfile:
        car_wait = [line.strip().split(',', 3) for line in carfile.readlines()]

    # Open and read the file containing the list of rented cars
    with open(file_name2, 'r') as rentfile:
        rented_cars = [line.strip().split(',', 3)[0] for line in rentfile.readlines()]

    print('The following cars are available:')

    # Create a list of cars that are not currently rented
    available_cars = [car for car in car_wait if car[0] not in rented_cars]

    # Print the details of each available car
    for car in available_cars:
        print('* Reg. nr: ', car[0], ', Model: ', car[1], ', Price per day: ', car[2], '\nProperties: ', car[3].replace(',', ', '), sep='')
    
    carfile.close()
    rentfile.close()
