# https://pynative.com/python-string-exercise/
# Exercise 1A: Create a string made of the first, middle and last character
str1 = "James"
res = str1[0::2]

# Exercise 1B: Create a string made of the middle three characters
str1 = "JhonDipPeta"
middlestr1 = int(len(str1)/2)
res = str1[ middlestr1-1 : middlestr1+2 ]

#Exercise 2: Append new string in the middle of a given string

s1 = "Ault"
s2 = "Kelly"
mi = int(len(s1) / 2)

# get character from 0 to the middle index number from s1
x = s1[:mi:]
# concatenate s2 to it
x = x + s2
# append remaining character from s1
x = x + s1[mi:]
# print("After appending new string in middle:", x)


# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"
first_char = s1[0] + s2[0]

# get middle character from both string
middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

# get last character from both string
last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

# add all
res = first_char + middle_char + last_char
# print("Mix String is ", res)

#Exercise 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
lowers = []
uppers = []
for i in str1:
    if i.islower():
       lowers.append(i)
    elif i.isupper():
         uppers.append(i)
         
# print("".join(lowers+uppers))


# Exercise 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
letters = [i for i in str1 if i.isalpha()]
digits = [ i for  i in str1 if i.isdigit()]
symbols = int(len(str1)-len(letters)-len(digits))
# print(len(letters), len(digits), symbols)


# Exercise 7: String characters balance Test

"""
Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character’s position doesn’t matter.
"""
s1 = "Yn"
s2 = "PYnative"
flag = True
for char in s1:
    if char in s2:
        continue
    else:
        flag = False
# print(flag) 

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
# print(str1.lower().count("usa"))


# Exercise 9: Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"

total = 0
cnt = 0
for char in str1:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)


# Exercise 10: Write a program to count occurrences of all characters within a string
str1 = "Apple"

char_dict = dict()

for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print('Result:', char_dict)