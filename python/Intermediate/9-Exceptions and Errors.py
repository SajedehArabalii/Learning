#A syntax error occurs when the code does not conform to the rules and grammar of the programming language.
"""
Syntax Error
a = 5 print(a)
or
print(a))
"""

#TypeError in Python occurs when an operation or function is applied to an object of an inappropriate type. While Python is dynamically typed, it still expects compatible data types for specific operations. If the types are incompatible, a TypeError is raised.
"""
Type Error
a = 5 + '10'
"""

#An ImportError in Python occurs when the Python interpreter is unable to locate, load, or execute a module or a specific name within a module that you are trying to import.
"""
Import Error
import nonExistantModule
"""

#NameError in Python occurs when you try to use a variable, function, or object that has not been defined in the current scope (local or global).
"""
Name Error
a = b and b is not defined
"""

#File not found Error
"""
FileNotFound Error
f = open('nonExistantFile.txt')
"""

#ValueError in Python occurs when a function receives an argument of the correct type but an inappropriate or invalid value. Essentially, the type of the input is correct, but the value itself doesn't make sense for the operation being performed.

"""
Value Error
a = [1,2,3]
a.remove(4)
"""

#IndexError in Python occurs when you try to access an element in a sequence (like a list, tuple, or string) using an index that is outside the valid range of indices for that sequence. 
"""
Index Erorr
1 = [1,2,3]
a[4]
"""

#KeyError in Python occurs when you try to access a key in a dictionary (or other mapping types) that does not exist. This is a common exception and typically happens when the key you're looking for is not present in the dictionary.
"""
Key Error
dict = {'name': 'Max'}
dict['age']
"""





#Exception in Python refers to an error that occurs during the execution of a program, disrupting its normal flow. Instead of crashing the program, Python provides a way to handle these errors gracefully using exception handling mechanisms.

#In Python, raising an exception is a way to signal that an error or unexpected condition has occurred in your program. This is done using the raise keyword. When an exception is raised, the normal flow of the program is interrupted, and Python looks for an appropriate exception handler to deal with the error.

"""
Raising an Exception
x = -5
if x < 0:
    raise Exception('x should be positive')

or

x = -5
assert (x < 0), 'x is not positive'
"""

#Try and Except in Python are used for handling exceptions (errors) that may occur during the execution of a program. This allows your program to continue running smoothly instead of crashing when an error is encountered.

"""
Try and Except
try:
    a = 5 / 0
except:
    print("An Error happened")
    
or

except Exception as e:
    print(e)
    
or 

except ZeroDevisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print("Always runs, used mostly for cleanupsc")
    
"""

#Defining your own Exception
"""
Custom Exception

class ValueTooHighError(Exception):
    pass

def test-value(x):
    if x > 100:
        raise ValueTooHighError('Value too high')

try:
    test-value(200)
except ValueTooHighError as e:
    print(e)
"""

