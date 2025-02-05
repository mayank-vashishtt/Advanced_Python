# OOPS

""" 
you should know to paradigm of programming language one is OOPS and other is functional programming



Encapsulation: giving this together inside a class - like methods and properties 

Abstraction : idc how functions work 
Abstraction in Python is a concept in object-oriented programming (OOP) that 
hides the internal implementation details of an object and only exposes the necessary 
and relevant functionalities. This allows the user to interact with the object without needing to understand the complexities behind it.

Inheritance:
Inheritance is a mechanism in which one class acquires the property of another class. 
For example, a child inherits the traits of his/her parents. With inheritance, 
we can reuse the fields and methods of the existing class.

Polymorphism:
Polymorphism is a concept that allows objects of different classes to be treated as objects of a common superclass. 
For example, a cat and a dog are both animals. 
You can handle a cat and a dog in the same way because they are both animals.






"""

# class Student:
#     # methods
#     # properties
#     pass


# mahesh = Student()
# ravi = Student()

# isinstance(Student, object) # True


# type(mahesh) # __main__.Student

# isinstance(mahesh, Student) # True  


# class Student: 
#     def study():
#         print("study")

# yash = Student()

# yash.study()  # TypeError: study() takes 0 positional arguments but 1 was given


class Student: 
    def study(self):
        print("study")

yash = Student()

yash.study() # study