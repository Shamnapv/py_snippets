import calendar
year=int(input("enter the year:"))
month=int(input("enter the month(1-12):"))
if 1<= month <=12:
    print(calendar.month(year,month))
else:
    print("Invalid month! please enter a number between 1 and 12.")