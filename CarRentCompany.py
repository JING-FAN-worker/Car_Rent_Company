from datetime import datetime,timedelta
import math
import Function1
import Function2_age
import Function2_form
import Function2_judge
import Function3_return
import Function4sum_money
while True:
    # User's selection from the menu
    user_choice = int(input(
        'You may select one of the following:\n'
        '1) List available cars\n'
        '2) Rent a car\n'
        '3) Return a car\n'
        '4) Count the money\n'
        '0) Exit\n'
        'What is your selection?\n'
    ))

    # Processing based on user's choice
    if user_choice == 1:
        # List available cars
        Function1.function1('Vehicles.txt', 'rentedVehicles.txt')  

    elif user_choice == 2:
        while True:
            number_of_car = input('Give the register number of the car you want to rent:\n')
            # Check if the car is already rented
            result = Function2_judge.function2_judge(number_of_car)  
            if result == 1:
                break;
        # Validate birth date format
        Birthday = Function2_form.function2_form()  
        # Check age criteria for car rental
        Function2_age.function2_age(Birthday, number_of_car)  

    elif user_choice == 3:
        # Return a car and update records
        Function3_return.function3_return()  

    elif user_choice == 4:
        # Calculate and display total revenue
        Function4sum_money.function4sum_money()  

    elif user_choice == 0:
        # Exit the loop and end the program
        print('Looking forward to your next visit!')
        break  



