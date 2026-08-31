#google collab link
#https://colab.research.google.com/drive/1BG-00S-mp3PWGR5g5WHQiCZO8OauektE?usp=sharing#scrollTo=QpSCkmTY80B7


# create one variable which will take first name as user input
# create another variable which will take second name as user input
# print both the variables in single line

f_name = input("your first name:")
s_name = input("your second name:")

print(f_name, s_name)

'''

DATA TYPES - It is the type of data a variable have
- Numeric - int, float, complex
- Text - string 
- Boolean

How to check the datatype?
type( ) - used for checking datatype.

Numeric Data types - everything related to numbers

Categories of Numeric datatypes

Integer - All the whole numbers - int

Float - all the decimal numbers - float

Complex - ecpression - a + bj - 3 + 4j, 9 + 1j - Complex

'''

v1 = 1.2
print(type(v1))

v2 = 6 + 9j
print(v2)


#Text datatype - string - a sequence of character which is enclosed in single, double or triple quotes. - str()
n1 = "hello world"
print(type(n1))

n2 = 5.67
n3 = "9.99"
n4 = "4.5"
n5 = "56"
print(type(n2))
print(type(n3))
print(type(n4))
print(type(n5))

#Indentation error - Blank space or tab
print()

#Boolean Datatype - It is datatype which has 2 Values - True , False - Bool
a = True
print(a)
print(type(a))

b = False
print(b)

m1 = 78
m2 = 87
c = m1==m2
print(c)
print(type(c))

'''

OPERATORS - symbols which are used to perform some operations .
1- Arithmetic Operators
2- Comparison Operators
3- Logical Operators
4- Assignment Operators
5- Membership Operators

'''

# 1- ARITHMETIC OPERATORS - used to perform the mathematical calculation
# add , sub , mul , div , modulous , floor division , exponential

n1 = 89
n2 = 76
print(n1+n2)  # add
print(n1-n2)   # subtract
print(n1*n2)   # multiplication

# div - (/) , floor division - (//)
# floor division - it will give the quotient in a whole number
a = 23
b = 3
print(a/b)
print(a//b)

# modulus operator - % -- return the remainder value
a = 17
b = 2
print(a%b)

# exponential operator - ** -give the exponential or power value

a = 7
b = 5
print(a**b)

a = 2
b = 3
print(a**b)

a = 4
b = 3
print(a**b)

'''

2- COMPARISON OPERATORS - used to compare the values.
- output will be a boolean value - true or false

'''

# comparison operators -
a1 = 67
b1 = 90
 # == - equals to
 # != not equals to
 # <>, >=,<=
print(a1==b1)
print(a1!=b1)
print(a1>b1)
print(a1<b1)
print(a1>=b1)