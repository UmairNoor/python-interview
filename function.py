#Basic Function Code
# Write a functon code that return square number 
def square(number):
    return number ** 2 

result = square(5)
print(result)

#Create a functions that takes two parameters and return their sum
def sum(a,b):
    return a+b

final = sum(2,1)
print(final) 

#Function with Lambda 
cube = lambda x: x**2
print(cube(3))

#Function with args 
# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i**2)
#     return sum(args)

# print(sum_all(1,2,3,4))

import builtins  # Import Python's built-in functions

def sum_all(*args):
    return builtins.sum(args)  # Use the built-in sum()

print(sum_all(1, 2, 3, 4))  # Output: 10
