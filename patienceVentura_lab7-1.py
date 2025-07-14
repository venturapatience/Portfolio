# patience ventura 27 February 2025 patienceVentura_lab7-1.py
'''
This program allows the user to enter the name of the team to find out how many 
times that team won in the World Series from the period 1903 to 2023.
'''

# Import the csv module
import csv


# The main function determines the flow of the program. While user presses 
# continue, the program continues to provide a menu to choose from.
def main():

    # Read the csv file
    worldSeries = readFile()

    # Enter a loop
    cont = ""
    while cont == "":

        # Program menu
        print("\nWorld Series Winners\n")
        print("1. Display winners by team")
        print("2. Display winners by years")
        print("3. End program")

        # Get input from user
        cont = input('\nPlease enter choice: ')

        # Based on user's input, the program will either go to the
        # winnersByTeam function, winnersByYears function, or 
        # end the program
        if cont == '1':
            winnersByTeam(worldSeries)
        elif cont == '2':
            winnersByYears(worldSeries)
        elif cont == '3':
            break
        else:
            print('Invalid input!')

        cont = input("\nPress enter to continue")


# The readFile function reads the csv file using the csv module
# and stores it inside a list
def readFile():
    try:
        with open('WorldSeriesWinners.csv', 'r') as world_series_file:
            # Creates a list with two columns. Each row is also a list
            read_lines = list(csv.reader(world_series_file))

        return read_lines

    # Handling the error
    except FileNotFoundError:
        print('The file does not exist.')


# The winnersByTeam function uses the list from the readFile() to 
# display the years the team has won
def winnersByTeam(main_list):

    win_by_team = []

    # Get input and use the lower function
    search = input('\nEnter team name: ')
    search = search.lower()

    # If input is found in a row in the Team column, item in 
    # the Year column is appended to the empty list
    for row in main_list:
        if search in row[1].lower():
            win_by_team.append(row[0])

    # Print 5 numbers per line
    print(f'The {search} won the series in')
    for i in range(len(win_by_team)):
        print(win_by_team[i], end=" ")
        if (i+1) % 5 == 0:
            print("")
    print()


# The winnersByYears function displays the winning team from the user's input
# of beginning and ending years
def winnersByYears(main_list):

    # Put the Year column from the csv file into one list, and 
    # the Team column into another
    years = []
    teams = []

    for row in main_list:
        years.append(row[0])
        teams.append(row[1])

    # Get input
    begin_year = input('\nEnter beginning year: ')
    end_year = input('Enter ending year: ')

    # Input validation so the user will only enter 1903 to 2023
    while int(begin_year) < 1903 or int(end_year) > 2023:
        print('ERROR: Invalid year input. Please enter a year between 1903 and 2023.')
        begin_year = input('\nEnter beginning year: ')
        end_year = input('Enter ending year: ')

    print('\nWorld Series Winners by Year')

    # Get index of the inputs from user
    if begin_year in years:
        begin_year_index = years.index(begin_year)
        end_year_index = years.index(end_year)

    # Display the winners for the years listed
    for i in range(begin_year_index, end_year_index+1):
        print(years[i], '>>', teams[i])


# Call the main function
if __name__ == '__main__':
    main()