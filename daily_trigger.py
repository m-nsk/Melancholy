"""Trigger at specific time of day"""

import datetime

def daily_trigger(t: datetime.time):
    while True:
        if datetime.datetime.now().strftime("%H %M") == t.strftime("%H %M"):
            text = input("Enter today's journal entry:\n")
            return {"Date": datetime.datetime.now().strftime("%Y-%m-%d"), "Text": text}
    
print(daily_trigger(datetime.time(16,4)))