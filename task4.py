import datetime

year = datetime.date.today().year
while True:
    year += 1
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        break

date = datetime.date.today()
leap_year = datetime.date(year, 2, 29)
count = leap_year - date
print(f"Days to wait until next leap year are: {count.days}.")

