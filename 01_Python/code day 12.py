# pass - does nothing - avoid the error
for i in range(1,11):
    pass



while True:
    print(2)
    if True:
        break
print(2)


# print the numbers from 1 to 15 and once you get 10 dont print anything
# print the number from 3 to 10 and once you get 7 skip that number

num = int(input())
while(num <= 0):
    print("enter positive number")
    num = int(input())

    if(num >= 0):
        break
print("number is: ", num)


# loop through a list and stop if "banana" is found
l1 = ['apple', 'guvava', 'papaya', 'watermelon', 'banana', 'grapes', 'berries']
for i in l1:
    if (i == 'banana'):
        break
    print(i)


# Print only even numbers from 1 to 10 using continue.
for i in range(1, 11):
    if (i%2!= 0):



# functions - used to perform soem task or it is named block of code you can call to do a task.

# '''
# syntax - 
# def finction_name():
#     body

# function_name() - function calling
# '''

# function without any parameter
def greet():            # function declaration
    print("hello")      # body
greet()                 # function calling

# Output:
# hello

# Function with parameters
def greet(name):
    print("hello", name)

n = input()
greet(n)
greet('sneha')
greet('karan')
greet('magesh')
greet('danish')
greet('salman khan')




# create a function whose task is to add 2 numbers - 
# first without parameters 
# with parameters

