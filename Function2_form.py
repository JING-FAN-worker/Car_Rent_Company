from datetime import datetime,timedelta
import math
# Function 2: Determine whether the entered date of birth format is correct.
def function2_form():
    while True:
        # Prompt user for their birthday
        birthday = input('Please enter your birthday in the form DD/MM/YYYY:\n')
        try:
            # Validate the format and length of the birthday
            datetime.strptime(birthday, '%d/%m/%Y')
            if len(birthday) != 10:
                raise ValueError("Incorrect length")

            # If validation is successful, return the birthday
            return birthday
        except ValueError:
            # Inform the user of the incorrect input and prompt again
            print('Your input is wrong, please check the form and the number.')
