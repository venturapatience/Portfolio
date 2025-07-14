# patience ventura 5 March 2025 Patience_Ventura_Project.py
'''
This  program generates a bill for sending a telegram 
and translates the message into Morse code.
'''

# MORSE CODE PROJECT

# Global Constants
BLOCK = 5
COST_OF_BLOCK = 1.50
SINGLE_WORD = 0.50

# Function Definitions

# The purpose of the main function is to control the flow of the program
# and call other functions as needed
def main():
    try:
        # Flag to control the main program loop
        flag = True

        while flag:
            # Call the function to display the menu
            displayMenu()
            
            # Get user input for menu choice
            choice = int(input('\nInput menu choice: '))

            # Input validation for menu choice (outside the integer range of 1 to 4)
            while choice < 1 or choice > 4:
                print('ERROR: Invalid choice. Please try again.\n')
                # Display the menu again and get input
                displayMenu()
                choice = int(input('\nInput menu choice'))

            # Menu choice 1: Process Telegram Bill
            if choice == 1:

                # Get user input for message and translate to small letters
                input_msg = input('\nEnter message to be sent:\n').lower()

                # Call the function to translate the message
                count, translated_msg = translateMessage(input_msg)

                # Get sender information
                firstName_lastName = input('\nInput sender first and last name ')
                street_address = input('Input sender street address ')
                city_state = input('Input sender city, state (comma separated) ')
                zipCode = input('Input sender zip code ')

                # Reprint sender information and message
                print('\nSender Information\n')
                print(f'{firstName_lastName}')
                print(f'{street_address}')
                print(f'{city_state} {zipCode}')

                # Display the message in morse code
                print('\nThis message')
                print(f'{input_msg}\n')
                print('translates to the following Morse Code\n')

                # Print 5 words per line
                word_count = 0
                for i in range(len(translated_msg)):
                    print(f"{translated_msg[i]}", end = "")

                    if translated_msg[i] == ' ':
                        word_count += 1

                    if word_count == 5:
                        print()
                        word_count = 0

                # Calculate the cost of sending the message by calling calcCost function
                print(f'\nIt will cost {calcCost(count):.2f} to send')

            # Menu choice 2: Translate message to Morse Code
            elif choice == 2:

                # Get user input for message and translate to small letters
                input_msg = input('\nEnter a message: ').lower()
                count, translated_msg = translateMessage(input_msg)

                # Display message into morse code
                print(f'Translation: ')
                word_count = 0
                for i in range(len(translated_msg)):
                    print(f"{translated_msg[i]}", end = "")

                    if translated_msg[i] == ' ':
                        word_count += 1

                    if word_count == 5:
                        print()
                        word_count = 0

            # Menu choice 3: Process Data File
            elif choice == 3:
                processDataFile() # Call the function

            # Menu choice 4: End the program
            elif choice == 4:
                print('\nThank you for using our program.')
                flag = False

    # Handle the ValueError exception (if user inputs a non-integer)    
    except ValueError:
        print('ERROR: Input menu choice must be a valid number from 1 to 4. Please try again.\n')
            
# The purpose of the function is to display the menu options
def displayMenu():
    print('\nWelcome to Western Union Telegraph Company\n')
    print('1. Process Telegram Bill')
    print('2. Translate to Morse Code')
    print('3. Process Data File')
    print('4. End Program')

# The purpose of the function is to calculate and return the amount owed
# based on the number of words as arguments
def calcCost(count_words):

    # Get the integer part of the quotient
    num_of_blocks = count_words//BLOCK

    # Get number of words in excess of 5 words
    remaining_words = count_words%BLOCK

    # Calculate the cost of sending the message
    blockCost = num_of_blocks*COST_OF_BLOCK
    singleWordCost = remaining_words*SINGLE_WORD

    # Get the total cost and return it
    totalCost = blockCost + singleWordCost

    return totalCost

# The purpose of the function is to accept a letter input and 
# return the corresponding Morse code translation
def translateLetter(letter):

    # Use a tuple to store the alphabet and Morse code to make them immutable
    alphabet = ('a', 'b', 'c', 'd', 'e', 
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 
                'z')
    morse_code = ('.-', '-...', '-.-.', '-..', '.',
                  '..-.', '--.', '....', '..', '.---',
                  '-.-', '.-..', '--', '-.', '---',
                  '.--.', '--.-', '.-.', '...', '-',
                  '..-', '...-', '.--', '-..-', '-.--',
                  '--..')

    # Check if the letter is in the alphabet
    if letter in alphabet:
        # Get the index of the letter in the alphabet
        letter_index = alphabet.index(letter)
        # Return the Morse code translation
        return morse_code[letter_index]
    
    # Check if the letter is not in the alphabet and return the character
    # to be reprinted as part of the translation
    elif letter not in alphabet:
        return letter
    
    else:
        return ""

# The purpose of the function is to accept an input that is to be
# translated into full Morse code translation
def translateMessage(input_msg):

    # Count the number of words in the message by checking if there is a space
    count_words = 1
    for letter in input_msg:
        if letter == ' ':
            count_words += 1

    morse_translation = []

    # Translate each letter (ch for character) in the message and append to a list
    for ch in input_msg:
        morse_translation.append(translateLetter(ch))

    return count_words, morse_translation

# The purpose of the function is to process the specified text file 
# (using the file that was )
def processDataFile():
    # Use a try-except block to handle the IOError exception
    try:
        # Open the file in read mode        
        with open('TelephoneData.txt', 'r') as text_file:
            # Read all lines
            lines = text_file.readlines()

            # Create an empty list
            clean_lines = []

            # Remove the \n character from each line and append to the list
            for line in lines:
                stripped_line = line.rstrip('\n')
                if stripped_line:
                    clean_lines.append(stripped_line)

            # Group the data into 6 lines each
            grouped = [clean_lines[i:i+6] for i in range(0, len(clean_lines), 6)]

            # Put each data in record into categories
            for group in grouped:
                name = group[0]
                address = group[1]
                city = group[2]
                state = group[3]
                zip = group[4]
                words = int(group[5])

                # Calculate the cost using the calcCost function
                # and from the number of words in the file
                total_cost = calcCost(words)

                # Display the information that was read
                print(f'\n{name}')
                print(f'{address}')
                print(f'{city}, {state} {zip}')
                print(f'Cost of telegram sent is {total_cost:.2f} for {words} words\n')
    
    # Handle the IOError exception
    except IOError:
        print('ERROR: File not found. Please try again.')


# Call the main function
if __name__ == '__main__':
    main()