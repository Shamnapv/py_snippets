import calendar
year=int(input("enter the year:"))
month=int(input("enter the month(1-12):"))
if 1<= month <=12:
    print(calendar.month(year,month))
else:
    print("Invalid month! please enter a number between 1 and 12.")

"""output:
(base) PS C:\Users\shaim\Desktop\pythonlab> python task3a.py
enter the year:2021
enter the month(1-12):1
    January 2021
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
(base) PS C:\Users\shaim\Desktop\pythonlab> python task3a.py
enter the year:2023
enter the month(1-12):13
Invalid month! please enter a number between 1 and 12."""
