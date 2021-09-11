"""
Homework 3
Deadline: 20 AUG, 20:00
"""
import math

"""
Problem 1
​
Write a function that gets a name and a salary and prints 'Employee named --- earns ---.'
If no salary is passed to the function, print the default salary which is 100.000.
"""

# def salary(name, salary=100000):
#     print("Employee named " + name + ' earns ' + str(salary))
#
#
# n = input("input your name ")
# s = input("input your salary ")
#
# salary(n, int(s))
# salary(n)
"""
Problem 2
​
Create a function that gets 3 numbers then checks if the f
irst number falls between the 2nd and 3rd numbers.
"""

# def func(num1, num2, num3):
#     if num2 <= num1 <= num3 or num3 <= num1 <= num2:
#         print(str(num1) + " is between " + str(num2) + " - " + str(num3))
#     else:
#         print(str(num1) + " is not in range ", num2, "-", num3)
#
#
# func(int(input("number 1: ")), int(input("number 2: ")), int(input("number 3: ")))

"""
Problem 3
​
Create a function that gets 3 numbers and returns the biggest of them.
Hint: You can use a function inside a function. 
"""

# def three_nums(num1, num2, num3):
#     def two_diff():  # we can also get this function out
#         if num1 >= num2:
#             return num1
#         else:
#             return num2
#
#     num = two_diff()
#     if num > num3:
#         return num
#     else:
#         return num3
# #
# #
# print(three_nums(-10, -19, -5))

"""
Problem 4
​
Write a function that will return the volume (ծավալ) of a cylinder (գլան). 
You can pass the radius and the height to the function. 
Google how to calculate the volume of the cylinder.
You are going to need sqrt(square root, արմատ) and pi (I show those below)
"""
#
# def cyl_volume(radius, height):
#     return math.pi * radius ** 2 * height
#
#
# def cyl_radius(volume, height):
#     return math.sqrt(volume / (math.pi * height))
#
#
# print(cyl_volume(4, 10))
# print(cyl_radius(502.6548245743669, 10))
"""
Problem 5 (Calculator)
​
Write a function that accepts 3 variables -> number1, number2, operation.
operation can be +, -, *, /
The function should return the result of the operation with the two number.
​
Example: calculator(9, 3, '+') -> result is 12
In case of division, if the second number is 0, say that the operation cannot be completed.
"""

# def calc(a, b, operation):
#     if operation == '/':
#         if b == 0:
#             return "Can't divide on 0"
#         else:
#             return a / b
#     elif operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#
#
# num1, num2, operation = int(input("input first number ")), int(input("input second number ")), input("input the operation symbol ")
# print(calc(num1, num2, operation))