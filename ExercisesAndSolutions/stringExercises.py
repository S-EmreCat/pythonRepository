# https://www.tutorjoes.in/python_programming_tutorial/string_programs_in_python

# 1. Write a Python program to calculate the length of a string.

# my_str = "Tutor Joes"
# len_str = len(my_str)
# print(len_str)

# 2. Write a Python program to count the number of characters (character frequency) in a string.

# my_str = "tutorjoes"
# countstr = 0
# mydict = {}
# for i in my_str:
#     countstr = my_str.count(i)
#     print(f"{i}: {my_str.count(i)}")
#     mydict[i] = my_str.count(i)
# print(mydict)    
    
# 4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

"""my_strA = "abc"
my_strB = "xyz"
my_str1 = my_strB[:2] + my_strA[2:]
print(my_str1)
my_str2 = my_strA[:2] + my_strB[2:]
print(my_str2)"""

# 5. Write a Python program to remove the nth index character from a nonempty string.

"""my_str = "Tutor Joes"
my_str = my_str.replace(my_str[my_str.index("t")],"")
print(my_str)
my_str = my_str.replace(my_str[5],"")
print(my_str)"""

# 6. Write a Python program to change a given string to a new string 
# where the first and last chars have been exchanged

my_string = "Python"
# print(my_string[::-1])

# 7. Write a Python program to remove the characters which have odd index values of a given string
my_string =  "Computer Education"
odd_strint= ""
for i in my_string:
    if my_string.index(i) % 2 == 0:
        odd_strint = odd_strint + i
#         print(i)

# print(odd_strint)

# 8. Write a Python program to count the occurrences of each word in a given sentence
"""my_string = "To change the overall look your document. To change the look available in the gallery"
my_list = my_string.split()
print(my_list)

a = [{i:my_list.count(i)} for i in my_list]
print(a)
b= {}
for i in a:
    b.update(i)
print(b)"""

# 9. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
my_string = "Tutor Joes"

# print(my_string.upper())
# print(my_string.lower())


# 10. Write a Python function to reverses a string if it's length is a multiple of 4.

# my_string = input("enter the string: ")
# if len(my_string) % 4 == 0:
#     print(f"the length is a multiple of 4 {my_string[::-1]}")
# else: 
#     print("the length is not a multiple of 4 {}".format(my_string))
    
# 11. Write a Python function to convert a given string to all uppercase 
# if it contains at least 2 uppercase characters in the first 4 characters.

my_string = "ComPuTeR"
count = 0
# for i in my_string[0:4]:
#     if i == i.upper():
#         count += 1
# if count >= 2:
#     my_string  = my_string.upper()
#     print(my_string) # "ComPuTeR" >  COMPUTER
# else:
#     print(my_string) # "CompuTeR" > "CompuTeR"
    
# 12. Write a Python program to sort a string lexicographically.
my_string = "Tutor"
# print(sorted([i.lower() for i in my_string ]))
# print(sorted(sorted(my_string), key=str.upper))

# 13. Write a Python program to remove a newline in Python.
my_string = "\nTutor \nJoes \nComputer \nEducation\n"
# print(f'before: {my_string}')
# my_string = " ".join(my_string.split())
# print(f'after: {my_string}')

# 14. Write a Python program to check whether a string starts with specified characters.
my_string = "Tutor Joes Computer Education"
# print(my_string.startswith('Tu'))

# 18. Write a Python program to print the following floating numbers upto 2 decimal places.
floatNumber = -84.99
# print(round(floatNumber,2))
# floatNumber = 23.36778
# print(round(floatNumber,2))

# 20. Write a Python program to print the following floating numbers with no decimal places
floatNumber = 23.36778
# print(round(int(floatNumber)))

# 22. Write a Python program to reverse a string.
my_string = "Python Exercises"
# print(my_string[::-1])


# 23. Write a Python program to reverse words in a string.
my_string = "Tutor Joes Computer Educations"
my_string = my_string.split()
# print(" ".join(my_string[::-1]).strip())  # Educations Computer Joes Tutor

# 24. Write a Python program to strip a set of characters from a string.
my_string = "Tutor Joes Computer Education"
chrs ="aeiou"
# print(" ".join(c for c in my_string if c not in chrs))

# 26. Write a Python program to swap comma and dot in a string.
val = "23,2000.00"
maketrans = val.maketrans
val = val.translate(maketrans(',.', '.,'))
print("After Swap Comma and Dot : ",val)

