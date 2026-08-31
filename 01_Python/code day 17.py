# 3 Polymorphism - It means same function or method name behave differently depending on the object.
# Poly + morphism -- Poly (many) + morphism (form) === many form

# Types - Method overloading and Method Overriding

# METHOD OVERLOADING?
# same method name but different numbers or types of parameters
# In python method overloading is not supported , if we are trying to do
# overriding will be done

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

c = Calculator()
c.add(4, 5, 6)
c.add(11, 10)  # This is method over loading.
c.add(4, 6)

# overloading ---> overriding
# We were try to do method averloading but it results in overriding.

class Calculator1:
    def add(self, a, b, c):
        return a + b + c

c = Calculator1()
c.add(4, 5, 6)
c.add(4, 6, 7)
c.add(11, 10, 12)

class Calculator2:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
    def add(self, a, b, c, d):
        return a + b + c + d

c1 = Calculator2()
c1.add(2, 4, 5, 6)

# METHOD OVERRIDING -
# same method name, same parameters, but defined in child class.
# when a child class has a method same as a method in the parent class, and it changes its behaviour.

class father:
    def phone(self):
        print("To make calls")

class Son(father):
    def phone(self):
        print("To play games")

s=Son()
s.phone()

# super() - It is a built in function, used inside a class to call a method from print(Super) class.

class father1:
    def phone(self):
        print("To make calls")

class Son1(father1):
    def phone(self):
        super().phone()
        print("To play games")

s=Son1()
s.phone()


# create a code to demonstrate method overriding and also use super().

class car:
    def color(self):
        print("speed is 300KM/hr")

class supercar(car):
    def color(self):
        super().color()
        print("speed is 350 KM/hr")

car = supercar()
car.color()

'''

Encapsulation - wrapping up the data in one place i.e. class
-----------------------------------------------------------------------------------------------------

4 Abstraction - It means showing only the necessary or relevant details and hiding the implementation or irrelevant details from the user.

Abstraction is not directly suported in python
So we need to take help from some module/libraries-

-----------------------------------------------------------------------------------------------------
Abstract Classes - Classes that can't be instantiated(cant be created)
it has abstract method inside it
can also have normal methods(concrete methods)

Abstract method - declared using @abstractmethod
it only have definition , do not have any body

-----------------------------------------------------------------------------------------------------
abc - abstract base class - it is a module
ABC - absctract class

-----------------------------------------------------------------------------------------------------

Encapsulation is for hiding coding complexity and increasing data security

Abstraction is for hiding designing logic.

'''

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("car can start with key")

class Bike(Vehicle):
    def start(self):
        print("bike can start with self")

c = Car() 
b = Bike()
c.start()
b.start()