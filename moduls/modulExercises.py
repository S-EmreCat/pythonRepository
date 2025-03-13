# https://pynative.com/python-date-and-time-exercise/#h-exercise-1-print-current-date-and-time-in-python


# Exercise 1: Print current date and time in Python
from time import gmtime, strftime

# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

#Exercise 2: Convert string into a datetime object
from datetime import datetime

date_string = "Feb 25 2020  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
# print(datetime_object)


# Exercise 3: Subtract a week (7 days)  from a given date in Python
from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("Given date")
print(given_date)

days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print("New Date")
print(res_date)

# Exercise 4: Print a date in a the following format
from datetime import datetime

given_date = datetime(2020, 2, 25)
print("Given date is")
print(given_date.strftime('%A %d %B %Y'))

# Exercise 5: Find the day of the week of a given date

from datetime import datetime

given_date = datetime(2020, 7, 26)

# to get weekday as integer
print(given_date.today().weekday())

# To get the english name of the weekday
print(given_date.strftime('%A'))