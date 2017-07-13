# working with the datetime module

from datetime import date
from datetime import time
from datetime import datetime

#DATE OBJECT
def main():
    today = date.today()
    print "today's date is: ", today
    print "today is", date.weekday(today)
#date individual components
    print "Date components:", today.day, today.month, today.year


    #DATETIME OBJECTS
    t = datetime.time(datetime.now())
    todayDay = datetime.now()
    print "current date is: ", todayDay
    print "current time is: ", t



if __name__ == "__main__":
    main();
