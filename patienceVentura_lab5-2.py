# patience ventura 13 Feb 2025 patienceVentura_lab5-2.py
'''
This program estimates the total cost of calculations for a paint job.
'''

# Import math module for calculations 
import math 

# Global Constants
SQ_FEET_PER_GALLON = 350
LABOR_HOURS_PER_GALLON = 4.55
LABOR_COST_PER_HOUR = 45

# Define the functions
def main():
    another = '1'
    while another == '1':
        # Input number of rooms
        input_room = int(input('How many rooms will be painted? '))
        x = numRooms(input_room)
        pricePaint = paintPrice()
        cost = calcCost(totArea=x, paint_price=pricePaint)
        printResults(cost, x)

        another = input('Another estimate? 1 = yes OR press ENTER to stop \n')

# Function purpose is to get input from user about the measurements of walls and 
# at the same time, to calculate the total square footage to be painted
def numRooms(room):

    # Input validation for number of rooms
    while room < 1:
        room = int(input('Rooms cannot be less than 1. How many rooms will be painted? '))

    total_area = 0  #initialization

    for i in range(1,room+1):
        for j in range(1,3):
            print(f'\nPlease enter the height and length of wall {j} for room # {i}')

            # Input validation for wall height so that square footage cannot be 0 or negative
            height = float(input('Wall height: '))
            while height <= 0:
                print('ERROR: Height must be greater than 0.')
                height = float(input('Wall height: '))

            # Input validation for wall length so that square footage cannot be 0 or negative
            length = float(input('Wall length: '))
            while length <= 0:
                print('ERROR: Length must be greater than 0.')
                length = float(input('Wall length: '))

            # Calculate and accumulate square footage for all walls
            wall_area = 2 * (height * length)
            total_area += wall_area

    return total_area


# Function purpose is to ask user the price per gallon of paint
def paintPrice():

    print('\nThe minimum price of the paint must be $22.50')

    # Input price from user
    price_per_gallon = float(input('Please enter the price per gallon of the paint: '))

    # Input validation for price per gallon of paint
    while price_per_gallon < 22.50:
        print('ERROR: The price cannot be less than $22.50')
        price_per_gallon = float(input('Please enter the price per gallon of the paint: '))

    return price_per_gallon


# Function purpose is to calculate the total cost for the job including
# the gallons required, labor hours, and the overall cost
def calcCost(paint_price, totArea):

    # Cannot purchase fractional gallons of paint
    gallons_paint_required = math.ceil(totArea/SQ_FEET_PER_GALLON) 
    paint_cost = gallons_paint_required*paint_price

    # Labor hours and cost 
    labor_hrs = gallons_paint_required*LABOR_HOURS_PER_GALLON
    labor_cost = labor_hrs*LABOR_COST_PER_HOUR

    total_job_cost = paint_cost+labor_cost

    return gallons_paint_required, paint_cost, labor_hrs, labor_cost, total_job_cost


# Function purpose is to display all the results of calculations
def printResults(costCalc, squareFootage):

    gallons_paint_required, paint_cost, labor_hrs, labor_cost, total_job_cost = costCalc
    
    print(f'\nSquare feet to be painted = {squareFootage:.2f}')
    print(f'\nGallons of paint required is {gallons_paint_required:.2f} gallons')
    print(f'Paint cost is ${paint_cost:.2f}\n')
    print(f'Labor hours are {labor_hrs:.2f}')
    print(f'Labor cost is ${labor_cost:.2f}\n')
    print(f'Total job cost is ${total_job_cost:.2f}\n')


# Call the main function
if __name__ == '__main__':
    main()