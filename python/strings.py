#declaring a string
print("Declaring a string")
myString = "Hello world"
print(myString)

#Multy line string
print("\n")
print("Multy line string")
myString = """Hello dear
welcome"""
print(myString)

#String is a list of letters, so you can get a specific letter or character just like a list
print("\n")
print("Getting a specific letter")
print(myString[0])

#We can use slicing in strings
print("\n")
print("Slicing")
substring = myString[1:5]
print(substring)

#Connecting strings together
print("\n")
print("Connecting strings")
greeting = "Hello"
name = "Sajedeh"
sentence = greeting + " " + name
print(sentence)

#We can connect strings using fstring, more concise and less confusing
print("Another way of printing strings")
print(f"{greeting} {name}.")

#Going through letters of the string
print("\n")
print("Going through characters of a string")
for i in greeting:
    print(i)
    
#We check if a character is inside a string using an if statement

#Getting rid of unwanter=d spaces
print("\n")
print("Stripping spaces")
greeting = "    Hello    "
print(greeting)
greeting = greeting.strip()
print(greeting)

#Uppercase and lower case strings
print("\n")
print("Uppercase: "+greeting.upper())
print("Lowercase: "+greeting.lower())

#Check if string starts with a specific character
print("\n")
print("Startswith: ")
print(greeting.startswith("Hel"))
print("Endswith:")
print(greeting.endswith("llo"))

#finding a character
print("\n")
print("Finding a character")
print(greeting.find("o"))

#Count the number of a specific character
print("\n")
print("Count a character in string")
print(greeting.count('l'))

#Replacing a part of the string
print("\n")
print("Replaceing:")
print(greeting.replace('ello', 'i'))

#Turning a string to a list, in the () the default argument is a space, but you can change it to other things, and it uses it to split the string to the list
print("\n")
print("Turning a string to a list")
myString = "How are you doing?"
myList = myString.split()
print(myList)

#Convert list to string
print("\n")
print("Turn list to string")
newString = ' '.join(myList)
print(newString)

