# Lecturer [ Bhuvan ]
'''

Question 1

1. Create a class named student and inside the class, create a function named fun1.

2. fun1 -> Should accept the user input and return the value.

3. Create another function named message() -> This function should print the value of the user input.

'''

# method 1
# here we will be calling the variable directly inside the message - which will surpass the return keyword. 
class Student:
    def fun1(self):
        self.data = input("enter a word: ")
        return self.data
    def message(self):
        print("You have entered: ", self.data())

st1 = Student()
st1.fun1()
st1.message()

# Method 2
# here rather calling the variable directly i.e. { self.data } we are calling the whole function i.e. {self.fun1} so that we can make the use of the return keyword.
class Student1:
    def fun1(self):
        self.data = input("enter a word: ")
        return self.data
    def message(self):
        print("You have entered: ", self.fun1()) 
        #here we have called the function beside calling the variable

st2 = Student1()
st2.fun1()
st2.message()



'''

Question 2

Create a class named Super and inside th4e class define a method fun1()

Inside the fun1, print the message "This is function 1 in super class"

'''

class Super:
    def fun1(self):  # --- this "def" is called method.
        print("This is function 1 in super class.")
obj = Super()
obj.fun1()

# In continution of the same above question.

'''

Create another class name Modified_Super, Inherit the Super class.

Inside the modified_super create a function fun1 and print "This is function 1 in Modified_Super"

Create another function fun2 - > print "This is function 2 inside Modified_Super"

'''

class Super:
    def fun1(self):
        print("This is function 1 in super class.")

class Modified_super(Super):
    def fun1(self):
        super().fun1() 
        #--- super() will get the complete output of the fun1 from super class.
        print("This is function 1 inside modified super")

    def fun2(self):
        print("This is function 2 inside modified super")

obj2 = Modified_super()
obj2.fun1()
obj2.fun2()



# Abstraction ->
'''

1. Create an abstract class named Device with abstract method start.

2. Creae 2 classes whose are inherited from the device.

3. Laptop, Mobile -> and complete the start method.

'''
# for using abstract method we have to first create a method named start.
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def start(self):
        pass

class Laptop(Device):
    def start(self):
        print("Hello guys")

class Mobile(Device):
    def start(self):
        print("Mobile Started")

    def hello(self):
        print("Device saying Hello")

device = Laptop()
device.start()

device2 = Mobile()
device2.start()
device2.hello()


'''

                            Polymorphism
              ____________________|___________________
              |                                       |
    Compiletime Polmorphism /           Runtime Polymorphism /
    Method overloading                  Method Overriding
-------------------------------------------------------------------
    class Mclass:                 |     class Mclass:
       def add(self, a, b):       |        def add(self, a, b):
          print(a + b)            |           print(a + b)
       def add(seld, a, b, c):    |        def add(self, a, b):
          print(a + b + c)        |           print("Hiiiiii")
                                  |
    obj = Mclass()                |     obj = Mclass()
    obj.add(10, 20, 30)           |     obj.add("Hiiiiii")


But in python the method overloading is not supported.
Whenever we try to do overloading the does overriding.

'''
'''

1. Create a abstract calss shape with an abstract function area.
2. Create two child class of shape -> Circle, Rectangle and complete the area method().

'''
'''

class Myclass1:
    def add(self, a, b):
        print(a + b)
    def add(self, a, b, c):
        print("Hi")

obj = Myclass1()
obj.add(1, 2, 3)

'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("Area of the Circle is:", 3.14*self.radius**2)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Area of the Rectangle is:", self.length*self.width)

c1 = Circle(5)
c1.area()

r1 = Rectangle(10,5)
r1.area()

# Few more questions.

'''

# Demonstrate multiple inheritance with Teacher and Mentor classes
# Guide as a child class and inherite the methods of parent classes
# show()

'''
# Answer
'''

# Create a abstract class Ride with a abstract method calculate fare()
# Create 2 inherited classes from the abstract class like Bus
# And Car and complete the method calculate_fare()
# For bus per kilometer fare is 5 rupees
# For Car per kilometer fare is 20 rupees

'''
# Answer
'''

# Design a Student class with private attribute marks
# marks should be a list of marks
# create a method cal_grade() and calculate the grade of the student
# A, B, C, D, F

'''
# Answer
'''

# Show hierarchial inheritance with Vehicle class as parent -> will have a method start()
# Child classes will be Car, Bike, Bus -> create atleast one method in every child class

'''
# Answer
'''

# Create a class Bank and 2 methods withdraw and deposite, check_balance
# take bank balance from user and make that private

'''
# Answer