from datetime import datetime,timedelta
import math
# Function: Determine whether the car has been rented.
def function2_judge(number_of_car):
    # Open the file and read the list of leased cars
    with open('rentedVehicles.txt', 'r') as file:
        leased_cars = [line.strip().split(',')[0] for line in file.readlines()]
    with open('Vehicles.txt', 'r') as file1:
        all_cars = [line.strip().split(',')[0] for line in file1.readlines()]

    # Check if the specified car is in the list of leased cars
    if number_of_car in leased_cars:
        print('Sorry, the car is rented.')
    elif number_of_car not in leased_cars and number_of_car not in all_cars:
        print('Please check the number that you put. There is no', number_of_car,'car here.')
    elif number_of_car not in leased_cars and number_of_car in all_cars:
        print('The car is available now. The next step is to fill in your personal information.')
        return 1
    file.close()
    file1.close()
    