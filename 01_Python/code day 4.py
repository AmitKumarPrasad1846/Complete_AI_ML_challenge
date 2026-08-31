# indexing and slicing
l1 = [10, 20, 30, 40, 50, 60, 70]
print(l1[3])
print(l1[-4])

# let's make other list
# slicing - accessing more than elements based on their index-
# listname[start index:stop index:step]
# step - gap between numbers
l2 = ['apple', 24, 'python', 88, 10, 67, 'a', 'hello']
print(l2[2:6])
print(l2[-2:-4:-1])

l2 = ['apple', 24, 'python', 88, 10, 67, 'a', 'hello']
print(l2[-2:4:-1])

l2 = ['apple', 24, 'python', 88, 10, 67, 'a', 'hello']
print(l2[-5::-2])

l2 = ['apple', 24, 'python', 88, 10, 67, 'a', 'hello']
print(l2[-2:-5:-2])

# fruits = ['apple','banana','cherry','grapes','papaya']
# 1- output for fruits[2]
# 2- output for fruits [-1]
# 3- output for fruits [:3]
# 4 - output for fruits[2:]
# 5- reverse the list 

fruits = ['apple','banana','cherry','grapes','papaya']
#answer 1
print(fruits[2])

#answer 2
print(fruits[-1])

#answer 3
print(fruits[:3])