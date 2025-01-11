# iteration protocol 

# a = "mayank"

# for i in a: 
#     print(i)

"""
#iterable -- list, tuple, dict, set, string


iterable : datastructure with atomic elements  which can be iterated over 
iterator : variable used to store those atomic elements like i here in above example 
iteartion block : entire body of the loop 


for i in 10: 
    print(i) -- not iterable 


for i in range(10): 
    print(i)   -- iterable as it creates a list of 10 elements will print 0 to 9


if i have an iterable condition avaible then i will go with for loop 
if i know the exact number of iterations then i will go with while loop




a = "mayank "

it = iter(a)

print(it) //<str_ascii_iterator object at 0x1046edff0>


next(it)  # m
next(it)  # a
next(it)  # y
next(it)  # a
next(it)  # n
next(it)  # k
next(it)  #  -- StopIteration



print(iter(10))  # TypeError: 'int' object is not iterable


for i in range(1,11):
    print(i)  # 1 to 10

    
for i in range(1,11,3):
  print(i)  # 1, 4, 7, 10

  
range(5.5)  # TypeError: 'float' object cannot be interpreted as an integer


def sheldon_knock(name):
  print("knock knock knock", name)
  print("knock knock knock", name)
  print("knock knock knock", name)

sheldon_knock("shivank")


def random(a,b):
  print("a = ", a)
  print("b = ", b)

random(2,3) # a = 2, b = 3
random(b =2, a = 3) # a = 3, b = 2


def x(a,b):
  pass
x(a=3, b=4) // no output

def random(a,b):
  print(a+b)

random(10) # TypeError: random() missing 1 required positional argument: 'b'


def random(a,b=4):
  print(a+b)

random(10) # 14


def addition(a, b):
  print(a+b)


ans = addition(3,4)
print(ans) # None as no return type is there



def addition(a, b):
  return a+b

ans = addition(3,4)
print(ans) # 7



a = ["shivank",1,print,3.4,"python"]
print(a[2]) // <built-in function print>



a = ["shivank",1,print,3.4,"python"]
print(a[2]("shivank"))  # shivank None


a = ["shivank",1,sum,3.4,"python"]
print(a[2]) # <built-in function sum>

a = ["shivank",1,sum,3.4,"python"]
print(a[2:4]) # [<built-in function sum>, 3.4]


a = ["shivank",1,sum,3.4,"python"]
print(a[-3:1:1])  // []

List a: ["shivank", 1, sum, 3.4, "python"]

Start index -3: This refers to the third element from the end, which is sum.
Stop index 1: This refers to the second element from the start, which is 1.
Step 1: This means we are moving forward one step at a time.


In Python, slicing with a positive step (1) requires the start index to be
 less than the stop index. Here, -3 (which is equivalent to index 2) is 
 greater than 1, so the slice returns an empty list.


 a = ["shivank",1,sum,3.4,"python"]
print(a[-3:1:-1])  # Output: [<built-in function sum>]


a = ["shivank",1,sum,3.4,"python"]

print(max(a)) // TypeError: '>' not supported between instances of 'int' and 'str'


a = ["a","b","c"]
print(max(a)) // c

a = ["a","b","c", "A", "D", "z", "m"]
print(min(a)) # A

a = ["a","b","c", "A", "D", "z", "m"]
print(max(a)) # z


print([1,2,3] + [4,5,6]) # [1, 2, 3, 4, 5, 6]  


print([1,2,3] -[4,5,6]) # TypeError: unsupported operand type(s) for -: 'list' and 'list'


a = ["shiv","sziv", "a" , "zaaa"]
c = max(a)
print(c) # zaaa


print([1,2,3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]




a = [[1,2],[3,4]]
print(a[0]) # [1, 2]
print(a[0][0]) # 1



a = [1,2,3,4,5]
print(id(a)) # 140067366366784


a = [1,2,3,4,5]
a.append([1,2,3])
a.extend([11,22,33])
print(a)  # [1, 2, 3, 4, 5, [1, 2, 3], 11, 22, 33]
print(a.pop())
print(a)  # [1, 2, 3, 4, 5, [1, 2, 3], 11, 22]
print(a.pop(1)) # 2
print(a) # [1, 3, 4, 5, [1, 2, 3], 11, 22]
a.remove(4)
print(a) # [1, 3, 5, [1, 2, 3], 11, 22]
print(6 in a) # False



a = (1,2,3,4)
a[0] = 23  # TypeError: 'tuple' object does not support item assignment

a= (10,)
type(a) # tuple

a = (10)
type(a) # int



def foo():
  return 1,2,3

bar = foo()
type(bar) # tuple

a,b,c = foo() # 1,2,3


a,b = [1,2]
print(a) # 1


a = 1,2,3 # tuple




a = 1
b = 2
a,b = b,a

print(a,b) # 2,1


a = (1,2,3) + (4,) // (1,2,3,4)

a = (1,2,3) + (4) // TypeError: can only concatenate tuple (not "int") to tuple


a = (1,2,3)

a += (5,)
print(a) # (1, 2, 3, 5)


"""


