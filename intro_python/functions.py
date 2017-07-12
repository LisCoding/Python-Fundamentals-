# function are objects in python

def eat():
    print "I like to eat sushi"

eat() #call the function
print eat() # return none
print eat

#function taking argument and retuns a value
def sum(num1, num2):
    return num1 + num2

print sum(5, 5)

# function with default values
def power(num, x = 1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

print power(2,3)
print power(2)

#function with one or more arguments(splat operator)
def addition(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print addition(4,5,6)
