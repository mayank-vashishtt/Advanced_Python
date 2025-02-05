# dict

# d ={

#     "name": "mayank",
#     "marks": 90,
#     "subjects": ["eng", "maths"]
# }


# # print(d.get("name"))  # mayank
# # print(d["name"]) # mayank
# # d["name"] = "sanvi"
# # print(d)


# # d.pop("marks")
# # print(d)  # {'name': 'sanvi', 'subjects': ['eng', 'maths']}

# d.update({"name" : "shivank" , "college" : "iiit"})
# # print(d)  # {'name': 'shivank', 'subjects': ['eng', 'maths'], 'college': 'iiit'}


# # # for i in d: 
# # #     print(i)  # name, subjects, college 

# # # for i in d.values():
# # #     print(i)  # shivank, ['eng', 'maths'], iiit

# # for i in d.items():
# #     print(i)  # ('name', 'shivank'), ('subjects', ['eng', 'maths']), ('college', 'iiit')

# # for key, value in d.items():
# #     print(key , "---> " ,  value)  # name shivank, subjects ['eng', 'maths'], college iiit


# # // any immutable datastructure can also be key 
# # // any immutable or mutable can be your value 


# # d1 = {
# #     [1,2] : "mayank"
# # }



# # print(d1)  # TypeError: unhashable type: 'list'
# # anything which in python is mutable cannot be a key

# # print(d["college"])  # iiit


# print(d.get("colege", "not found"))  # not found -- as typo error 



# sets 

# s = {1,2,3,4,51,2,3,2,1,1,5,1} 

# s1 = set()  # blank element 
# s1.add(10)
# s1.add(20)
# s1.add(2)

# print(s1) # {10, 2, 20}


# s1.add(10)
# s1.add(20)
# s1.add(1)
# print(s1) # {1, 10, 20}


# s1 = set()  # blank element  output --> set()
# s1.add(10)

# s1.add(10)
# s1.remove(10)


# print(s1) # {10}


# s = {1, 11 ,2 , 3 ,21,1,2,11 }

# for i in s: 
#     print(i)  # 1, 2, 3, 11, 21


# a = {1,2}
# b = {1,3,4,5}

# print(a-b) # {2}

# # print(a+b) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print (a | b)  # {1, 2, 3, 4, 5}
# print (a & b)  # {1}


