# OOPS - Object oriented programming System.
# it is related to real world entity, objests.


# functions are of two types - 
# 1. Procedural Object - the main focus on steps and instructions.
# 2. Functional Object - the main focus on functions.


# Why did OOPs appear at all??
# Before OOPs we were using Procedural and Functional Programming Style.
# Procedural Programming Style - It is a programming style where the main focus is on procedures (sequence of steps or instructions).
# Functional Programming Style - It is a programming style where the main focus is on functions which helps to organize our code in better way.

# But while working on large project or complex problem using these both language style was somewhere giving the problem, so tackle this problem the concept of OOPs came in scenario.


# OOPS -
# 1. Class - blueprint / temp.
# 2. Objests - real world things.

'''
Example - home
---------
|       |
|       |  -> design or blueprint - class
|   |   |
----|----
    |______ blueprint - object
'''

'''
Example - Car making company
           ________________
          |                |   -> design or blueprint - class
__________|                |_________
|       _____           ______    ---|----> Final Output - object
|______|     |_________|      |______|

'''


# OOPS - It is a programming style where we organize our code using objects (real world things ex - student, car, phones).
# we treat everything as objects.
# has data (attributes) - e.g - car - has color, model, speed.
# has functions (behaviour) - car - can start(), can stop(), car fuel().


# WHAT IS A CLASS?
# A class is like a blueprint or design which is used for creating objects.
# It tells what an object should have and what it can do(methods or behaviour).


# WHAT IS AN OBJECT?
# An object is the real thing or real world entity made from class.


# how to create a class --- keyword - class
# class class_name:
    # body - attributes /functions of objects
# create an object - object_name = class name
class Car:
    color = "black"
    speed = 50
    model = "swift"
    milage = 10

obj = Car()  # Object creating

# how to access any feature or function from inside the class - use object name -- object_name.method/feature_name
print(obj.color)
print(obj.model)

obj1 = Car()
obj1.color = "red"
print(obj1.color)
print(obj1.model)


# Create a class student which have three attributes and you have to print all three attributes.
class student:
    name = "Amit"
    score = "86%"
    address = "Indore"
stu = student()

print(stu.name)
print(stu.score)
print(stu.address)
# In the same class create one more object and change the value of any two attribute and again print the value for all the three attribute.
stu2 = student()
stu.last_name = "Kumar"

print()

# s = Student()
# print(s.name)
# print(s.age)
# print(s.gender)

# s1 = Student()
# s1.name = "anurag"
# s1.age = 22
# print(s1.name)
# print(s1.age)
# print(s1.gender)