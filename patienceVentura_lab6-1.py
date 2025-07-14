# patience ventura 22 February 2025 patienceVentura_lab6-1.py
'''
This program writes a series of random numbers to a file
and displays information about the numbers.
'''

# Import random module to get random numbers
import random


# Function purpose is to create a loop of creating and reading a file to 
# get random numbers and calculate the total, average, maximum, and minimum
# using other functions
def main():
    again = '1'

    try:
        while again == '1':
            # Get input from user
            input_count = int(input('\nHow many numbers do you want? '))
            createFile(input_count)
            results = readFile(input_count)
            displayResults(input_count, results)
        
            again = input('Run program again? 1 = yes OR press ENTER to stop: ')

    # Handle ValueError when user inputs anything other than a number
    except ValueError:
        print('ERROR: Input should be a valid integer, above 0.')
          
# Function purpose is to write data (random numbers)
# on a file called "myRandomNums.txt"
def createFile(input):

    with open('myRandomNums.txt', 'w') as randNumFile:

        print('\nRandom numbers generated...\n')

        for count in range(1, int(input)+1):
            randomNum = int(random.randint(1, 500))
            randNumFile.write(f'{randomNum}\n')
            count+= 1


# Function purpose is to read data from the created file and calculate 
# the total, average, maximum, and minimum of the set of numbers
def readFile(input):

    try:  
        with open('myRandomNums.txt', 'r') as randNum_file:

            totalRandNum = 0 # initialize accumulator

            count = 0 # initialize a variable to keep count of random numbers

            max = 0 # set to 0 since this is lower than the range of numbers to get max
            min = 501 # set to 501 since this is higher than the range of numbers to get min

            for line in randNum_file:
                randNum = int(line)
                count += 1
                print(randNum, end=" ")

                # Print 6 numbers per line
                if count % 6 == 0:
                    print("")

                # Calculate total
                totalRandNum += randNum

                # Determine the maximum and minimum numbers
                if randNum > max:
                    max = randNum
                if randNum < min:
                    min = randNum

            # Calculate the average
            ave = totalRandNum/input

            return totalRandNum, ave, max, min
    
    except FileNotFoundError:
        print('The file does not exist.')

# Function purpose is to display the results of the previous calculations
def displayResults(input, results):
    totalRandNum, ave, max, min = results
    print(f'\n\nThe total of the random numbers is: {totalRandNum}')
    print(f'The count of the numbers is: {input}')
    print(f'The average is: {ave:.2f}')
    print(f'The maximum number is: {max}')
    print(f'The minimum number is: {min}\n')

# Call the main function
if __name__ == '__main__':
    main()