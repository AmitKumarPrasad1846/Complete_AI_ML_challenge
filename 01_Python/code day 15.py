# CONSTRUCTOR ??
# A constructor is a special function inside a class that automatically runs whenever you create an object.
# constructor is always named as - __init__.
# It's purpose - set up(initialize) the object's data when it is first created.

'''
SELF ?
It is a way for the  class methods (functions inside class) to know which object they are working on.
'''
# Constructor
class student:
    def __init__(self, name, age, gender, marks):   # self is a parameter here. [initialize the data by writting]
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks # The value which we give to parameter is called argument.

    def show(self):
        print("name - ", self.name)
        print("age - ", self.age)
        print("gender - ", self.gender)
        print("marks - ", self.marks)

s1 = student('Harsha', 23, 'male', 55)
s2 = student('Sneha', 21, 'female', 58)
s3 = student('Anurag', 22, 'male', 59)
s2.show()
s1.show()
s3.show()

# Write a program to create a class with some 2 or 3 attributes and 2 methods inside it.
# Where first method is printing the value of only first attribute.
# And second method is printing the value of both the attributes and then create 2 objects.

class car:
    def __init__(self, model, color, milage):
        self.model = model
        self.color = color
        self.milage = milage
    
    def show_car(self):
        print("model - ", self.model)
        print("color - ", self.color)
        print("milage - ", self.milage)

c1 = car("ABC", "blue", 20)
c2 = car("EFG", "red", 15)
c3 = car("JKL", "black", 35)
c1.show_car()
c2.show_car()
c3.show_car()

# PILLARS OF OOPS -
# There are 4 main ideas or properties that make Object-Oriented Programming more powerful and useful:
# 1. Inheritance  
# 2. Encapsulation  
# 3. Polymorphism  
# 4. Abstraction


# Inheritance
# Inheritance is the process where one class can inherit or extract the properties and features of another class.
# The class which inherits the properties is called the child class or derived class.
# The class from which the properties are inherited is called the base class or parent class.
# Types of Inheritance:
# 1. Single Inheritance  
# 2. Multiple Inheritance  
# 3. Multilevel Inheritance  
# 4. Hierarchical Inheritance  
# 5. Hybrid Inheritance


# 1. Single-level Inheritance = one child class inherits from one parent class.
class Animal:
    def sound(self):
        print("animals can make sound")

class Dog(Animal):
    def bark(self):
        print("dog can bark")

d = Dog()
d.bark()
d.sound()