# tupple -- created using ( )  -- it is immutable -- if we want to change the value then we have to first type cast.
# list -- created using [ ]  -- it is mutable.

# repetition - string*n(any number) - it will repeat that string n times

s1 = "hiii "
print(s1*2)
print(s1*5)

# 1 create a tuple with 5 elements and print the element which is at 3 position
# 2 create two strings and concatenate them
# 3 create a string and apply repetition 4 times
# 4 take on string as user input and reverse the string

# answer 1
tuple = ("a" , "b", "c", "d", "e")
print(tuple[2])

# answer 2
str1 = "Amit"
str2 = "Kumar"
print(str1 + " " + str2)

# answer 3
rep_str = "Amit"
print(rep_str*4)

# answer 4
user_input = input("Enter a string: ")
reversed_str = user_input[::-1]
print("Reversed string:", reversed_str)

# NON - SEQUENTIAL DATATYPE - elements are not stored in the sequence or elements are not arranged in a ordered way.

#    • set
#    • dictionary

# 1- Set - unordered collection of distinct(unique) elements

#    • it stores unique value - (no duplicate element is allowed)
#    • it is mutable (add or remove the element, we can't change the elements of set)
#    • {}

s1 = {1,2,3,4,5,6}
print(s1)
print(type(s1))

# Output
# {1, 2, 3, 4, 5, 6}
# <class 'set'>

s1 = {'a','b','c','a','b','c'}
print(s1)

# add() - adds a single element in a set.
s1 = {'a','b','c','a','b','c'}
print(s1)
s1.add('e')
print(s1)

# create a set and use add function to add an element in the set also check the data type of the set you created

set = {1,2,3,4,5,6,5,5,3,2}
set.add(7)
print(set)
print(type(set))

# update() - used to add multiple values in a set
# s1.update([values])

s1 = {1,2,4,5,6}
print(s1)
s1.update()

s2 = {14, 2, 4}
s2.update([1, 4, 5, 6])
print(s2)

# To remove element
# remove() - remove the element
# remove() - it will remove the element , if element not found it will return error
# s1.remove(value)
s1 = {1,2,4,5,6}
print(s1)
s1.remove(4)
print(s1)

# update will throw error if element not found
# a1.remove(10)
# print(s1)  

# discard() - remove an element , no error if element is not found

s1 = {1,2,4,5,6}
s1.discard(5)
print(s1)
s1.discard(23)
print(s1)
s1.remove(23)
print(s1)      # error


# pop() - remove a random element from the set

s1 = {1,2,4,5,6}
print(s1)
s1.pop()
print(s1)

{1, 2, 4, 5, 6}
{2, 4, 5, 6}

# clear() - remove all the values from the set

s1 = {1,2,4,5,6}
s1.clear()
print(s1)

# add elements in a set and remove duplicates.
# create one set and add 5 elements using set function then remove the element of your choice
# clear all elements from the set and print empty set
# s1= {1,True,False,0}      --- output??

# answer 1
s = set([1, 2, 2, 3, 4, 4, 5])
print(s)  # Output: {1, 2, 3, 4, 5}

# answer 2
s1 = set([10, 20, 30, 40, 50])  # Creating a set with 5 elements
print("Original set:", s1)

s1.remove(30)  # Removing element 30
print("Set after removing 30:", s1)

# answer 3
s1.clear()  # Removes all elements
print("Set after clearing:", s1)  # Output: set()

# answer 4
s1 = {1, True, False, 0}
print(s1)
# Output
# {0, 1}

# SET OPERATIONS --
#1 - UNION -- return the unique elements from both the sets
# 2- INTERSECTION -- common elements between 2 sets
# 3- Difference -- s1.difference(s1)-- only s1 elements not in s2
# s2.difference(s1)-- only s2 elementgs not in s1

s1= {1,2,3,4}
s2 = {5,6,2,3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))

# DICTIONARY - it is a collection of key value pair
# d1 = { 1 : 'python' , 2 : 34 , 'a': 'hello'}
# - each key is unique
# - keys are immutable
# - values can be of any data type
# - value are mutable
d1 = {'name':'anas', 'age':22, 'gender':'m'}
print(d1)
print(type(d1))



# create a dictionary with 4 values and check and print the data type
# take two sets and perform set operations 
# 1- union
# 2- s1.difference(s2)
# create a set then add 3 values using update function
# create a dictionary and access all the values of dictionary one by one

# 1.
d = {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}
print("Dictionary:", d)
print("Data type:", type(d))

# 2
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print("Union of s1 and s2:", s1.union(s2))
print("Difference s1 - s2:", s1.difference(s2))

# 3
s3 = set()
s3.update([10, 20, 30])
print("Set after update:", s3)

# 4
d2 = {'a': 100, 'b': 200, 'c': 300}
for value in d2.values():
    print("Value:", value)
