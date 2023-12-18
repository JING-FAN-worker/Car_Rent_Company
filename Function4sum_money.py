from datetime import datetime,timedelta
import math
# Function 4 calculates total income.
def function4sum_money():
    # Define the name of the file containing transaction data
    transactions_file = 'transActions.txt'

    # Open the file and read transaction data
    with open(transactions_file, 'r') as file:
        transactions = [line.strip().split(',') for line in file.readlines()]

    # Calculate the total revenue from the transactions
    total_revenue = sum(float(transaction[5]) for transaction in transactions)

    # Round the total revenue to the nearest whole number and print it
    print('The total amount of money is ', round(total_revenue), '.00 euros', sep='')
    
    file.close()