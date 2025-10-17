#Declaring a set, a set does not allow for duplicate items
print("Declaring a set")
mySet = {1,2,3,3,4,4,5,5,5,6,}
print(mySet)

#Making a set from a list using set function

#A set is unordered
print("\n")
print("String in set")
thisSet = set("Hello")
print(thisSet)

#Declaring an empty set, if you declare just an empty set when you get the type it will show you dictionary
print("\n")
print("Empty set")
empSet = set({})
print(type(empSet))

#Adding elements into a set
print("\n")
print("Add element")
mySet.add(8)
print(mySet)

#Removing elements from a set, discard removes element whithout giving an error if the element does not exist in the set, and pop removes with also returning the items
print("\n")
print("Remove element")
mySet.remove(8)
print(mySet)

print("Remove element v2")
mySet.discard(8)
print(mySet)

print("Remove element v3")
mySet.pop()
print(mySet)

#Emptying the set
print("\n")
print("Empty the set")
mySet.clear()
print(mySet)

#Looping through set with form
print("\n")
print("Looping inside set")
mySet = {1,2,3,4,5,6,7,8,9}
for i in mySet:
    print(i)
    
#finding an item inside the set
print("\n")
print("Finding item")
if 3 in mySet:
    print("Yes")
else:
    print("No")
    
#Union and Intesections
print("\n")

odd = {1,3,5,7,9}
even = {2,4,6,8}

print("Union")
u = odd.union(even)
print(u)

print("Intersection")
i = odd.intersection(even)
print(i)

#difference of two sets
print("\n")
print("difference of two sets")

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

d = setA.difference(setB)
print(d)

print("Difference of two sets v2 (symmetric difference)")
diff = setA.symmetric_difference(setB)
print(diff)

#Updating a set by adding the elemnets of the other set into it
print("\n")
print("Updating sets")
setA.update(setB)
print(setA)

#Updating a set by intersection

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

print("\n")
print("Intersection update")
setA.intersection_update(setB)
print(setA)

#Updating a set by difference, and off course we have symmetric difference update too

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

print("\n")
print("Difference update")
setA.difference_update(setB)
print(setA)

#calculate if setA is subset of setB( all the elements of our first set exist in the second set)

setA = {1,2,3,4,5,6}
setB = {1,2,3}

print("\n")
print("Is it a subset?")
print(setA.issubset(setB))

#Calculate if setA is a superset of setB(if the first set contains all the elements from the second set)
print("\n")
print("Is it a superset?")
print(setA.issuperset(setB))

#if both sets don't have any intersection
print("\n")
print("Is it a disjoint?")
print(setA.isdisjoint(setB))

#for copying you can use the copy function or the set function

#making an immutable set
print("\n")
print("Frozen set")
a = frozenset(setA)
print(a)