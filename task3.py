from datetime import datetime
date = input("Enter a date(YYYY/MM/DD): ")
d = datetime.strptime(date, "%Y/%m/%d")
print(f"Your date: {date} converted into datetime datatype looks like this {d}.")
