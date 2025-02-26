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

print(max(my_set))
print(min(my_set))