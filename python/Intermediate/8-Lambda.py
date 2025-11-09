# Lambda function : small one line anonymous function that is defined without a name 
# Lambda arguments : expression
#It is used when you want a simple function that is used only once in your code or as an argument in other functions


#Example of Lambda
print("Add10 lambda function:")
add10 = lambda x: x + 10
print(add10(5))
"""
It is the same as writing

def add10(x):
    return x + 10

"""

#Another example
print("\n")
print("Multiplication Lambda function:")
mult = lambda x,y: x * y 
print(mult(2,3))


#Sorted with lambda as argument
print("\n")
print("Sort by second value:")
points2d = [(1,2), (15,1), (5,-1), (10,4)]
pints2dSorted = sorted(points2d, key=lambda x:x[1])
print(points2d)
print(pints2dSorted)

print("\n")
print("Sort by sum of 2 values:")
points2dSorted = sorted(points2d, key=lambda x:x[1] + x[0])
print(points2d)
print(points2dSorted)


#map with lambda as argument, map(func, seq)
print("\n")
print("Multiply by 2 using map:")
a = [1,2,3,4,5]
b = map(lambda x: x * 2, a)
print(list(b))

"""
You can do it using list comprehension
b = [x*2 for x in a]
"""

#filter(func,seq)
print("\n")
print("Filter even numbers:")
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2 == 0, a)
print(list(b))

"""
Can also be done with
b = [x for x in a if x%2 == 0]
"""

#reduce(func,seq)
from functools import reduce
print("\n")
print("Multiply all elements using product:")
a = [1,2,3,4,5,6]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)