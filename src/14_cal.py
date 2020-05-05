"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
# These are modules
import sys 
import calendar
from datetime import datetime

# starts the week on a Monday displays the week headers
# The number represents how many letters to display
print(calendar.weekheader(3))
print() # adds a space in your output

# prints the index of the first weekday which is 0
print(calendar.firstweekday())
print()

# prints the selected month (1-12) and the given year
print(calendar.month(2020, 3,))
print()

# prints out the calendar in a flat list 
print(calendar.monthcalendar(2020, 3))
print()

# prints out the calendar for the entire year
print(calendar.calendar(2020))
print()

args = sys.argv
if(len(args) == 1):
     cal = calendar.TextCalendar()
     month = datetime.now().month
     year = datetime.now().year
     print(cal.prmonth(year, month))
elif(len(args) == 2):
     cal = calendar.TextCalendar()
     month = int(args[1])
     year = datetime.now().year
     print(cal.prmonth(year, month))
elif(len(args) == 3):
    cal = calendar.TextCalendar()
    month = int(args[1])
    year = int(args[2])
    print(cal.prmonth(year, month))
else:
     print("wrong format")
     print()
     print("Expecting in format: \n> py14_cal.py(month number)(year)")

