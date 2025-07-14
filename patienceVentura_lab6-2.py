# patience ventura 22 February 2025 patienceVentura_lab6-2.py
'''
This program calculates the average of the numbers in the file and
should able to handle errors such as IOError and ValueError.
'''

# Global Constant
COUNT_NUM = 11

# Function purpose is to read the file and calculate the average of numbers
# in file while being able to handle IOError and ValueError
def main():
    try:
        with open('exceptionNumbers.txt', 'r') as infile:

            # Initialize accumulator to 0
            total = 0

            # Initialize a variable to keep count of numbers
            count = 0

            # Read every line from file and calculate total
            for line in infile:
                try: 
                    # Convert line to a float
                    number = float(line)

                    # Add 1 to the count variable
                    count += 1

                    # Add to total
                    total += number
                
                # Handle ValueError
                except ValueError:
                    print('\nA non-numeric character found in file - ignored')

            # Calculate the average
            ave = total/COUNT_NUM

            # Display the total and average of numbers
            print(f'\nNumbers in the file: 11')
            print(f'\nThe total is {total:.2f}')
            print(f'\nThe average of the numbers is {ave:.2f}\n')
      
    # Handle IOError
    except IOError:
        print('The file could not be found.\nProgram terminated.')


# Call the main function
if __name__ == '__main__':
    main()