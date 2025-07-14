# patience ventura  2025Jan30  patienceVentura_lab3-2.py
'''

This program asks the user to input a number of seconds and 
calculates the number of days, hours, minutes and seconds from the input seconds.

'''

# Get input from user
seconds_input = int(input('Enter the number of seconds: '))

# Initialize the number of seconds per minute, hour, and day, and hours per day
SEC_PER_MINUTE = 60
SEC_PER_HOUR = 3600
SEC_PER_DAY = 86400
HOURS_PER_DAY = 24

# Calculate the number of days, hours, minutes, and seconds based on 
# the input seconds and display the result

if seconds_input < 60:
    seconds = seconds_input
    #Display the result
    print(f'''{seconds_input} seconds is equal to:
    {seconds} second(s)''')

elif seconds_input >=60 and seconds_input < 3600:
    minutes =  seconds_input // SEC_PER_MINUTE
    seconds = seconds_input % SEC_PER_MINUTE
    #Display the result
    print(f'''{seconds_input} seconds is equal to:
    {minutes} minute(s) and
    {seconds} second(s)''')

elif seconds_input >= 3600 and seconds_input < 86400:
    hours = seconds_input // SEC_PER_HOUR
    minutes = (seconds_input // SEC_PER_MINUTE) % SEC_PER_MINUTE
    seconds = seconds_input % SEC_PER_MINUTE
    #Display the result
    print(f'''{seconds_input} seconds is equal to:
    {hours} hour(s),
    {minutes} minute(s), and
    {seconds} second(s)''')

else:
    days = seconds_input // SEC_PER_DAY
    hours = (seconds_input // SEC_PER_HOUR) % HOURS_PER_DAY
    minutes = (seconds_input // SEC_PER_MINUTE) % SEC_PER_MINUTE
    seconds = seconds_input % SEC_PER_MINUTE
    #Display the result
    print(f'''{seconds_input} seconds is equal to:
    {days} day(s),
    {hours} hour(s),
    {minutes} minute(s), and
    {seconds} second(s)''')

