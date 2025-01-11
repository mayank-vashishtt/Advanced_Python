# data types which we define in other lang is called primitives like int 


# when we take input in python it always return string


# a = 12
# print(type(a))  

# b = [12, 13, 14]
# print(type(b))  


# object is a instance of class, like a individual person like you 
# object is called first class citizen in python
# no limit to space in python
# Can be assigned to variables
# Can be passed as arguments
# Can be returned from functions
# Can be stored in data structures
# Have their own properties and methods

#compiler -- > code --> machine code --> output 
# interpreter --> code --> output


"""
source.cpp -> [COMPILER] -> executable -> [EXECUTION]
- Converts entire code at once
- Creates executable file
- Faster execution
- Shows all errors at once
- Example: C++, Java
"""

#=== Interpreter Example (Python) ====#
"""
script.py -> [INTERPRETER] -> execution line by line
- Converts and executes code line by line
- No separate executable
- Slower execution
- Shows errors one at a time
- Example: Python, JavaScript
"""



"""
Compiler vs Interpreter:
1. Compilation Time:
   - Compiler: Entire code at once
   - Interpreter: Line by line

2. Execution Speed:
   - Compiler: Faster (pre-compiled)
   - Interpreter: Slower (real-time)

3. Error Detection:
   - Compiler: All at once
   - Interpreter: One at a time

4. Memory:
   - Compiler: More efficient
   - Interpreter: Less efficient
"""

# byte code > assembly code(add 0 1) > mid lvl lang(java) > high lvl lang(c#, python)



a =10 
print(isinstance(a, int))  # True

a = 1 + 2j 
print(isinstance(a, complex))  # True
 
# -8//3 = -3   -- one step lesser than 8/3
# -8/3 = -2.6666666666666665
# 8//3 = 2   -- one step lesser than 8/3
# 8%3 = 2  --- 8 - x * 3 (x * 3 lesser than 8)
# -8%3 = 1



"""
identifier   -- name of variable, function, class, module
a =10 
alphanumerical or _ or it should not start with number 

if def ma():
      returns a,b

then 
_ , c = ma()

mutuable and immutable 

immutable -- int, float, complex, bool, string, tuple
mutuable -- list, dict, set 


immutable -- id will be  not same
a=5
a=3 
id will be diff 

b = 2
c =2 
id will be same

del a 

everything is python is an object 
int is an object for eg 




"""


