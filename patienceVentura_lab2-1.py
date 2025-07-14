# patience ventura  2025Jan23  patienceVentura_lab2-1.py

'''

This program calculates how many grapevines I. B. Winemaker needs to plant per
row using the formula V = (R - (2*E)) / S, where 
V is the number of grapevines per row (vines_num), 
R is for the length of row in meters (row_length), 
E is for the space, in meters, of each end-post assembly (end_post_space), and
S for the space between planted vines in meters (space_between_vines). 

'''

# Get input from user

row_length = float(input('Enter the length of the row, in meters: '))
end_post_space = float(input('Enter the amount of space, in meters, used by each end-post assembly: '))
space_between_vines = float(input('Enter the distance, in meters, between each vine: '))

# Calculate using the formula and input given by user
vines_num = int((row_length - (2*end_post_space))/space_between_vines)

# Display results
print(f'You have enough space for', vines_num, ' vines.')
