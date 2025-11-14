#Java Script Object Notation

#Turning python dictionary into JSON object/string
import json
person ={
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "swimming", "singing"],
    "age": 28,
    "hasChildren": True,
    "children": [
        {
        "firstName":"Alex",
        "age": 5
        },
        {
        "firstName":"Bob",
        "age": 7
        }
    ]
}
print("Python to JSON")
personJSON = json.dumps(person, indent = 4, sort_keys= True) 
print(personJSON)

#Making a JSON file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
    
    
#Turning a Json format back into python dictionary
print("\n")
print("JSON to python")
person = json.loads(personJSON)
print(person)

#Reading a JSON file and turning it back into a usable Python object
print("\n")
print("Reading the JSON file as a python dictionary")
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
    
    
#Turning a Python object into a JSON string using a custom encoder.
print("\n")
print("Custom encoder")
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
user = User('Max',27)

def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name,
               'age':o.age,
               o.__class__.__name__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user,default = encode_user)
print(userJSON)

print("\n")
print("Custom encoder v2")
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return{'name': o.name,
                   'age':o.age,
                   o.__class__.__name__:True}
        return JSONEncoder(self,o)

userJSON = UserEncoder().encode(user)
print(userJSON)

#JSON to python
print("\n")
print("Turn user from JSON to python dictionary")
user = json.loads(userJSON)
print(user)
print(type(user))# This is a dictionary

#Turn JSON into an instance of the User class, rather than a plain Python dictionary.
def decode_user(dct):
    if User.__name__ in dct:
        return User(name = dct['name'], age = dct['age'])
    return dct
print("\n")
print("custom decoding")
user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)