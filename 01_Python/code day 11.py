n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Question
l1 = ['a','b','c','d','e','f','g']
# iterate and print every element from this list using for loop

for i in l1:
    print(i)

'''
while loop - repeat the block of code as long as the condition is true.

syntax - 
while condition:
    # body
    # update condition variable
'''

# count until i get n <= 5
n = int(input("enter no. = "))
while (n <= 5):
    print(n)
    n += 1

# W.A.P. that will keep asking for a positive num
num = int(input("Enter a number: "))
while num <= 0:
    print("enter positive number")
    num = int(input())
print("number is:", num)

# Programming Tasks (in green text):
# print the numbers from 1 to 15 and once you get 10 dont print anything
# print the number from 3 to 10 and once you get 7 skip that number
# take your input one string and write a program that will repeatly ask user to enter correct string until the user is oing

