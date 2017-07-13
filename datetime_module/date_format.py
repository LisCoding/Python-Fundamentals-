#formatting date and output
# Time and dates can be formatted a set of predefined strings
from datetime import datetime

def main():
    now = datetime.now()
    print "current time is", now

#Date formatting
#%y/%Y -> Year, %a,/%A ->weekday, %b/%B -> month, %d- dayof the moth
# strftime
    date_formated = now.strftime("%y, %b, %a, %d")
    print "today is: ", date_formated

# %c = local-s date and time. %x -> locales's  date, %X locale's time
    print now.strftime("%c")
    print now.strftime("%x")
    print now.strftime("%X")


#Time formatting
    #%I/%H -> 12/24  HOUR , %M - Minute %S seconds %p AM/PM
    print now.strftime("%I:%M:%S %p")

if __name__ == "__main__":
    main();
