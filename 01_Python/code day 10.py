# Conditional Statement - used to make decision based on some condition or criteria.
# - if (condition):
# - elif (condition):
# - else:


# Syntax-

# simple if
# if (condition):
    # run if condition is True

# if else.......................
# if (condition):
    # run if the condition is True
# else:
    # if is false then else

# if elif else............
# if (condition): 
    # run if the condition is true
# elif (condition):
    # run if the elif condition is true




# LOOPS - used to repeat a block of code multiple times.
# - Instead of writing the same code again and again, you tell python-
# keep doing the thing, until i say you stop.

# TYPES OF LOOPS -

#1- FOR LOOP- used when you know how many times you want to repeat something.
# for expression.......

# without loop -
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)

# with loop -
for i in range(1, 11):
    print(i)


# homework
# using for loop print the table of any number

n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

