from datetime import date, time, datetime

# get todays date
date = date.today()
print("today's date is " + str(date))

# get present time
present = datetime.now()
time = present.strftime("%H:%M:%S")
print(time)