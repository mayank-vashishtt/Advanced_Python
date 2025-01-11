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