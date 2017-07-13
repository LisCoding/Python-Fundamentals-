#workin wuth loops
#while loops
def boom():
    x = 5
    while (x > 0):
        print "boom" + str(x)
        x = x - 1
boom ()

# For Loops
def myFavNumbers():
    for num in range(2, 10):
        print num

myFavNumbers()

#Iterating through a collection
sports = ["tennis","soccer", "football", "swimming"]

def play(sports):
    for x in sports:
        print "I love playing " + x + "!"


play(sports)

#using the the enumerate function
numbers = [1, 2, 4, 8, 10]
def favNums(arr):
    for i, num in enumerate(arr):
        print i, num

favNums(numbers)

#using break statement

def myNums():
    for i in range(1, 10):
        if(i == 5): break
        print i

myNums()

#using continue statement
def oddNumbers():
    for i in range(1, 12):
        if (i % 2 == 0): continue
        print i

oddNumbers()
