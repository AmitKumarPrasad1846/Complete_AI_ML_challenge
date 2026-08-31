d2 = {1: 'apple', 'a': 43, 'name': 'sucharitha'}
print(d2)
print(type(d2))


# access any value from dictionary
d2 = {1: 'apple', 'a': 43, 'name': 'sucharitha'}
print(d2['name'])

# change the value
d2 = {1:'apple','a':43,'name':'sucharitha'}
d2['name']='pragya'
print(d2)

# create a dictionary student and change the value for 2 data and print the updated data
student = {1:'Amit', 2:'Anil'}
student[1] = 'Roshan'
print(student)

# keys() - return all the keys in dict
# values() - returns all the values from dict
# items() - it will return both keys and values

student = {'name':'abc', 'age':21 , 'marks':78}
print(student.keys())
print(student.values())
print(student.items())


l1 = list(student.keys())
print(l1)
print(type(l1))


# items() - to get both keys and values from dict

student = {'name':'abc','age':21,'marks':78}
l3 = list(student.items())
print(l3)
print(type(l3))

# add multiple values in a dictionary-
# update() - multiple values or merge dictionaries
student = {'name':'abc', 'age':21 , 'marks':78}
print(student)
student.update({1:'hello' ,'id':101, 'abc':'python world'})
print(student)

# popitem() - remove the last inserted pair
student = {'name':'abc', 'age':21 , 'marks':78}
print(student)
student.popitem()
print(student)

# clear() - remove all the data from dictionary and it will return empty dict
student = {'name':'abc','age':21,'marks':78}
print(student)
student.clear()
print(student)

# pop() -- pops the particular data
student = {'name' : 'abc', 'age' : 21, 'marks' : 78}
print(student)
print(student.pop('age'))
print(student)

# 1- create a dictionary with name, age, city
# 2- update your city to "Bangalore"
# 3- print all the - (a) - keys, (b) - values
# 4- delete age from dictionary
# 5- add 2 new values in the dictionary
# 6- remove the last value from the dict and print new dict

# Step 1: Create a dictionary with name, age, city
student = {
    'name': 'Amit',
    'age': 22,
    'city': 'Indore'
}

# Step 2: Update your city to "Bangalore"
student['city'] = 'Bangalore'

# Step 3: Print all the keys and values
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

# Step 4: Delete age from dictionary
del student['age']

# Step 5: Add 2 new values in the dictionary
student['marks'] = 85
student['course'] = 'SQL'

# Step 6: Remove the last value from the dict and print new dict
student.popitem()  # Removes 'course': 'SQL'
print("Updated dictionary:", student)

# mam's answer

# d1 = {'name':'abc','age':20,'city':'mumbai'}
# d1['city'] = 'bangalore'
# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d1.pop('age'))
# print(d1)
# d1.update({1:101, 2:'hiiii'})
# print(d1)
# d1.popitem()
# print(d1)


l1 = list(student.keys())
print(l1)
print(type(l1))


# to get the value of dictionary-
# get() - access the values
# d1.get(key)
student = {'name':'abc', 'age':21, 'marks':78}
print(student.get('marks'))



# can i give list and tuple to values???
d1 = {'name':['sahil','anurag','mohan','roshan'],'age':21,'gender':'m'}
print(d1)

# access??
print(d1['name'])
print(d1['name'][2])



# Creating a dictionary with keys: name, age, and city
# 'age' and 'city' store tuples with 3 values each
student = {
    'name': 'Amit',
    'age': (21, 22, 23),
    'city': ('Indore', 'Bhopal', 'Ujjain')
}

# Answer 1: Accessing two values from the 'age' tuple
print(student['age'][0])  # Output: 21
print(student['age'][2])  # Output: 23

# Answer 2: Accessing one value from the 'city' tuple
print(student['city'][1])  # Output: Bhopal

# access 2 value from age and 1 value from city
print(d3['age'][1])
print(d3['city'][0])


# topics covered 

# introduction to python -- features
# variables
# data types
# operators
# type casting
# sequential and non sequential data types