# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/#h-exercise-1-print-first-10-natural-numbers-using-while-loop

# Exercise 1: Print first 10 natural numbers using while
i = 0
# while i < 10:
#     print(i)
#     i +=1
    
#  Exercise 2: Print the following pattern
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

# for i in range (1,6):
#     for j in range(1,i+1):
#         print(j,end= " ")
#     print("")
        
        
# Exercise 3: Calculate sum of all numbers from 1 to a given number
# sum = 0 
# for i in range (1,11):
#     sum +=i
# print(sum) # 55

# print(sum(range(1,11))) #55

# Exercise 4: Print multiplication table of a given number

# num = 2
# for i in range(1,11):
#     print(num*i)


# Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
"""
The number must be divisible by five
If the number is greater than 150, then skip it and move to the following number
If the number is greater than 500, then stop the loop
"""
# for i in numbers:
#     if i > 500:
#             break
#     if i > 150:
#             continue    
#     elif i % 5 == 0:
#         print(i)
 
# Exercise 6: Count the total number of digits in a number

# number = 75869
# count = 1
# while number // 10 > 1:
#     count +=1
#     number = number // 10
#     print(f'number: {number} , count : {count}')
# print(count)

# Exercise 7: Print the following pattern
"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

# for i in range(1,6):
#     for j in range(6-i,0,-1):
#         print(j, end=" ")
#     print("")

# Exercise 8: Print list in reverse order using a loop (((Using a reversed())))
list1 = [10, 20, 30, 40, 50]
"""
50
40
30
20
10"""
# for i in list1:
#     print(i)
# list2 = reversed(list1)
# for i in list2:
#     print(i)

# for  i in range(len(list1)-1,-1,-1):
#     print(list1[i])

# Exercise 9: Display numbers from -10 to -1 using for loop
# for i in range(-10,0,1):
#     print(i)
    
# Exercise 10: Display a message “Done” after the successful execution of the for loop    

# for i in range(3):
#     print(i)
# else:
#     print("done")

# Exercise 11: Print all prime numbers within a range
# number = int(input("enter range: "))
# start = 25
# for i in range (start,number+1):
#     if i > 1:
#         for j in range(2,i):
#             if (i% j ==0):
#                 # print(f"{i} is not prime")
#                 break
#         else:
#             print(f"{i} is prime")    
            
# Exercise 12: Display Fibonacci series up to 10 terms

# first = 1
# second = 1
# fibonacciSeries = [first,second]
# for i in range(10):
#     first , second = second , second + first
#     fibonacciSeries.append(second)

# print(fibonacciSeries)

# Exercise 13: Find the factorial of a given number
# number = int(input("enter number: "))
# factorial = 1
# for i in range(1,number+1):
#     factorial *=i
# print(factorial)

# Exercise 14: Reverse a integer number
# number = 76542
# print(str(number)[::-1])

# Exercise 15: Print elements from a given list present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(len(my_list)+1):
#     if i % 2 != 0:
#         print(my_list[i])
# for i in my_list[1::2]:
#     print(i)

# Exercise 16: Calculate the cube of all numbers from 1 to a given number
# number = int(input("enter number: "))
# for i in range(number+1):
#     print(f'number: {i} and cube is: {i**3} ')

# Exercise 18: Print the following pattern
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print("")

for i in range(4,-1,-1):
    for j in range(i+1):
        print("*",end=" ")
    print("")
    