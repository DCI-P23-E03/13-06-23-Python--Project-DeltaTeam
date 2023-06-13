from datetime import datetime
date1 = input("Give first date(YYYY/MM/DD HH:MM:SS): ")
date2 = input("Give second date(YYYY/MM/DD HH:MM:SS): ")
result = input("Do you want the time difference in seconds, days or years(s/d/y): ")
d1 = datetime.strptime(date1, "%Y/%m/%d %H:%M:%S")
d2 = datetime.strptime(date2, "%Y/%m/%d %H:%M:%S")
delta = d2 - d1
if result == "s":
    print(f"Time difference is {delta.total_seconds()} seconds")
elif result == "d":
    print(f"Time difference is {delta.days} days")
elif result == "y":
    years = d2.year -d1.year
    print(f"Time difference is {years} years")
else:
    print(f"I don't understand {result}, program closes.")