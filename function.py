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
import builtins  # Import Python's built-in functions
def sum_all(*args):
    return builtins.sum(args)  # Use the built-in sum()

print(sum_all(1, 2, 3, 4))  # Output: 10

#Function with yeild 
def even_generator (limit):
    for i in range(2,limit+1,2):
        yield i 

for num in even_generator(10):
    print(num)
