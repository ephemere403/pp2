from datetime import datetime,timedelta
current_date = datetime.now()
five_days = timedelta(days = 5)
print(current_date-five_days)

difference = timedelta(days = 1)
print("Today is: " + str(current_date.strftime("%c")))
print("Yesterday was: "+str((current_date-difference).strftime("%c")))
print("Tommorow will be: "+ str((current_date+difference).strftime("%c")))

formatted_date = current_date.replace(microsecond=0)
print(formatted_date)

second_date = datetime(year = 2003,month = 5, day = 27)
difference = current_date - second_date
print("difference in seconds: " + str(difference.total_seconds()))