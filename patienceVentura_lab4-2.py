# patience ventura 2025February06 patienceVentura_lab4-2.py
'''
This program lets the user enter a non-negative integer and then uses a 
loop to calculate & display the factorial of that number.
'''

# Initialize the variable to control the loop
another = '1'

# Use nested loops 
while another == '1':
    number = input('Enter a positive integer value : ')

    # Input validation: Input contains a letter or special character, excluding the negative sign
    if not number.isdigit() and number[0] != '-':
        print('ERROR: Non-integer input - press enter to try again')
        continue

    # Input validation: Input is a negative
    if int(number) < 0:
        print('ERROR: Negative number input - press enter to try again')
        continue

    # Initialize the factorial variable as 1 since factorial is the product of 
    # all positive integers of the number starting from 1
    factorial = 1

    # Calculate the factorial of the number
    for i in range(1, int(number)+1):
        # 0! = 1
        if int(number) == 0:
            print(f'The factorial of {number} is 1')
            break
        # Multiply the current value of the factorial by the current value of i
        factorial *= i

    # Display the factorial of the number
    print(f'The factorial of {number} is {factorial:,.0f}')

    # Ask user if they want to try another number
    another = input('Try another number? 1 = yes, press enter to end ')

    # Terminate the program if the user presses enter
    if another == '':
        print('Thank you for using our factorial program. Have a nice day!!')
        break
