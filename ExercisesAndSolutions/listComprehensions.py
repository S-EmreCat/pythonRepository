# https://www.tutorjoes.in/python_programming_tutorial/list_comprehensions_exercises_in_python

# 1. Create a List of Squares of numbers from 1 to 10

res = [i**2 for i in range(1,11)]

# 2. Create a List of Even numbers from 1 to 20

res = [i for  i in range(1,20) if i%2 ==0]

# 3. Generate a list of characters from a string

string = "Hello World!"
res = [i for i in string if i.isalpha()]

# 4. Create a list of lengths of words in a sentence
string = "This is a sample sentence."
res = [len(i) for i in string.split()]

# 5. Generate a list of tuples containing a number and its square

res = [(i, i**2) for i in range(1,11)]

# 6. Create a list of lowercase letters

import string 
res = [ i for i in string.ascii_lowercase]
lowercase_letters = [chr(x) for x in range(ord('a'), ord('z')+1)]
# print(lowercase_letters)
# print(string.ascii_lowercase)

# 7. Generate a list of uppercase letters
res = [i for i in string.ascii_uppercase]

# 8. Create a list of even numbers squared and odd numbers cubed from 1 to 10

res = [i**2 if i % 2== 0 else i**3  for i in range(1,10)]

# 9. Generate a list of common multiples of 3 and 5 up to 100

res = [ i for i in range(1,100) if i % 3 == 0 and i % 5 == 0]

# 10. Create a list of reversed strings from another list
my_list = ['apple', 'banana', 'cherry']

res = [ i[::-1] for i in my_list]

# 11. Generate a list of prime numbers from 1 to 50

res =(sorted(set([x for x in range(2,51)]).difference(set([x for x in range(1, 51) if x > 1 for i in range(2,x) if x % i == 0]))))

# 12. Create a list of squares of even numbers and cubes of odd numbers from -5 to 5

res = [ i**3 for i in range(-5,6)]

# 13. Generate a list of strings with their lengths from another list
my_list = ['apple', 'banana', 'cherry']
res = [(i,len(i)) for i in my_list]

# 14. Create a list of first characters from a list of words 
my_list = ['apple', 'banana', 'cherry']
res = [i[0] for i in my_list]

# 15. Generate a list of numbers with their squares if the number is even
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i**2 for i in my_list if i % 2 == 0 ]

# 16. Create a list of uppercase words from a sentence
string = "This is a sample sentence."
res = [i.upper() for i in string.split() ]

# 17. Generate a list of strings with vowels removed
import string
my_list = ['apple', 'banana', 'cherry']
res = [''.join([char for char in word if char.lower() not in 'aeiou']) for word in my_list]

print(res)

