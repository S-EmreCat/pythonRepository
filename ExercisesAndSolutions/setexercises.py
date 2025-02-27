# https://www.tutorjoes.in/python_programming_tutorial/set_programs_in_python

# 1. Write a Python program to create a set
my_set = {'T', True, 45, 23, 56, 'Joes', 45.6}
# print(type(my_set),my_set)

# 2. Write a Python program to iteration over sets

# for i in my_set:
#     print(i)
    
# 3. Write a Python program to add member(s) in a set

my_set = {"Lion", "Cat"}
my_set.add("Dog")
# print(my_set)

# 4. Write a Python program to remove item(s) from a given set
"""my_set = {'T', True, 45, 23, 56, 'Joes', 45.6}
print(my_set)
my_set.remove(45)
print(my_set)
my_set.pop()
print(my_set)
my_set.pop() 
print(my_set)
my_set.discard(56)
print(my_set)"""

# 6. Write a Python program to create an intersection of sets
"""a= {40, 20, 70, 30}
b={40, 50, 20, 60}
c=b.intersection(a)
print(c)"""

# 7. Write a Python program to create a union of sets
"""a= {40, 20, 70, 30}
b={40, 50, 20, 60}
c=b.union(a)
print(c)"""

# 8. Write a Python program to create set difference

a= {80, 50, 20, 70, 40, 30}
b= {50, 20, 90, 40, 10, 60}
"""c=b.difference(a)
print(c)
print(a.difference(b))"""

# 9. Write a Python program to create a symmetric difference

a= {80, 50, 20, 70, 40, 30}
b= {50, 20, 90, 40, 10, 60}
# print(a.symmetric_difference(b))

# 12. Write a Python program to check if two given sets have no elements in common

a = {23, 8, 56, 45, 78}
b = {42, 26, 55, 87}
z = {46, 87}

"""print("Compare A and B: ", a.isdisjoint(b))
print("Compare B and Z: ", b.isdisjoint(z))
print("Compare A and Z: ", a.isdisjoint(z))"""

# 13. Write a Python program to find maximum and the minimum value in a set

my_set = {17, 56, 23, 8, 10, 45}

# print(max(my_set))
# print(min(my_set))

# 14. Write a Python program to remove all elements from a given set
my_set = { "Red", "Green", "Pink", "White", "Black", "Yellow", "Blue" }
my_set.clear()
# print(my_set)

# 15. Write a Python program to Intersection of two lists
l1 = [1,2,3,4,5,6,7,8]

l2 = [11,2,43,48,55,6,76,8]

# print(set(l1).intersection(set(l2)))

# 16. Write a Python program to Convert String to Set
my_string = "TutorJoes"
my_set = set(my_string)
# print(my_set)

# 17. Write a Python program to Convert Set to String
my_set = {'T', 'u', 't', 'o', 'r', 'J', 'o', 'e' , 's'}
my_string =""
my_string2=str(my_set)
# print(my_string2)
# print(type(my_string2))
# print(my_string.join(list(my_set)))
# print(type(my_string.join(list(my_set))))

# 19. Write a Python program to Convert Set to Tuple
my_set = {'T', 'u', 't', 'o', 'r', 'J', 'o', 'e' , 's'}
# print(tuple(my_set),type(tuple(my_set)))

# 21. Write a program to add all its elements into a given set
my_set = {10,20,30,40,50}

my_list = [60,70,80,90,100]
# for loop
# for i in my_list:
#     my_set.add(i)
# print(my_set)

# update 
# my_set.update(my_list)
# print(my_set)

# 22. Write a Python program to return a new set 
# with unique items from both sets by removing duplicates.
a = {10, 20, 30, 40, 50}
b = {40, 50, 60, 70,80}
c = b.union(a)
# print(c)

# 23. Write a Python program to Check if two sets have any elements in common. 
# If yes, display the common elements

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {5, 3, 7, 8, 9}
my_set3 = {6, 7, 8, 9, 10}

"""
print(f"set1 and set2 commons: {my_set1.isdisjoint(my_set2)}") 
# False ("Two sets items in Common")
print(f"set1 and set2 commons: {my_set1.intersection(my_set2)}")
print(f"set1 and set3 commons: {my_set1.isdisjoint(my_set3)}") 
# True ("Two Sets No items in Common")
print(f"set1 and set3 commons: {my_set1.intersection(my_set3)}")
"""