# OPERATORS - symbols which are used to perform some operations .

# 1- Arithmetic Operators

# 2- Comparison Operators

# 3- Logical Operators

# 4- Assignment Operators

# 5- Membership Operators

# 1- ARITHMETIC OPERATORS - used to perform the mathematical calculation
# add , sub , mul , div , modulous , floor division , exponential

n1 = 89
n2 = 76
print(n1 + n2) #add
print(n1 - n2) #subtraction
print(n1 * n2) #multiplication


# division - /
# floor division - // - it will give the3 quotient in a whole number. 
a = 23
b = 3
print(a/b)
print(a//b)

# modulus operator - % -- return the remainder value

a = 17
b = 2
print(a % b)

# exponential operator - ** - give the exponential or power value

a = 7
b = 5
print(a**b)

a = 2
b = 3
print(a**b)

# comparision operator - used to compare two values.
# output will be a boolean value
# either 'True' or 'False'

# "==" equals to
# "!=" not equals to
# <>, >=, <=

a1 = 67
b1 = 90

print(a1==b1)
print(a1!=b1)
print(a1>b1)
print(a1<b1)
print(a1>=b1)
print(a1<=b1)

# LOGICAL OPERATORS -
# and - return true if both the statements are true
# or - return true if atleast one statement is true
# not - it will the reverse the output - true - false

# = assign
# += add ,aasign
# -= , *= , /=,//= , **=

a = True
b = False
print(a and b)
print(a or b)
c = a and b
print(c)
print(not c)

# This is single line comment.

"""
This is multi line comment.
"""

'''
this is also multiline comment.
'''
# Conditionals
age = 34
score = 67
turn = 3
if (age>=35) and score >=50 and turn<=5:
    print("qualified")

# Assignment operator - used to assign or give some value to a variable.
# 1. =
# 2. +=
# 3. -=
# 4. *=

var1 = 7
print(var1)

name = "komal"
print(name)

var1= 10
print(var1+10)

20

var1+=10
print(var1)
a = 20
a -=5     # a =  a-5
print(a)

# MEMBERSHIP OPERATORS - used to check whether a value is a member or a part of a list or not.
# in
# not in
# output is a boolean value - true or false

# Type casting - used to convert data type of one variable to another.
# variable_name = datatype(variable)
# int(), float(), str(), list(), tuple(), set()

# ex:1
p1 = 182.96
print(p1)
print(type(p1))
#ex:2
p2 = int(p1)
print(p2)
print(type(p2))
#ex:3
s1 = 34
print(s1)
print(type(s1))


# SEQUENTIAL DATA TYPES - when we have elements or values in a sequence, or in an ordered collection of elements .
# list
# tuple
# string

# LIST - store multiple elements in a single variable
# ordered collection of elements
# lists are mutable - (can change the value of list , add , remove)
# accessed by indexing or slicing
# list can store heterogeneous data - (value of different data type)
# list can store duplicate values

# ex:1
l1 = [10,12,'python',1,2,4,5,'hello',5,2]
print(l1)
print(type(l1))

# ex:2
# access the elements - indexing or slicing
l2 = [11,2,3,5,6,7,'hello','banana','python']
# access banana
# access value 6
# access value python

print(l2[-2])
print(l2[4])
print(l2[-1])
