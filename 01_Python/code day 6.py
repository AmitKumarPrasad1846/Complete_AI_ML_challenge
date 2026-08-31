# HOW TO DELETE AN ELEMENT FROM THE LIST-

# remove() - it will delete the first occurrence of the element from the list

l1 = [10,11,12,10,20,30,40,50]
print(l1)
l1.remove(10)
print(l1)

# clear() - it will remove all the element in the list and it will return empty list

l1 = [10,11,12,10,20,30,40,50]
print(l1)
l1.clear()
# empty list - list without any elements
print(l1)

# index() - return the index of first occurrence of an element

l1 = [25,37,10,11,12,10,20,30,40,50]
print(l1)
print(l1.index(30))
print(l1.index(10))
# result in an error- because this value is not present in my list
print(l1.index(90))

# create a list with 2 elements and then extend 4 elements and print the list
# insert one element at position 3 and again print the list.
l1 =[1,2]
print(l1)
l1.extend(['a','b','c','d'])
print(l1)

l1 = [25,37,10,11,12,10,20,30,40,50]
f1 = l1.index(10)
print(f1)
f2 = l1.index(10, f1+1)      # start searching after index1
print(f2)

# access the element in the tuples
t1 = (1,2,3,4,5,6,'a','b')
print(t1[-2])

t1 = (1,2,3,4,5,6,'a','b')
# print the value 2 
# print the value 6

print(t1[1])
print(t1[-3])

# index() - return the index of first occurrence of elements
t1 = (1,2,3,4,5,6,'a','b')
print(t1.index('b'))

# count() - return the number of times a value is occurring
t1 = (1,2,3,4,5,6,'a','b')
print(t1.count(1))

# typecast tuple - list and then list to tuple
t1 = (1,2,3,4,5,6,'a','b')
l1 = list(t1)
print(l1)
print(type(l1))
l1[2] = 'abc'
print(l1)
t1 = tuple(l1)
print(t1)

# length of the string - len()
s2 = "Amit"
print(len(s2))

# strip() - remove the spaces from the string from both the ends - start and end

s3 = "    hello python    "
print(s3)
print(s3.strip())

# strip() - remove the spaces from the string from both the ends - start and end
s3 = "    hello python    "
print(s3)
print(s3.strip())
# lstrip() - remove the spaces from left side
# rstrip() - remove the space from right side

# concatenation - joining of two strings -
s1 = "hello"
s2 = "world"
print(s1+s2)

# functions
# lower() - used to convert string into lower case
# upper() - used to convert string into upper case
# capitalize() - used to convert first letter - capital

s1 = "HELLO"
print(s1.lower())
s2 = "python"
print(s2.upper())
print(s2.capitalize())

# repetition - string*n(any number) - it will repeat that string n times

s1 = "hiii "
print(s1*2)
print(s1*5)

