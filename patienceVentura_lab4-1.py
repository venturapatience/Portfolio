# patience ventura 2025February06 patienceVentura_lab4-1.py
'''
This is a program that predicts the approximate population growth of bacteria.
The program will ask the user for the starting count of bacteria, the average
daily population increase, and the number of days to run the experiment.
Multiple runs are allowed until the user decides to terminate the program.
'''

# Initialize the variable to control the loop
keep_going = '1' 

# Use nested loops to display the population for each day that the bacteria grows
# and allow repetition of the experiment until the user decides to terminate the program

while keep_going == '1':    

    # Get the starting count of bacteria and validate it
    count = int(input('Starting number of bacteria: '))
    while count <= 0:
        print('ERROR: Count should be greater than 0')
        count = int(input('Starting number of bacteria: '))

    # Get the population percent increase and validate it
    popn_pct = float(input('Average daily percent (%) increase: '))
    while popn_pct <= 0:
        print('ERROR: Population percent increase should be greater than 0')
        popn_pct = float(input('Average daily percent (%) increase: '))
    
    # Get the number of days and validate it
    num_days = int(input('Length of experiment in days: '))
    while num_days <= 0:    
        num_days = int(input('Length of experiment in days: '))

    # Print the table headings
    print('Day\tPopulation')
    print('------------------')

    # Calculate the population for each day
    for day in range(1, num_days+1):
        print(f'{day}\t{count:.0f}')
        count = count * (1 + (popn_pct / 100))

    # Ask user if they want to run another test
    keep_going = input('run another test? 1 = yes, press ENTER to stop ')

    # Terminate the program if the user presses enter
    if keep_going == '':
        break
