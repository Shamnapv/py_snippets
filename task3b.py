import datetime
year=int(input("enter the year:"))
month=int(input("enter the month(1-12):"))
first_day=datetime.date(year,month,1)
if month == 12:
    next_month = datetime.date(year + 1, 1, 1)
else:
    next_month = datetime.date(year, month + 1, 1)

days_in_month = (next_month - first_day).days
print("\nMo Tu We Th Fr Sa Su")
start_weekday = first_day.weekday()  # Monday = 0
day = 1
print("   " * start_weekday, end="")
for i in range(start_weekday, start_weekday + days_in_month):
    print(f"{day:2d} ", end="")
    if (i + 1) % 7 == 0:
        print()
    day += 1

print()