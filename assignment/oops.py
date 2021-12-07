'''class Parrot:

    speices = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def function(self,action):
        print("the {} is always{}".format(self.name,action))

a = Parrot('ram',9)  #calling the class and passing the arguments
print(a.function("chirping")) # calling the function of the class
print("the bird {} belongs to {}".format(a.name,a.__class__.speices)) # accessing the class varaible'''

'''
class Bird:
    def __init__(self):
        print('bird is ready')
    def wHoisThis(self):
        print('bird')
    def swim(self):
        print('swim faster')

class Penguin(Bird):
    def __init__(self):
        super().__init__()
    print('penguin is ready')
    def swim(self):
        print('swim faster')
    def run(self):
        print('run faster')

PEG = Penguin()
print(PEG.run())'''

'''
class Employee:

    def __init__(self,name,sal,id):
        self.name= name
        self.sal=sal
        self.id=id
    def details(self,expenditure):
        savings = self.sal-expenditure
        print('the total is',savings)

p_name= input('enter the name')          # giving inputs from user instead of declaring initially
s_sal = int(input('enter the salary'))
i_id =  int(input('enter the id'))

person = Employee(p_name,s_sal,i_id)      # passing the varaibles into the employee class 
person.details(2000)'''

# single inheritence#
'''class Marks:
    def __init__(self):
        self.m1 = int(input('enter the marks in physics'))
        self.m2 = int(input('enter the marks in maths'))
        self.m3 = int(input('enter the marks in chemistry'))
    def displaymarks(self):
        print('the marks in physics',self.m1)
        print('the marks in maths', self.m2)
        print('the marks in chemistry', self.m3)

class Result(Marks):

    def __init__(self):
        Marks.__init__(self)
        self.total = self.m1+self.m2+self.m3
        self.average = self.total/3
    def displaypercent(self):
        print('the total marks obtained are :',self.total)
        print('the average gained for the subjects :',self.average)

mark = Result()
mark.displaymarks()
mark.displaypercent()'''

# multi level inheritence#
'''class Marks:

    def __init__(self):
        self.m1 = int(input("Enter marks in Physics: "))
        self.m2 = int(input("Enter marks in Chemistry: "))
        self.m3 = int(input("Enter marks in Maths: "))

    def displayMarks(self):
            print("Marks in Physics: ", self.m1)
            print("Marks in Chemistry: ", self.m2)
            print("Marks in Maths: ", self.m3)

class Result(Marks):                   #derived class
    def __init__(self):
        super().__init__()                 # the class from which class inherits is parent or super class
        
        self.total = self.m1 + self.m2 + self.m3
        self.percentage = self.total / 3

    def displayResult(self):
            print("Total Marks: ", self.total)
            print("Percentage: ", self.percentage)

class Grade(Result):                    # derived class
    def __init__(self):
        super().__init__()
        if self.percentage > 80:
            self.grade = "A"
        elif self.percentage > 60:
            self.grade = "B"
        elif self.percentage > 40:
            self.grade = "C"
        else:
            self.grade = "Fail"

    def displayGrade(self):
        print("Grade: ", self.grade)

g = Grade()
g.displayMarks()
g.displayResult()
g.displayGrade() '''

#multiple inheritence
'''class Student:

    def __init__(self):
        self.name = input("Enter student name: ")
        self.rollno = input("Enter student roll number: ")

    def displayStudent(self):
        print("Student Name: ", self.name)
        print("Student Roll Number: ",self.rollno)

class Marks:
    def __init__(self):
        self.m1 = int(input("Enter marks in Physics: "))
        self.m2 = int(input("Enter marks in Chemistry: "))
        self.m3 = int(input("Enter marks in Maths: "))

    def displayMarks(self):
            print("Marks in Physics: ", self.m1)
            print("Marks in Chemistry: ", self.m2)
            print("Marks in Maths: ", self.m3)

class Result(Student, Marks):                            # derived class from classes student and marks
    def __init__(self):
        Student.__init__(self)
        Marks.__init__(self)
        self.total = self.m1 + self.m2 + self.m3
        self.percentage = self.total / 3

    def displayResult(self):
            print("Result of ", self.name, " - ",self.rollno)
            print("Total Marks: ", self.total)
            print("Percentage: ", self.percentage)

r = Result()
r.displayStudent()
r.displayMarks()
r.displayResult()  '''

