# john_info = {
#     "name": "john",
#     "cgpa": 9.6,
#     "marks": [85, 90, 78],
#     "subject": ("maths", "physics", "chemistry"),
#     "age": 20,
#     "is_adult": True,
# }
# john_info["name"] = "haziq"
# john_info["surname"] = "syed"
# print(john_info)
# shees_info = {} #empty dictionary
# shees_info["name"] = "shees"
# print(shees_info)

# NESTED DICTIONARY
from operator import add


Talha = {
    "name": "Talha",
    "age": 20,
    "subjects": {
        "maths": 90,
        "physics": 85,
        "chemistry": 80
    }
}
# print(Talha["subjects"]["maths"]) #accessing nested dictionary value
# print(Talha.keys()) #to get all the keys of the dictionary
# print(Talha.values()) #to get all the values of the dictionary
# print(Talha.items()) #to get all the key-value pairs of the dictionary, In tuple format
# print(Talha["name"])
# print(Talha.get("name4")) #to get the value of a key, if the key is not present it will return None
# newdict={"name": "Haziq", "roll_number": 21} 
# Talha.update(newdict) #to update the dictionary with another dictionary
# print(Talha)

""""
 SETS
Sets are unordered collection of unique elements. 
Sets are mutable but the elements of a set must be immutable.
"""
collection = set() #empty set
collection.add(1) #to add an element to the set
collection.add(2)
collection.add("haziq")
collection.add((1, 2, 3)) #to add a tuple to the set
# collection.add([1, 2, 3]) #to add a list to the set, this will give an error because list is mutable
# collection.clear() #to remove all the elements from the set
# print(len(collection)) #to get the length of the set
# print(collection)
print(collection.pop()) #to remove a random element from the set
print(collection.pop()) #to remove a random element from the set

