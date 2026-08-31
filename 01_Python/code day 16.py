# 2- Multilevel Inheritance - A class inherits from another class, and another class inherits from that derived class

# Grandfather class -> Father class -> Child class.

class car:
    def red(self):
        print("this is red car")

class car1(car):
    def blue(self):
        print("car is blue")

class car2(car1):
    def white(self):
        print("car is white")

c = car2()
c.red()
c.blue()
c.white()

# 3. Multiple Inheritence - There are more than one base class for a child class.

class pen:
    def red(self):
        print("this is red pen")

class pen1():
    def blue(self):
        print("pen is blue")

class pen2(pen, pen1):
    def yellow(self):
        print("pen is yellow")

p = pen2()
p.red()
p.blue()
p.yellow()


# 4. Hierarchical Inheritence - More than one child class will inherit from one parent class.

class pen:
    def red(self):
        print("color is red")

class gell_pen(pen):
    def blue(self):
        print("gell_pen is blue")

class ball_pen(pen):
    def yellow(self):
        print("ball_pen is yellow")

g = gell_pen()
g.red()
g.blue()

b = ball_pen()
b.red()
b.blue()

# 5- Hybrid Inheritance - Combination of two or more types of Inheritance
# eg - Singlelevel inheritance + multiple inheritance

class A:
    def fun1(self):
        print("single base class")
class B(A):
    def fun2(self):
        print("first child class")
class C:
    def fun3(self):
        print("print c")
class D(B, C):
    def fun4(self):
        print("print d")

d = D()
d.fun4()
d.fun3()

# 2- ENCAPSULATION - Keeping or wrapping up the data and functions together in one place (class) and hiding the details from outside
# - Its main purpose is to prevent the data or restrict the access
# - Encapsulation = putting data + functions together and hiding the details.

# How it is restricting the accsess?
# Access Modifiers - used give or restrict the access.
# 1. Public - freely available, can be accessed any where freely (inside or outside).
# 2. Proctected - accessed inside the same class and by derived class
#       - (_) single underscore variable name
# 3. Private - accessible only inside the class
#       - (__) double underscore variable name.

class Student:
    def __init__(self, name, aadharno):
        self.name = name   # Public Variable.
        self.__aadharno = aadharno   # Private Variable 
    
    def display(self):
        print(self.__aadharno)

o1 = Student('Nandana', 1234567)
o1.name
o1.__aadharno

o1.__aadharno     # error ?? - private variable can't be accessed outside the class


# create one class and implement a code for encapsulation
class Person:
    def __init__(self, name, aadharno):
        self.name = name
        self.__aadharno = aadharno  # private variable

    def get_aadharno(self):
        return self.__aadharno

    def set_aadharno(self, new_aadharno):
        self.__aadharno = new_aadharno

# Usage
p1 = Person("Amit", "1234-5678-9012")
print(p1.name)               # Accessible
print(p1.get_aadharno())     # Accessing private variable via getter