# https://www.tutorjoes.in/python_programming_tutorial/tuple_comprehensions_exercises_in_python

# 1. Squares of numbers from 1 to 10 as tuples
res = tuple(x**2 for x in range(1,10))  # (1, 4, 9, 16, 25, 36, 49, 64, 81)

# 2. Even numbers from 1 to 20 as tuples
res = tuple( x for x in range(1,20) if x % 2 == 0) # (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

# 3. Tuple of characters in a string # ('h', 'e', 'l', 'l', 'o') 

string = "hello"
res = tuple(i for i in string)

# 4. Length of words in a sentence as tuples  (4, 2, 1, 6, 8)
string = "This is a sample sentence"

res = tuple(len(i) for i in string.split(" "))


# 5. Vowels in a sentence as tuples

string = "Hello, how are you?"

res = tuple(x for x in string if x in "aeiou")

# 6. Tuple of distinct prime factors of numbers in a list  # (2, 5, 3, 5, 2, 5, 5)

my_list = [10, 15, 20, 25]

# for i in my_list:
#     print(f'i: {i}')
#     for k in range(2,i+1):
#         print(f'i: {i}')
#         if i % k == 0 and all(k % d != 0 for d in range(2,k)):
#             print(f'k: {k}')
    
res = tuple(i for number in my_list for i in range(2,number+1) if number % i  == 0 and all(i % d != 0 for d in range(2,i)))

# 7. Tuple of distinct characters in a list of strings # ('a', 'p', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y')

my_list = ['apple', 'banana', 'cherry']
res = tuple(c for word in my_list for c in word)

# 8. Tuple of ASCII values for characters in a string  # (104, 101, 108, 108, 111)
string = "hello"
res= tuple(ord(i) for i in string)

# 9. Tuple of common letters between two words # ('a',)

string1 = "apple"
string2 = "banana"
# for i in string1:
#     for k in string2:
#         if i == k:
#             print(i)
res = tuple(set(i for i in string1 for k in string2 if i == k))
common_letters = tuple(char for char in string1 if char in string2)

# 10. Tuple of even squares up to 100
res = tuple(i**2 for i in range(11) if i % 2 == 0)

print(res)
