#collections: Counter, namedtuple, orderedDict, deque

#Counter
#A container that stores elements as dictionary keys and their counts as dictionary values
#we can use counter on lists, string
from collections import Counter
a = "aaaaabbbbccc"

print("Counter")
myCount = Counter(a)
print(myCount)

print("\n")
print(myCount.keys())

print("\n")
print(myCount.values())

print("\n")
print(myCount.items())

#How many of the most common do you want to see 
print("\n")
print("Most common element")
print(myCount.most_common(1))
print(myCount.most_common(1)[0])
print(myCount.most_common(1)[0][0])

#Prints each key as many times as the counter
print("\n")
print("Prints each key as many times as the counter")
print(list(myCount.elements()))



#namedtuple
#Used for making a class, you can access elements by name rather than by index
#around the same memory footprint as a plain tuple instead of a class
from collections import namedtuple
print("\n")
print("namedTuple")
point = namedtuple('point', 'x,y')
pt = point(1,-4)
print(pt)
print(pt.x , pt.y)

#orderedDict
#just like an ordinary dictionary but they remember the order the items were stored in
#less relevant nowadays
from collections import OrderedDict
print("\n")
print("orderedDict")
myDict = OrderedDict()
myDict['a'] = 1
myDict['b'] = 2
myDict['c'] = 3
myDict['d'] = 4
print(myDict)


#defaultdict
#like a normal dictionary but it will have a default value if the key has not been set yet
from collections import defaultdict
print("\n")
print("default dict")
d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d['b'])
print(d['c'])




#deque
#A double ended queue used for adding and removing elements from both ends, efficiently
from collections import deque
print("\n")
print("Deque")
d = deque()

print("Appending")
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)

print("Popping")
d.pop()
print(d)
d.popleft()
print(d)

print("Clear")
d.clear()
print(d)

print("extending")
d.extend([1,2,3])
print(d)
d.extendleft([4,5,6])
print(d)

print("Rotating")
d.rotate(1)
print(d)























