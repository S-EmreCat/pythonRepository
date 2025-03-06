# https://pynative.com/python-dictionary-exercise-with-solutions/

# Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# print(dict(zip(keys,values)))

# Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)
# dict3 = dict1 | dict2
# print(dict3)
# dict4 = {**dict1,**dict2}
# print(dict4)

# Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# print(sampleDict["class"]["student"]["marks"]["history"])

# Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
my_dict = dict.fromkeys(employees,defaults)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# my_dict = {}
# for i in sample_dict.keys():
#     if i in keys:
#         my_dict[i] = sample_dict[i]

# print(my_dict)

# Exercise 6: Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
sample_dict.pop("name")
sample_dict.pop("salary")
# print(sample_dict)

# Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
# 200 present in a dict

# if 200 in sample_dict.values():
#     print("200 present in a dict")
 
 # Exercise 8: Rename key of a dictionary
 #Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict["location"] = sample_dict.pop("city")
# print(sample_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# print(min(sample_dict.keys()))

# Exercise 10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
"""
Expected output:
{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
"""

sample_dict["emp3"]["salary"] = 8500
print(sample_dict)