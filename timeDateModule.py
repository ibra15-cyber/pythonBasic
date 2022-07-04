from datetime import datetime

dateObj = datetime.now() - datetime(1900, 12, 31)
print(type(dateObj))
print("date diff: ", dateObj)
print("days: ", dateObj.days)

now = datetime.now()
print(type(now))
print(now)


date = datetime(1990, 9, 18) #create a datetime dateObj
date2 = datetime.now() #creates the current date time
date3 = datetime.strptime("2018:09:17 05:35:59", "%Y:%m:%d %H:%M:%S")

#calling a an already defined time in a format prefare
date4 = date2.strftime("%Y") #need only the year
print(date)
print(date2)
print(date3)
print(date4)
