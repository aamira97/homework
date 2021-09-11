"""
Homework 5
Deadline: 25 AUG, 20:00
"""

"""
Problem 1
​
You have a list, you want to iterate over it and return the numbers that are divisible by 5.
If you iterate over a number larger than 500, stop the loop.
"""
# ls = [5, 11, 30, 45, 175, 99, 106, 300, 490, 512, 890, 1000]
#
# for num in ls:
#     if num >= 500:
#         break
#     elif num % 5 == 0:
#         print(num)

# ls = [5, 11, 30, 45, 175, 99, 106, 300, 490, 512, 890, 1000]
#
# for i in ls:
#     if not i % 5:
#         if i >= 500:
#             continue
#         print(i)

"""
Problem 2
​
Create a loop to print the reverse of a list. 
"""
# list1 = [11, 21, 31, 41, 51]
#
# i = 1
# while i < 6:
#     print(list1[-i])
#     i += 1
#


"""
Problem 3

Write a function to get a number and return the factorial of the number. Use loops. 
ex. factorial of 5 is 1*2*3*4*5
You can't count factorial of negative numbers, and the factorial of 0 is 1. 
"""

# num = 40
# factorial = 1
#
# if num < 0:
#     print("can't calculate factorial of negative numbers")
# # elif num == 0:
# #     print("factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print(f"factorial of {num} is {factorial}.")

"""
Problem 4

Write a code that would print list items that are at even positions. 
ex. in list = [10, 11, 12], 10 is at index 0, 11 - index 1 (odd), 12 - index 2 (even)
Use loops
"""
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(len(my_list)):
#     if i % 2 == 0:
#         print(my_list[i], end=' ')


"""
Problem 5

Write a function that gets a list of names and returns the ones that start with A.
Notice that some list items begin and end with spaces, or start with @.
"""
# names = [' Anna', "Lily", " Anahit ", "@Bob", "@Ani@", " Luiza@", "@@Armen"]
#
# for name in names:
#     name = name.strip()
#     name = name.strip("Anna")
#     if name.startswith('A'):
#         print(name)

"""
Problem 6

Write a program that checks if a number is prime (պարզ) or not. Try not to google. :) 
"""

# num = 211
#
# for i in range(2, num):
#     if (num % i) == 0:
#         print(num, "is not a prime number")
#         break
# else:
#     print(num, "is a prime number")

"""
Problem 7 (OPTIONAL)

Write a loop that will print this pattern.

* 
* * 
* * * 
* * * * 
* * * * *


Hint: print("\r") -> for printing on a new line, 
      print('*', end=' ') -> for printing on the same line

"""

# for x in range(1, 6):
#     print(x * "* ")

# x = 0
# y = "*"
# while x < 5:
#     print(y)
#     y += " *"
#     x += 1

# The /r stands for "return" or "carriage return" which owes it's history to the typewriter.
# A carriage return moved your carriage all the way to the right so you were typing at the start of the line.
# The /n stands for "new line", again, from typewriter days you moved down to a new line.
