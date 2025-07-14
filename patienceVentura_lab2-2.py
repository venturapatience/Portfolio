# patience ventura  2025Jan23  patienceVentura_lab2-2.py

'''

This program adjusts and calculates the quantity of each ingredient based on the
number of cookies the user wants, according to the given recipe.

'''

# Get input from the user on how many cookies they want to make
num_cookies_want = int(input('Enter the number of cookies you want to make: '))

# Initialize the number of cups per ingredient and the number of cookies made for a recipe
CUP_SUGAR = 1.50
CUP_BUTTER = 1.75
CUP_FLOUR = 2.75

COOKIES_MADE = 39

# Calculate the cups per ingredient based on the number of cookies inputted
cup_sugar_needed = (CUP_SUGAR/COOKIES_MADE)*num_cookies_want
cup_butter_needed = (CUP_BUTTER/COOKIES_MADE)*num_cookies_want
cup_flour_needed = (CUP_FLOUR/COOKIES_MADE)*num_cookies_want

# Display the results based on calculations
print(f'''
To make {num_cookies_want} cookies, you will need:
{cup_sugar_needed:.2f} cups of sugar
{cup_butter_needed:.2f} cups of butter
{cup_flour_needed:.2f} cups of flour
''')