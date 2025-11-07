#Iterators are data types that can be used in a for loop
#Itertools functions: product, permutations, combinations, accumulate, groupby, and infinite iterators

#Cartesian product of input iterables.
from itertools import product
print("product: ")
a = [1,2]
b = [3,4]
prod = product(a,b)
print(prod)
print(list(prod))
print("\n")
print("product repeated:")
prod = product(a,b, repeat=2)
print(list(prod))

#All possible orderings of r elements.
from itertools import permutations
print("\n")
print("permutations: ")
a = [1,2,3]
perm = permutations(a)
print(list(perm))
print("\n")
print("permutations with only 2 numbers: ")
perm = permutations(a,2)
print(list(perm))

#All possible combinations of r elements (order doesn't matter).
#It won't work without specifying the length
from itertools import combinations, combinations_with_replacement
print("\n")
print("combination:")
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))
#Like combinations, but allows repeated elements.
print("\n")
print("combination with replacement: ")
combWR = combinations_with_replacement(a, 2)
print(list(combWR))

# takes an iterable (like a list) and returns a running result of applying a function cumulatively.
from itertools import accumulate
import operator
print("\n")
print("accumulate: ")
acc = accumulate(a)
print(list(acc))
print("\n")
print("accumulate multiplication:")
accM = accumulate(a, func=operator.mul)
print(list(accM))
print("\n")
print("accumulate max:")
accMax = accumulate(a, func=max)
print(list(accMax))


#It lets you group consecutive elements in an iterable that share a common key. But there’s a twist: it only groups adjacent items with the same key, not all matching items throughout the iterable.
from itertools import groupby
print("\n")
print("Groupby: ")
def smaller_than_3(x):
    return x<3
a = [1,2,3,4]
groupObj = groupby(a, key=smaller_than_3)
for key, value in groupObj:
    print(key,list(value))
    
    
#Infinite iterator generate values endlessly (until you stop them manually)
from itertools import count, cycle, repeat
#Generates consecutive numbers.
print("\n")
print("count:")
for i in count(10):
    print(i)
    if i == 15:
        break
#Repeats elements of an iterable forever.
print("\n")
print("cycle:")
count = 0
a = [1,2,3]
for i in cycle(a):
    print(i)
    count += 1
    if count == 10:
        break
            
#Repeats an item either infinitely or a fixed number of times.
print("\n")
print("repeat:")
for i in repeat(1,4):
    print(i)