from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%X')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %A')

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,9,12,30,10)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)

result = simdi - timedelta(days = 10)

"""# Import the time module
import time
# Import the datetime module
import datetime

# Print the current date and time using datetime
print("Current date and time: " , datetime.datetime.now())

# Print the current year extracted from today's date
print("Current year: ", datetime.date.today().strftime("%Y"))

# Print the month of the year extracted from today's date
print("Month of year: ", datetime.date.today().strftime("%B"))

# Print the week number of the year extracted from today's date
print("Week number of the year: ", datetime.date.today().strftime("%W"))

# Print the weekday of the week extracted from today's date
print("Weekday of the week: ", datetime.date.today().strftime("%w"))

# Print the day of the year extracted from today's date
print("Day of year: ", datetime.date.today().strftime("%j"))

# Print the day of the month extracted from today's date
print("Day of the month : ", datetime.date.today().strftime("%d"))

# Print the day of the week extracted from today's date
print("Day of week: ", datetime.date.today().strftime("%A")) """
