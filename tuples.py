#Making Tuples, paranthesis are optional but the cammas are not
print("Making Tuples")
myTuple = ("max",28,"Buston")
myTuple2 = "David", 'Sara', 43
print(myTuple)
print(myTuple2)

#Making a Tuple using lists
print("\n")
print("Making a tuple from a list")
myList= [ 1,2,3 ,4]
myTuple =tuple(myList)
print(myTuple)

#Getting an element from Tuple
print("\n")
print("Getting an element from a tuple")
item = myTuple[0]
print(item)

#Getting the last itme
print("\n")
print("Getting the last item")
item = myTuple[-1]
print(item)

#Counting a specific element inside a tuple
print("\n")
print("Counting an item in Tuple|")
myTuple = ('a','p','p','l','e')
print(myTuple)
print("counting p")
print(myTuple.count('p'))

#Making a list out of a tuple
print("\n")
print("Make a list out of a Tuple")
myList = list(myTuple)
print(myList)

#Giving a variable to each item in tuple
print("\n")
print("Giving variable to items in tuple")
myTuple = 'Sajedeh', 'Arabali', 23
name, familyName, age = myTuple
print(myTuple)
print(f"name: {name}")
print(f"family name: {familyName}")
print(f"age: {age}")

#Unpacking tuples using *, i2 is a list
print("\n")
print("Unpacking tuples")
myTuple = (0,1,2,3,4)
i1, *i2, i3 = myTuple
print(i1)
print(i2)
print(i3)

#When is working with tuple more efficient than list?
    #tuple uses less memory which you can test by importing library sys and using the function sys.getsizrof()
    #more efficient to iterate(time) which you can test by importing timeit library and using the timeit.timeit(stat=tuplename, number=1000000)which will tell you the time it takes to run it 1million times

#Tuple dooes not support item assignment, you cannot change the value of any of the items after the tuple is written, unless you redefine the Tuple itself

#The rest are like list
