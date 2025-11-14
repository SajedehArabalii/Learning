#The random module in Python provides functions to generate pseudo-random numbers and perform random operations like shuffling, sampling, or choosing elements.
import random

#A random float in range 0 to 1
a = random.random()
print("random random")
print(a)

#For a specific range (float)
print("\n")
print("random uniform")
b = random.uniform(1,10)
print(b)

#For a specific range (integer)
print("\n")
print("random randint")
c = random.randint(1,10)
print(c)

#For specific range but upperbound is not included (int)
print("\n")
print("random randrange")
d = random.randrange(1,10)
print(d)

#generates a random floating-point number drawn from a normal (Gaussian) distribution with mean 0 (Mu) and standard deviation 1 (Sigma).
print("\n")
print("random normalvariate")
e = random.normalvariate(0, 1)
print(e)

#Picks a random element from the list
print("\n")
print("random choice")
myList = list("ABCDEFGH")
a = random.choice(myList)
print(a)

#Picks several random elements from the list
print("\n")
print("random choices")
b = random.choices(myList,k=3)
print(b)

#Picks several unique elements
print("\n")
print("random sample")
c = random.sample(myList, 3)
print(c)

#Shuffles elements int helist
print("\n")
print("random shuffle")
random.shuffle(myList)
print(myList)

#Initializes the random number generator with a fixed starting value x, ensuring reproducible random results across runs.
print("\n")
print("random seed")
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))


#Provides secure random number generation for cryptography and sensitive data like passwords or tokens.
import secrets

#Returns a secure random integer between 0 and 9.
print("\n")
print("secrets randbelow")
a = secrets.randbelow(10)
print(a)

#Generates a secure random integer between 0 and 15 using 4 random bits.
print("\n")
print("secrets randbits")
b = secrets.randbits(4)
print(b)

#Securely selects and returns one random element from List
print("\n")
print("secrets choice")
c = secrets.choice(myList)
print(c)


#provides fast, efficient tools for numerical computing, especially with arrays and matrices.
import numpy as np


#Creates a NumPy array of 3 random floating‑point numbers between 0 and 1, drawn from a uniform distribution.
print("\n")
print("numpy random rand 3")
a = np.random.rand(3)
print(a)
print("\n")
print("np random rand 3 * 3")
a = np.random.rand(3,3)
print(a)

#Returns a random integer between 0 (inclusive) and 10 (exclusive).
print("\n")
print("numpy random randint")
b = np.random.randint(0,10)
print(b)
print("\n")
print("numpy random randint 3")
b = np.random.randint(0,10,3)
print(b)
print("\n")
print("numpy random randint 3 * 3")
b = np.random.randint(0,10,(3,3))
print(b)


#Randomly reorders the rows of the array in place, changing their order but not the elements within each row.
print("\n")
print("numpy random shuffle")
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)

#
print("\n")
print("numpy random seed")
np.random.seed(1)
print(np.random.rand(3))
np.random.seed(1)
print(np.random.rand(3))