# patience ventura  2025Jan30  patienceVentura_lab3-1.py
'''

This program asks a user to input two distinct primary colors to mix. 
The program will then output the secondary color that results from mixing the two primary colors.

'''

# Instructions for user
print("Let's mix primary colors to get a secondary color!")
print('Color choices:\n1 = red\n2 = blue\n3 = yellow')

# Get input from user

color1 = input('Enter the name or number of first color from the choices > ')
color2 = input('Enter the name or number of second color from the choices > ')

### Determine the secondary color using if-elif-else statement then print the result

# if clause to check if input is a string. If true, then another if-elif-else statement 
# will be used to determine the secondary color.

if color1.isalpha() == True and color2.isalpha() == True:
    if (color1.lower() == 'red' and color2.lower() == 'blue') or (color1.lower() == 'blue' and color2.lower() == 'red'):
        print('The secondary color is purple.')
    elif (color1.lower() == 'red' and color2.lower() == 'yellow') or (color1.lower() == 'yellow' and color2.lower() == 'red'):
        print('The secondary color is orange.')
    elif (color1.lower() == 'blue' and color2.lower() == 'yellow') or (color1.lower() == 'yellow' and color2.lower() == 'blue'):
        print('The secondary color is green.')
    elif color1.lower() == color2.lower():
        print('COLOR1 AND COLOR2 CANNOT BE THE SAME!')
    else:
        print('COLOR CHOICE INVALID - PROGRAM ENDING!')

# elif clause to check if inputs are numbers. If true, then another if-elif-else statement 
# will be used to determine the secondary color.

elif color1.isdigit() == True and color2.isdigit() == True:
    color1 = int(color1)
    color2 = int(color2)
    if (color1 == 1 and color2 == 2) or (color1 == 2 and color2 == 1):
        print('The secondary color is purple.')
    elif (color1 == 1 and color2 == 3) or (color1 == 3 and color2 == 1):
        print('The secondary color is orange.')
    elif (color1 == 2 and color2 == 3) or (color1 == 3 and color2 == 2):
        print('The secondary color is green.')
    elif color1 == color2:
        print('COLOR1 AND COLOR2 CANNOT BE THE SAME!')
    else:
        print('COLOR CHOICE INVALID - PROGRAM ENDING!')

# else clause when inputs are invalid

else:
    print('COLOR CHOICE INVALID - PROGRAM ENDING!')
