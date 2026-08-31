# Sequential datatype:

# A Sequential datatype is a container that keeps items in a specific order so you can access them by their position
# Key properties
#1. Ordered :
#2. Indexable :
#3. Iterable :
#4. Slicable

# Two kinds :
# Mutable : that can be changed
# Immutable : can't change

# types of sequential datatype
#1. list
#2. tuple
#3. string
#4. range

# Types of Sequential Datatypes
# - List
# - A list is a mutable sequence that can hold any data type
# - Ordered
# - Allows duplicates
# - Tuple
# - String
# - Range

# Tuple
# - A tuple is an immutable sequence — once created, you can't change it
# - Ordered
# - Immutable
# - Allows duplicates
# - Faster than list

# range :

# range is an immutable sequence of number -- often used in loops
# efficient - does store all numbers generates number when needed

# used for iteration in looping concept
# immutable -- cant change after creation

r1 = list(range(1, 6))
print(r1)

# i want to generate numbers from 2 to 10 and skip = 2 -> 2,4,6,8


str1 = "hello world"
pos = 6
new_text = str1[:pos] + "python" + str1[pos:]
print(new_text)


name = "payal"
greeting = "hello {}"
new_text = greeting.format(name)
print(new_text)


str1 = "hello world"
new_text = str1[:6] + "python " + str1[6:]
print(new_text)
str1[:6] + "python "

# dictionary ->
# a dictionary stores data as a key value
# unordered
# mutable
# key must be unique and immutable
# value can be any data type and duplicates are allowed

