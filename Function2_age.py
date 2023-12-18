from datetime import datetime,timedelta
import math
def function2_user(Birthday, number_of_car):
    # Initialize customer and rental data
    customer_data = ''
    rented_car_data = ''
    existing_customers = []
    customer_names = []

    # Read customer data
    with open('Customers.txt', 'r') as file:
        for line in file:
            customer_details = line.strip().split(',')
            existing_customers.append(customer_details[0])
            customer_names.append(customer_details[1])
            customer_data += line

    # Read rented vehicles data
    with open('rentedVehicles.txt', 'r') as file1:
        rented_car_data = file1.read()

    # Check if the user is a returning customer
    if Birthday in existing_customers:
        customer_index = existing_customers.index(Birthday)
        print('Hello', customer_names[customer_index], '\nYou rented the car', number_of_car)
        rental_entry = f'{number_of_car},{Birthday},{datetime.now().strftime("%d/%m/%Y %H:%M")}'
        rented_car_data += rental_entry
    else:
        # Handle new customer registration
        print('You are a new customer, and we need to register some information about you.')
        first_name = input('Please enter your first name.\n')
        last_name = input('Please enter your last name.\n')
        email_addresses = input('Please enter your email addresses:\n')
        
        try:
            if '@' not in email_addresses or '.' not in email_addresses:
                raise ValueError("Invalid email format")
        
            new_customer_entry = f'{Birthday},{last_name},{first_name},{last_name}.{first_name}@{email_addresses}\n'
            customer_data += new_customer_entry
            rental_entry = f'{number_of_car},{Birthday},{datetime.now().strftime("%d/%m/%Y %H:%M")}'
            rented_car_data += rental_entry
        except ValueError as e:
            print(e)

        # Write the updated data back to the files
    with open('rentedVehicles.txt', 'w') as wri:
        wri.write(rented_car_data)

    with open('Customers.txt', 'w') as writ:
        writ.write(customer_data)
        
    file.close()
    file1.close()
    wri.close()
    writ.close()

# Determine whether the user's age in 2024 meets the car rental standards.            
def function2_age(Birthday, number_of_car):
    # Calculate the age of the user
    birth_date = datetime.strptime(Birthday, '%d/%m/%Y')
    current_year = datetime.strptime('2024', '%Y').year
    age = current_year - birth_date.year

    # Check if the age meets the criteria for renting a car
    if 18 <= age <= 100:
        # Proceed if the age is within the acceptable range
        function2_user(Birthday, number_of_car)
    elif age < 18:
        print('You are too young to rent a car')
    elif age > 100:
        print('You are too old to rent a car')