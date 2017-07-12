#working with classes
class myStudents():
    def method1(self):
        print "Student number 1"

    def method2(self, course):
        print "Student is taking: " + course

#using inhertance
class  otherStudents(myStudents):
    def method2(self, course):
        print "Stundent change class from python to" + course

    def method1(self):
        print "I overide method1 from myStudents class"

def main():
    student1 = myStudents()
    student1.method1()
    student1.method2("Python")

    student2 = otherStudents()
    student2.method1()
    student2.method2("Java")

if __name__ == "__main__":
    main()
