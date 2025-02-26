# https://www.tutorjoes.in/python_programming_tutorial/dictionary_programs_in_python

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

dict = dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_dict= sorted(dict.items(), key= lambda item : item[1])
sorted_dict= sorted(dict.items(), key= lambda item : item[1],reverse=True)
# print(sorted_dict)

# 2. Write a Python program to add a key to a dictionary

dictionary = {"Name" : "Ram" , "Age" : 23}
# print(dictionary)
add_key = {"City" : "Salem"}
dictionary.update(add_key)
# print(dictionary)
dictionary["new_key"] = "new_value"
# print(dictionary)

# 3. Write a Python program to concatenate following dictionaries to create a new one.

dictionay1 = {"Name" : "Ram" , "Age" : 23}
dictionary2 = {"City" : "Salem", "Gender" : "Male"}

#update
dictionay1.update(dictionary2)
# print(dictionay1)
# | (Pipe) operator
my_dict = dictionay1 | dictionary2
# print(my_dict)
# ** operator
my_dict = {**dictionay1,**dictionary2}
# print(my_dict)

# 4. Write a Python program to check whether a given key already exists in a dictionary.

my_dict = {'Name' : 'Ram', 'Age' : 23,}
# if "Name1" in my_dict:
#     print("key is available")
# else:
#     print("key is not available")

# 5. Write a Python program to iterate over dictionaries using for loops.
my_dict = {"Name" : "Ram" , "Age" : 23 , "City" : "Salem", "Gender" : "Male"}

# ('Name', 'Ram')
# for i,k in my_dict.items():
#     print(i,k)
# for i in my_dict.items():
#     print(i)
    
# 6. Write a Python script to generate and print a dictionary that 
#       contains a number (between 1 and n) in the form (x, x*x).

# number = int(input("enter the number: "))
# my_dict = {}
# for i in range(1,number+1):
#     my_dict.update({i:i*i})
# print(my_dict)

# 9.Write a Python program to iterate over dictionaries using for loops.
# my_dict = {"Name":"Ram" , "Age":23 , "City": "Salem", "Gender": "Male"}
# for k, v in my_dict.items():
#      print(f'{k} : {v}')

# 10. Write a Python program to sum all the items in a dictionary.


# my_dict = {1 : 23, 2 : 45, 3 : -17, 4 : 87}
# total = 0
# for v in my_dict.values():
#     total += v
#     print(total)
# print(f"sum:{sum(my_dict.values())}")

# 11. Access dictionary key’s element by index.
my_dict = {"Name" : "Pooja", "Age" : 23, "Gender" : "Female", "City" : "Salem", "Mark" : 488}

for i in my_dict.keys():
    print(i)
x = [x for x in my_dict.keys()]
