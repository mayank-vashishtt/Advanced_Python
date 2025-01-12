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

