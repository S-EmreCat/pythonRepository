# https://www.tutorjoes.in/python_programming_tutorial/list_programs_in_python

# 1 Write a Python program to sum all the items
my_list = [1,7,-10,34,2,-8]
sum = 0 
for i in my_list:
    sum += i
#print (sum)

# 2 Write a Python program to multiply all the items in a my_list

my_list = [3,4,5,4,7]
result = 1
for i in my_list:
    result *= i
# print(result)

# 3 Write a Python program to get the largest number from a my_list

my_list = [1,7,10,34,2,8]

# print(max(my_list))

# 4. Write a Python program to get the smallest number from a my_list

my_list = [51,7,10,34,2,8]
# print(min(my_list))

# 5. Write a Python program to count the number of strings 
# where the string length is 2 or more and the first and last character 
# are same from a given my_list of strings

my_list = ['abc', 'xyz', 'aba', '1221']

count = 0
strint = ''
for i in my_list:
    if len(i) > 1 and i[0] == i[-1]:
        count+=1
# print(count)    
        
# 6. Write a Python program to remove duplicates from a my_list
     
my_list = [1,2,3,7,2,1,5,6,4,8,5,4]
# list set 
new_list = list(set(my_list))
# print(new_list)
# set 
set_new_list = set(my_list)
# print(set_new_list)

# 7. Write a Python program to check a list is empty or not

my_list = [34,45,6,5,4,56,7] #not empty
a = [] #empty 

# if a:
#     print("not empty")
# else:
#     print("empty")
    
# 8. Write a Python program to clone or copy a list

my_list = [10, 22, 44, 23, 4]
aClone =my_list
bCopy = my_list.copy() 
my_list.insert(4,113)
# print(aClone)
# print(bCopy)

# 9. Write a Python program to find the list of words 
# that are longer than n from a given list of words

#Find the List of Words that are Longer than n from a given List of Words
#Given value of 

n = 4
listOfWords= "Find the List of Words that are Longer than n from a given List of Words"
my_list = listOfWords.split(" ")
# print(my_list)
len4Words = []
for i in my_list:
    if len(i) > 4:
        len4Words.append(i)
# print(len4Words)        

# 10. Write a Program that get two lists as input and check 
# if they have at least one common member

my_list1 = [1,2,3,9,4,5]
my_list2 = [5,6,7,8,9,2]
# my_list_common = []
# for member1 in my_list1:
#     for member2 in my_list2:
#         if member1 == member2:
#             my_list_common.append(member1)
#             print(f"{member1} Lists have at least one common member")
#         else:
#             print(f"{member1}-{member2} no common")

# print(my_list_common)      


# 17. Write a Python program to find the index of an item in a specified list  

my_list = [20, 70, 30, 90, 10, 30, 90, 10, 80] 
indexItem = my_list.index(30)
# print(indexItem)
    
# 18. Write a Python program to find the index of an item in a specified list

import itertools
my_list = itertools.chain([[20,30,70],[30,90,10], [30,20], [70,90,10,80]])

# 19. Write a Python program to add a list to the second list

my_list = [10, 20, 30, 40]
my_list2 = ["Cat", "Dog", "Lion", "Ponda"]
# my_list3 = my_list + my_list2
# print(my_list3)
my_list.extend(my_list2)

# 20. Write a Python program to select an item randomly from a list Using random.choice()

import random
my_list = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# print(random.choice(my_list))

# print(my_list)

# 22. Write a Python program to find the second smallest number in a list
my_list = [2,4,56,78,4,34,5,8,9,2,2,4,4,5]

a = sorted(set(my_list))
# print(a)
# # print(a[0])
# print(a[1])
# print(a[-1])


# 23. Write a Python program to find the second largest number in a list

my_list = [82,4,56,78,4,34,5,100,9]

a = sorted(my_list,reverse=True)[1]
# print(a)

# 24. Write a Python program to get unique values from a list

my_list = [82, 4, 10, 56, 78, 4, 34, 5, 10, 9]
# print(list(set(my_list)))

# 25. Write a Python program to get the frequency of the elements in a list.

my_list = [10, 30, 50, 10, 20, 60, 20, 60, 40, 40, 50, 50, 30]
my_dict={}
for i in my_list:
    my_dict[i] = my_list.count(i)
# print(my_dict)

# 26. Create a list by concatenating a given list which range goes from 1 to n
my_list = ['T', 'J']
N = 10
list2=[]
# for i in range(1,11):
#     list2.extend([my_list[0]+str(i)])
#     list2.extend([my_list[1]+str(i)])
  
# print(list2)

# for i in range(1,11):
#     for t in my_list:
#         list2.append(t+str(i))
        
# print(list2)

# 27. Write a Python program to get variable unique identification number or string

x = 30

s = "Tutor Joes"

# print(f'{x}: identification: {id(x)}')
# print(format(id(x), 'x'))

# 28. Write a Python program to find common items from two lists
my_list1 = [23,45,67,78,89,34]

my_list2 = [34,89,55,56,39,67]
my_list3 = []
for l1 in my_list1:
    for l2 in my_list2:
        if l1 == l2:
            my_list3.append(l1)
# print(my_list3) 
# print(list(set(my_list2).intersection(my_list1)))
# print(list(set(my_list1) & set(my_list2)))

# 29. Write a Python program to split a list based on first character of word
my_list = ["cat", "dog", "cow", "tiger", "lion", "Fox", "Shark", "Snake",
           "turtle", "mouse", "monkey", "bear"]

# sorted_list = sorted(my_list)
# for i in sorted_list:
#     print(i[0])
#     for j in sorted_list:
#         if j.startswith(i[0]):
#             print("  ", j)
            
# 30. Write a Python program to select the odd number of a list

my_list = [1,2,4,3,6,7,5,8,9,7,8,9,10]
a = [a for a in my_list if a%2!=0]
# print(a)

            
    
    


