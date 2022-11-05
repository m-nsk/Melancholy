"""Insert objective here!!!"""

from datetime import datetime
def todays_diary(): 
  while True: 
    todays_diary = input("Today's diary is")
    dates = []
    sum_todays_diary = []
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in dates:
      sum_todays_diary.append(todays_diary())
      dates.append(today)
      print(sum_todays_diary)