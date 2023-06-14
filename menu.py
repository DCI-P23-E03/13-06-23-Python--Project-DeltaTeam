'''
Show a simple menu using the input() function to allow users to select different options. Design an intuitive menu that guides users through the available features.'''

# importing datetime module, time module
import datetime, time, calendar
#from datetime import date, timedelta, time, datetime
import pytz
import random
from dateutil import relativedelta

#while True:
# menu to take input from the user
print('''
    0 - Current Time 
    1 - Current Unix Timestamp
    2 - Convert String into Datetime
    3 - Leap Year and time untill Next Leap year
    4 - Specific unit(seconds, days, years)
    5 - Current month Calendar
    6 - Timezone
    7 - Current time at the opposite end of world
    8 - Joke
    9 - Surprise
    ''')

choice = int(input("Enter your choice from menu: "))

if choice == 0:
        print(f"\nCurrent Time: ",datetime.datetime.now().time().strftime("%H:%M:%S"))
elif choice == 1:
        print(f"\nCurrent Unix Time(since 1, Jan): ", time.time())
elif choice == 2:
        #string = "2023-06-13 15:17:05"
        string1 = input("Enter datetime in formate (YYYY-MM-DD HH:MM:SS): ")
        print(f"String to Datetime formate: ", datetime.datetime.strptime(string1,"%Y-%m-%d %H:%M:%S"))
elif choice == 3:
        year = datetime.date.today().year
        while True:
              year += 1
              if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                break

        date = datetime.date.today()
        leap_year = datetime.date(year, 2, 29)
        count = leap_year - date
        print(f"\nDays to wait until next leap year are: {count.days}.")
        
elif choice == 4:
        
        # input 2 dates from user

        td = input("\nEnter First date in (YYYY-MM-DD HH:MM:SS) :")
        td1 = input("\nEnter Second date in (YYYY-MM-DD HH:MM:SS): ")
        date1 = datetime.datetime.strptime(td, "%Y-%m-%d %H:%M:%S")
        date2 = datetime.datetime.strptime(td1, "%Y-%m-%d %H:%M:%S")
        time_output = input("Choose 'Days' or 'Secs' or 'Year' to see difference in:  ").upper()

        delta = date2 -date1
        if time_output == "DAYS":
            print("\nTime difference in Days :", delta.days,"days")
        elif time_output == "SEC":
            print("\nTime difference in Seconds :", delta.total_seconds,"seconds")
        elif time_output == "YEAR":
            year = date2.year - date1.year
            print("Thime differnec in Years :", year, "year")    
        else:
            print("Invalid!, choose wisely.")

elif choice == 5:
        # Enter the month and year
        cal_year = int(input("\nEnter year: "))
        cal_month = int(input("\nEnter month:"))
        cal_today = datetime.now().day
        color_today = '\033[92m'+ str(cal_today) +'\033[0m'
        cal_output = calendar.month(cal_year,cal_month)
        highlight_today = cal_output.replace(str(cal_today),color_today)
        print(highlight_today)    
elif choice == 6:
        print('''
        T - Tokyo/Japan
        D - Dublin / Ireland
        S - San Francisco / USA
        B - Berlin / Germany
        J - Johannesburg / South Africa''')
        timezone_choose = input("\nChoose timezone to show it's time: ").upper()
        if timezone_choose == "T":
            japan_timezone = pytz.timezone("Japan")
            time_in_japan = datetime.datetime.now(japan_timezone)
            currtime_in_japan = time_in_japan.strftime("%H:%M:%S")
            print("\nThe current time in Tokyo is: ",currtime_in_japan)

        elif timezone_choose == "D":
            dublin_timezone = pytz.timezone("Europe/Dublin")
            time_in_dublin = datetime.datetime.now(dublin_timezone)
            currtime_in_dublin = time_in_dublin.strftime("%H:%M:%S")
            print("\nThe current time in Dublin is: ",currtime_in_dublin)
        
        elif timezone_choose == "S":
            sanf_timezone = pytz.timezone("America/Los_Angeles")
            time_in_sanf = datetime.datetime.now(sanf_timezone)
            currtime_in_sanf = time_in_sanf.strftime("%H:%M:%S")
            print("\nThe current time in San Francisco is: ",currtime_in_sanf)
        
        elif timezone_choose == "B":
            berlin_timezone = pytz.timezone("Europe/Berlin")
            time_in_berlin = datetime.datetime.now(berlin_timezone)
            currtime_in_berlin = time_in_berlin.strftime("%H:%M:%S")
            print("\nThe current time in Berlin is: ",currtime_in_berlin)
        
        elif timezone_choose == "J":
            johann_timezone = pytz.timezone("Africa/Johannesburg")
            time_in_johann = datetime.datetime.now(johann_timezone)
            currtime_in_johann = time_in_johann.strftime("%H:%M:%S")
            print("\nThe current time in Johannesburg is: ",currtime_in_johann)
        else:
            print("Invalid!, Choose wisely....")
elif choice == 7:
        current_time = datetime.datetime.now()
        other_side_of_world = current_time + datetime.timedelta(hours=12)
        print("Your current time is: ", current_time.strftime("%H:%M:%S"))  
        print("The current time other side of world is: ",other_side_of_world.strftime("%H:%M:%S"))
elif choice == 8:
        print("Here comes, your random jokes.......: \n")
        joke = [
            "There are only ten kinds of people in this world: those who know binary and those who don't.",
            "C allows you to shoot yourself in the foot. C++ allows you to re-use the bullet.",
            "How to function break up.................They stop calling each other!!!",
            "Why do Java Pogrammers have to wear glasses?...............Because they don't C#",
            "What did the Python say when he came out of his shell?..........Print('Hello World!')",
            "It must have been a real shock when people found out the Monty Python theme was originally written by someone from the United States........After all, nobody expects the American composition",
            "Why did the Python data scientist get arrested at customs?.........She was caught trying to import pandas!",
            "Why do Python programmers have low self esteem?..........They're constantly comparing their self to other.",
            "I failed my python breeding class because of a late assignment........My homework ate my dog.",
            "Why does the Python live on land?..........Because it's above C-level",
            "Since MIT is giving free access to their courses online, I shall study Computer science web programming with Python and Java...........as I thought it would be so cool to have a large snake round my neck as I drink coffee.",
        ]
        joke1 = random.choice(joke)
        print(joke1)
elif choice == 9:
        # input 2 dates
        date1 = input("Enter First date in (DD-MM-YYY): ")
        date2 = input("Enter Secon date in (DD-MM-YYYY): ")
        
        # convert string to date object
        d1 = datetime.datetime.strptime(date1,"%d-%m-%Y")
        d2 = datetime.datetime.strptime(date2,"%d-%m-%Y")

        delta = relativedelta.relativedelta(d2,d1)
        print("Year, Months, Days between two date is: ", delta.years,"year", delta.months, "months", delta.days, "days")
else:
        #break    
        print("End...")