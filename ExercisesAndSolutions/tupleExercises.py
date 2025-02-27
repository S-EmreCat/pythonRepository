# https://www.tutorjoes.in/python_programming_tutorial/tuple_programs_in_python

# 5. Write a Python program to add an item in a tuple
# my_tuple = (10, 40, 50, 70, 90)
# my_tuple = my_tuple + (20,)
# print(my_tuple)

# my_list = list(my_tuple)
# my_list.append(20)
# print(tuple(my_list))

# 6. Write a Python program to convert a tuple to a string

my_tuple=('T', 'u', 't', 'o', 'r', ' ', 'J', 'o', 'e', 's')

my_string = "".join(my_tuple)
# print(my_string)

# 7. Write a Python program to get the 4th element and 4th element from last of a tuple
my_tuple = ('w', 3, 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e')
# print(my_tuple[3],my_tuple[-4])

# 8. Write a Python program to create the colon of a tuple
my_tuple = ("Tutor", 'J', 23 , 56.67 , [23,12] , True)
tuple_copy = my_tuple
tuple_copy = tuple_copy + (50,)
# print(tuple_copy)


# 9. Write a Python program to find the repeated items of a tuple

my_tuple = (2, 34, 45, 6, 7, 2, 4, 5, 78, 34, 2)
count = my_tuple.count(2)
# print(count)

# 10. Write a Python program to check whether an element exists within a tuple

my_tuple = ('T', 'u', 't', 'o', 'r', ' ', 'J', 'o', 'e', 's',8)
# print(9 in my_tuple)
# print(8 in my_tuple)

# 12. Write a Python program to remove an item from a tuple
my_tuple = (23, 45, 56, 68, 10, 45, 7, 9)
my_list = list(my_tuple)
my_list.remove(56)

# print(tuple(my_list))

# 13. Write a Python program to slice a tuple

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
len_tuple= int(len(my_tuple)/2)
# print(my_tuple[0:len_tuple])
# print(my_tuple[len_tuple:])

# 14. Write a Python program to find the index of an item of a tuple
my_tuple = (23, 45, 67, 78, 89, 90, 34, 56)
# print(my_tuple.index(45))
# print(my_tuple.index(34))

# 15. Write a Python program to find the length of a tuple
my_tuple = ("Lion", "Cat", "Dog", "Panda", "Tiger", "Fox")
# print(len(my_tuple))

# 16. Write a Python program to convert a tuple to a dictionary
my_tuple = (("Name", "Ram"), ("Age", 23), ("City", "Salem"), ("Mark", 422))

# my_dict = dict(my_tuple)
# print(my_dict)
# print(dict((k,v) for k,v in my_tuple))


