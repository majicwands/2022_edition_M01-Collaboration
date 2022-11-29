
#total_seconds = float(input('Enter a number of seconds: '))
total_hours = float(input('Enter the amount of hours: '))
hours = total_hours

# Get the number of remaining minutes.
minutes = (total_hours * 60) 

# Get the number of remaining seconds.
seconds = (total_hours * 3600)

# Display the results.
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)
