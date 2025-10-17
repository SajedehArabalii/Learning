#Declaring a list
print("Declaring a list using []")
myList = ['banana', 'cherry', 'apples']
print(myList)

#Using for to print a list
print("\n")
print("Using for to print a list")
for i in myList:
    print(i)
    
#Using if to find an element in the list 
print("\n")
print("Using if ___ in to find an element in the list")
if 'banana' in myList:
    print("Yes")
else:
    print("No")
    
#Getting the length of the list
print("\n")
print("Getting length of the list using Len()")
print(len(myList))

#Add an item to the end of the list
print("\n")
print("Add an item to the end of the list using append()")
myList.append("lemon")
print(myList)

#Add an item to an specific place in the list
print("\n")
print("Add an item to an specific place in the list using insert()")
myList.insert(1,'blueberry')
print(myList)

#Reverse the list
print("\n")
print("Reverse the list using reverse()")
myList.reverse()
print(myList)

#create a new-list with the previous list sorted inside it
print("\n")
print("create a new list with the previous list sorted inside it using sorted()")
newList = sorted(myList)
print(newList)

#Sorting your list
print("\n")
print("Sorting your list" using sort())
myList.sort()
print(myList)

#Return and remove the last item
print("\n")
print("Return and remove the last item using pop()")
item = myList.pop()
print(item)
print(myList)

#Remove specific element from the list
print("\n")
print("Remove specific element from the list using remove()")
item = myList.remove('cherry')
print(item)
print(myList)

#Remove all elements from list
print("\n")
print("Remove all elements from list using clear()")
myList.clear()
print(myList)

#To make a list with the same element several times
print("\n")
print("Make a list with the same element several times using *")
myList = [0] * 5
print(myList)

#merging two lists
print("\n")
print("Merging lists using +")
myList2 = [1,2,3,4,5]
newList = myList + myList2
print(newList)

#slicing
print("\n")
print("Slicing the list from index 1 to index 5 using[1:5]")
myList = [1,2,3,4,5,6,7,8,9]
a = myList[1:5]
print(myList)
print(a)

print("Slicing from start to element 5 using [:5]")
a = myList[:5]
print(a)

print("Slicing from element 5 to the end using [5:")
a = myList[5:]
print(a)

print("Going from elements to another elements with steps using [::2]")
a = myList[::2]
print(a)

print("Reversing a list in another list using [::-1")
a = myList[::-1]
print(a)

#copying your list. we use the copy() in order to make sure that they are just not the same to list but instead two different lists with the same values and that changing one of them won't change the other one
print("\n")
print("Copying your list using copy()")
newList = myList.copy()
print(newList)

print("Copying your list v2 using list()")
copyList = list(myList)
print(copyList)

print("Copying your list v3 using slicing")
cpyList = myList[:]
print(cpyList)

#list comprehension
print("\n")
print("Copying and altering the list in the same line")
comp = [i*i for i in myList]
print(comp)
