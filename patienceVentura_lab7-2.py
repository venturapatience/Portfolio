# patience ventura 27 February 2025 patienceVentura_lab7-2.py
'''
This program displays 2 lists composing of prime and composite with all of the integers 
from 2 up and including the value entered.
'''

# The main function creates a loop to ask a number from user and then
# display the primes and number using other functions
def main():
    another = '1'

    while another == '1':
        
        # Get input from user
        number = int(input('\nEnter an integer greater than 1: '))

        # Input validation since the number should be 25 and above
        while number <= 25:
            print("ERROR: Input should be greater than 1")
            number = int(input('Enter an integer greater than 1: '))

        print(f"\nFor numbers ranging from 2 to {number}")
        
        primes, composites = primes_and_composites(number)

        # Display the primes and composites using displayNumbers()
        print(f"\nThese are the prime numbers:\n")
        displayNumbers(primes)

        print(f"\nThese are the composite numbers: \n")
        displayNumbers(composites)

        # Ask for another input
        another = input('\nTest more numbers? 1 = yes OR press enter to end program: ')

# The primes_and_composite function creates two separate lists of primes and
# composites depending on the value returned by the isPrime function
def primes_and_composites(number_input):

    # Create two empty lists
    primes = []
    composites = []

    # Create loop from number 2 to user input
    for num in range(2, number_input+1):
        if isPrime(num):
            primes.append(num)
        else:
            composites.append(num)

    return primes, composites
    
# The isPrime function checks if each the number is a prime 
# or composite using a loop
def isPrime(num):

    # if the number is 2, it returns True since 2 is the only 
    # even number that is prime
    if num == 2:
        return True
    
    # Loop from 2 to n-1
    for i in range(2, num):
        # When dividing a number by another number and the remainder is 0,
        # that means the number has factors aside from 1 and itself (composite!)
        if num % i == 0:
            return False
        
    return True

# The displayNumbers function prints the list so that there are 
# only 5 numbers each line
def displayNumbers(list):
    for i in range(len(list)):
        print(f"{list[i]}", end=" ")
        # Print 5 numbers per line
        if (i+1) % 5 == 0:
            print("")
    print()
        

# Call the main function
if __name__ == '__main__':
    main()
