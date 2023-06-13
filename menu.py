print("Enter: 1 for current time")
print("Enter: 2 for current time in UNIX timestamp")
print("Enter: 3 to convert date into datetime datatype")
print("Enter: 4 for time until next leap year")
print("Enter: 5 to dispaly a date in seconds, days, or years")
print("Enter: 6 for calendar of current month")
print("Enter: 7 for multiple timezones")
print("Enter: 8 for time in the opposite end of the world")
print("Enter: 9 for a joke")
print("Enter: 0 for countdown to Gamescom Cologne 2023")
menu = input("Your choice: ")
if menu == "1":
    print("\n")
elif menu == "2":
    print("\n")
elif menu == "3":
    print("\n")
elif menu == "4":
    print("\n")
elif menu == "5":
    print("\n")
elif menu == "6":
    print("\n")
elif menu == "7":
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
elif menu == "8":
    from datetime import datetime, timedelta
    current = datetime.now()  
    opposite = current + timedelta(hours=12)
    print("Your current time is:", current.strftime("%H:%M:%S"))
    print("Time on the opposite end of the world is:", opposite.strftime("%H:%M:%S"))
elif menu == "9":
    import random
    jokes = [
            "I'm afraid for the calendar. Its days are numbered.",
            "My wife said I should do lunges to stay in shape. That would be a big step forward.",
            "Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!",
            "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
            "What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.",
            "What do you call a fish wearing a bowtie?" "Sofishticated.",
            "How do you follow Will Smith in the snow?" "You follow the fresh prints.",
            "If April showers bring May flowers, what do May flowers bring?" "Pilgrims.",
            "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.",
            "How does dry skin affect you at work?" "You dont have any elbow grease to put into it.",
            "What do you call a factory that makes okay products?" "A satisfactory.",
            "Dear Math, grow up and solve your own problems.",
            "What did the janitor say when he jumped out of the closet?" "Supplies!",
            "Have you heard about the chocolate record player? It sounds pretty sweet.",
            "What did the ocean say to the beach?" "Nothing, it just waved.",
        ]
    joke = random.choice(jokes)
    print(joke)
elif menu == "0":
    from datetime import datetime
    gamescom = datetime(year=2023, month=8, day=23, hour=9)
    countdown = gamescom - datetime.now()
    print(f"Countdown to Gamescom 2023 in Clogne: {countdown} WOOHOOOO!!!")
else:
    print("Syntax error, format C:")