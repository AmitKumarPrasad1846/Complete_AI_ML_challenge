# fruits = ['apple','banana','cherry','grapes','papaya']
# 1- output for fruits[2]
# 2- output for fruits [-1]
# 3- output for fruits [:3]
# 4 - output for fruits[2:]
# 5- reverse the list

# LIST - store multiple elements in a single variable
# ordered collection of elements
# lists are mutable - (can change the value of list, add, remove)
# accessed by indexing or slicing
# list can store heterogeneous data - (value of different data type)
# list can store duplicate values

# Indexing is used for accessing single values only.
# slicing use for accessing multipe value. --- var[start : stop : step]

l1 = [1,2,3,4,5,6,7,8,9,10]
# print the value of 7 using indexing
# print the value from 2 to 6 using positive indexing
# print the value of 4 to 8 using negative index

l1 = [1,2,3,4,5,6,7,8,9,10]

# print the value of 7 using indexing (index 6)
print(l1[6])  # Output: 7

# print the value from 2 to 6 using positive indexing (index 1 to 5, as end is exclusive)
print(l1[1:6])  # Output: [2, 3, 4, 5, 6]

# print the value of 4 to 8 using negative index (indexes -7 to -2)
print(l1[-7:-2])  # Output: [4, 5, 6, 7, 8]


v2 = ['apple', 24, 'python', 88, 10, 67, 'a', 'hello']

print(v2[0:6:2])   # Output: ['apple', 'python', 10]
print(v2[0:4:2])   # Output: ['apple', 'python']

# modifying list item

l1 = ['python', 10, 20, 30, 'hello', 'list', 1, 2, 3]
print(l1)
l1[5] = 'abc'
print(l1)


# len() - length of the list - total no of elements
l1 = ['python', 10, 20, 30, 'hello', 'list', 1, 2, 3]
print(len(l1))


# HOW TO ADD AN ELEMENT IN A LIST??
# 1- append() - add a single element at the end of the list -- l2.append(value)
# 2- extend() - add more than one element at the end of the list -- list_name.extend([values])
# 3- insert - helps you insert a value at a specific index-
# listname.insert(position, value)

# 1- append() - add a single element at the end of the list -- l2.append(value)
l2 = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']
print(l2)
l2.append('d')
print(l2)

# 2- extend() - add more than one element at the end of the list -- list_name.extend([values])
l2 = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']
print(l2)
l2.extend([0, 'd', 'g', 'akhil', 'dns', 'time', 'maddy', 10])
print(l2)

# 3- insert - helps you insert a value at a specific index-
# listname.insert(position, value)
l2 = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']
print(l2)
l2.insert(2, 'hiiii')
print(l2)