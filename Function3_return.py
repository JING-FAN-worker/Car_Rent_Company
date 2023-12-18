from datetime import datetime,timedelta
import math
#Function 3: Return the car and delete the record in rentedVehicles.txt and enter the information in transActions.txt.
def function3_return():
    # Prompt user for the registration number of the car to return
    numberofcar = input('Give the register number of the car you want to return:\n')

    # Read data from rented vehicles and all vehicles files
    with open('rentedVehicles.txt', 'r') as file:
        rented_vehicles = [line.strip().split(',') for line in file.readlines()]

    with open('Vehicles.txt', 'r') as file1:
        vehicles = {line.split(',')[0]: line.split(',')[2] for line in file1.read().splitlines()}

    # Initialize variables
    rented_car_file = []
    transaction_entry = ''
    money = 0

    # Process the return of the rented car
    for vehicle in rented_vehicles:
        if numberofcar == vehicle[0]:
            # Calculate the rental cost
            rent_day = datetime.strptime(vehicle[2], '%d/%m/%Y %H:%S')
            diff = datetime.now() - rent_day
            money = int(vehicles[numberofcar]) * diff.days
            print(f'The rent lasted {diff.days} days and the cost is {money}.00 euros.')
        
            # Prepare transaction entry
            return_day = datetime.now().strftime('%d/%m/%Y %H:%S')
            transaction_entry = f'{numberofcar},{vehicle[1]},{vehicle[2]},{return_day},{diff.days},{money}.00\n'
        else:
            # Append non-returned cars to the updated list
            rented_car_file.append(','.join(vehicle))

    # Write the updated rented car data and transaction data to files
    with open('rentedVehicles.txt', 'w') as write_rent:
        write_rent.write('\n'.join(rented_car_file))

    with open('transActions.txt', 'a') as trans:
        trans.write(transaction_entry)
    
    file.close()
    file1.close()
    write_rent.close()
    trans.close()
