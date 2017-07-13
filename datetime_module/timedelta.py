#working with timedelta objects

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#construct a basic timedelta and print it
print timedelta(days=365, hours=5, minutes= 1)

#print today's date
today = datetime.now()
print "Today is: ", today

#print today's date one year from now
print "One year from now the date will be: " + (str(today + timedelta(days=365)))

#create a timedelta that uses more than one arguments
print "In two weeks and 3 days it will be: "  + (str(today + timedelta(weeks = 2, days=3)))

#calculates the date 1 week ago, formatted as srtings
lastWeek = today - timedelta(days= 7)
stringTime= lastWeek.strftime("%A %B %d, %Y")
print "One week ago it was " + stringTime

### How many days until April Fool's Day?
todayDate = date.today()
aprilFoolsday = date(today.year, 4, 1) # get April's fool for the same year

if aprilFoolsday < todayDate:
    print "April fool's day already went by %d days ago" %((todayDate - aprilFoolsday).days)
    aprilFoolsday.replace(year=todayDate.year + 1)

#calculate the amount of time until April Fool's Day
nexttime = abs(aprilFoolsday - todayDate)
print nexttime.days, "days until next April Fool's Day!"
