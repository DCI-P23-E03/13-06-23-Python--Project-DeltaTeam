from datetime import datetime
import pytz

print("Enter 1 for Tokyo")
print("Enter 2 for Dublin")
print("Enter 3 for San Francisco")
print("Enter 4 for Berlin")
print("Enter 5 for johannesburg")
city = input("Which timezone do you need: ")

tokyo = pytz.timezone('Asia/Tokyo')
dublin = pytz.timezone('Europe/Dublin')
sanfran = pytz.timezone('America/Los_Angeles')
berlin = pytz.timezone('Europe/Berlin')
johannes = pytz.timezone('Africa/Johannesburg')

if city == "1":
    tokyo_current = datetime.now(tokyo)
    tokyo_time = tokyo_current.strftime('%H:%M:%S')
    print(f"Current time in Tokyo is: {tokyo_time}")
elif city == "2":
    dublin_current = datetime.now(dublin)
    dublin_time = dublin_current.strftime('%H:%M:%S')
    print(f"Current time in Dublin is: {dublin_time}")
elif city == "3":
    sanfran_current = datetime.now(sanfran)
    sanfran_time = sanfran_current.strftime('%H:%M:%S')
    print(f"Current time in San Francisco is: {sanfran_time}")
elif city == "4":
    berlin_current = datetime.now(berlin)
    berlin_time = berlin_current.strftime('%H:%M:%S')
    print(f"Current time in Berlin is: {berlin_time}")
elif city == "5":
    johannes_current = datetime.now(johannes)
    johannes_time = johannes_current.strftime('%H:%M:%S')
    print(f"Current time in Johannesburg is: {johannes_time}")
else:
    print(f"{city} is very wrong, get lost!")
