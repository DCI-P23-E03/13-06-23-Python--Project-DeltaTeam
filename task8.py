from datetime import datetime, timedelta

current = datetime.now()  
opposite = current + timedelta(hours=12)

print("Your current time is:", current.strftime("%H:%M:%S"))
print("Time on the opposite end of the world is:", opposite.strftime("%H:%M:%S"))





