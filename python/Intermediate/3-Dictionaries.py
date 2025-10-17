#Declaring a dictionary
print("Declaring a dictionary")
myDict = {
    'name':'Sajedeh', 'age' : 23, 'city': 'Sari'
    }

print(myDict)

#Printing a value from dictionary
print("\n")
print("Printing a value from dictionary")
value = myDict['name']
print(f"name is {value}")

#Giving the dictionary a new key and value, we can use the same thing to change the value of an existing key
print("\n")
print("giving the dictionary a new key and value")
myDict['email'] = 'arabalisajedeh@gmail.com'
print(myDict)

#Removing a key from the dictionary
print("\n")
print("Removing a key from dictionary")
del myDict['email']
print(myDict)

print("Removing a key from dictionary v2")
myDict.pop('city')
print(myDict)

#Check if the key is inside the dictionary
print("\n")
print('if key inside dictionary')

if 'name' in myDict:
    print('yes, it was found')
else:
    print('no , could not find it')
    
    
print('if key inside dictionary v2')
try:
    print(myDict['name'])
except:
    print('error')
    
#looping through a dictionary
print("\n")
print('Looping through a dictionary')

print("Looping through the keys:")
for key in myDict:
    print(key)
    
print("Looping through the values:")
for value in myDict.values():
    print(value)
    
print("Looping through both")
for key, value in myDict.items():
    print(f"{key} : {value}")
    
#copying a dictionary so that modifying does not change the original one, so we can use the copy function just like the list, or the dict function

#merging two dictionaries the update method
print("\n")
print("merging dictionaries using update method")
myDict = {'name':'Sajedeh', 'age':23, 'email':'sajedeharabali@gamil.com'}
myDict2 = {'name':'Mary', 'age':22, 'city':'Boston'}
print(myDict)
print(myDict2)
myDict.update(myDict2)
print("new updated function",myDict)

#we cannot use list as keys in dictionaries but we can use tuple as a key in dictionary




    