'''
Ques 1 – Create two sets and perform the following operations on sets:
- Intersection of 2 sets
- Union of 2 sets
- Difference of 2 sets –
s1.difference(s2)
s2.difference(s1)

'''

s1 = {1, 2, 3, 4, 56, 7}
s2 = {2, 3, 4, 9, 8, 7}
print(s1.union(s2))         # Combines all unique elements from both sets
print(s1.intersection(s2))  # Shows elements common to both sets
print(s1.difference(s2))    # Elements in s1 but not in s2
print(s2.difference(s1))    # Elements in s2 but not in s1



# Ques 2 – Take a float as input and convert it to intege

inp = float(input("enter a number : "))
input = int(inp)
print(type (input))


# forward = backward -- palindrome

# Ques 3 - check whether a string is palindrome or not - 
# Palindrome String - It is a string that reads forward and backward same - string == reverse -- Palindrome

Palindrome = input("enter a word to check for Palindrome = ")
if Palindrome == Palindrome[ : :-1]:
    print(Palindrome, "is palindrome")
else:
    print("Not a palindrome")

# Ques 4 - Check whether a number is prime or not.

# num = int(input("Enter a Number : "))
# zero = 0
# if (num % 2 == zero):
#     print("Not a prime")
# elif (num == 2):
#     print("it is a prime no.")
# elif (num == 0):
#     print("try different no.")
# else:
#     print("prime no. found")
    
# Check whether a number is prime or not
num = int(input("Enter a Number: "))

if num <= 1:
    print("Not a prime number")
elif num == 2:
    print("It is a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("It is a prime number")


# Ques 5 - Check whether a given is armstrong or not.

# Armstrong number - It is a number that is equal to the sum of its own digits each raised to the power of the total number of digits.
# digit_1 ** n  + digit_2 ** n + digit_3 ** n + ......   -- where n = total digit

'''
For example
input - 153
digits ------- 3 digits  ->  1      5       3
total digits -------- 3
'''

arm_no = int(input("Enter a number for checking Armstrong no. = "))
arm_no_count = count(arm_no)
