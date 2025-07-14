# patience ventura 22 February 2025 patienceVentura_lab6-3.py
'''
This program accepts input and calls a function to test if input is a number and
displays a message regarding the result of that numeric test.
'''

# Main Function which calls the numTest function
def main():
    print('\nThis program will test for numeric input.')

    # Get input from user
    number = input('Please enter your test data, OR press ENTER to stop program: ')

    try:
        while number != '':

            # Call  numTest() and display if number or not
            if numTest(number):
                print(f'\n{number} IS a number')
            else:
                print(f'{number} IS NOT a number')

            number = input('Please enter your test data, OR press ENTER to stop program: ')

    except:
        print('An error occurred.')

# Function purpose is to return True or False, depending on whether
# making the number float will be successful or result to an error
def numTest(num):
    try:
        # Convert to float, if successful, returns true
        num = float(num)
        status = True
    except:
        status = False
    return status


# Call the main function
if __name__ == '__main__':
    main()