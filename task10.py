from datetime import datetime

gamescom = datetime(year=2023, month=8, day=23, hour=9)
countdown = gamescom - datetime.now()

print(f"Countdown to Gamescom 2023 in Clogne: {countdown} WOHOOO!!!")
