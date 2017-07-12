# defining functions
def greating():
    name = "Liseth"
    print "Hello " + name + "!"
greating()

def hobbies():
    sport = "tennis";
    print "I like to play " + sport

hobbies()

# Declare a variable and initialize it
num = 10
print num

#reasign a variable
num = 30
print num
# global variables
name = "Lis"
def myFunction():
    global name
    name = "liseth"
    print name

myFunction()
print name


# del -> delete a varible assignmet
color = "red"
print color
del color 
print color
