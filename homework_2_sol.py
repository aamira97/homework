"""
Homework 2
Deadline: 18 AUG, 20:00
"""

"""
Problem 1

Create a program to check if a number entered by a user is even or odd.
Use input() function to save user's input.
"""
# number = float(input("Enter a number: "))
# # n = int(number)
# if number % 2 == 0:
#     print(str(number) + ' is even')
# else:
#     print(str(number) + ' is odd')

"""
Problem 2

Create a program to check if the number is divisible by 3. 
"""
# number = int(input("Enter a number: "))
# if number % 3 == 0:
#     print(number, ' is divisible by 3.')
# else:
#     print(str(number) + ' is not divisible by 3.')


"""
Problem 3

Write a program that allows user to enter their grade and tells them which letter they got. 

 Grade                       Letter Grade
 > 95                             A
 85 - 95                          B
 65 - 84                          C
 < 65                             D
"""
# grade = float(input("Enter your grade: "))
# if 95 < grade <= 100:
#     print('Your grade is A')
# elif 85 <= grade <= 95:
#     print('Your grade is B')
# elif 65 <= grade < 85:
#     print('Your grade is C')
# elif grade < 65:
#     print("Your grade is D")
# else:
#     print("Wrong input")

"""
Problem 4

Create a program that takes a number (1-7) from user and returns a day of the week. 
Like 1 for Monday, 2 for Tuesday, etc.
"""

# day = int(input("Input a number: "))
# if day == 1:
#     print('Monday')
# elif day == 2:
#     print('Tuesday')
# elif day == 3:
#     print('Wednesday')
# elif day == 4:
#     print('Thursday')
# elif day == 5:
#     print('Friday')
# elif day == 6:
#     print('Saturday')
# elif day == 7:
#     print('Sunday')
# else:
#     print("Wrong input")

"""
Problem 5

Create a program that tells if a person can get a driving license or no.
Required age for driving license is 17. 

If they are older than 17, check the score of their test (which can be from 0 to 10).
If the score is 9 or 10, they get a license, if it is less than 9 they don't get a license.
"""

# age = int(input("Please insert your age: "))
# if age >= 17:
#     score = int(input("Please insert your exam score:"))
#     if score == 9 or score == 10:
#         print('You get a license.')
#     elif 0 < score > 10:
#         print("Invalid score.")
#     else:
#         print("You can't get a license.")
# else:
#     print("You can't get a license.")

"""
Problem 6

Write a program that takes 2 numbers from the user and prints the smaller one.
"""

# number1 = float(input("1st number: "))
# number2 = float(input("2nd number: "))
# if number1 > number2:
#     print(number2, 'is smaller than', number1)
# elif number1 < number2:
#     print(number1, 'is smaller than', number2)
# else:
#     print("Numbers are equal.")

"""
Problem 7

Create a program to check whether a number is negative or positive or equals to 0.
"""

# number = float(input("Please insert a number: "))
# if number == 0:
#     print('number equals to 0')
# elif number > 0:
#     print('number is positive')
# else:
#     print('number is negative')

"""
Problem 8

Bob wants to go to university. 

Bob can be accepted if his math exam score is 10 or more and his english exam score is 10 or more.
Bob can also be accepted if his math score is 15 or more and his english score is 5 or more
                            or his math score is 5 or more and his english score is 15 or more.
Bob can also be accepted if one of the scores is 20. 
Bob cannot be accepted if both scores are 0. 

(Exam scores are from 0-20)
"""
#
english_score = float(input("Input your english score: "))
math_score = float(input("Input your english score: "))
if math_score > 20 or english_score > 20 or math_score < 0 or math_score < 0:
    print("Invalid Score.")
else:
    if math_score >= 10 and english_score >= 10:
        print("Bob is accepted.")
    elif (math_score >= 15 and english_score >= 5) or (english_score >= 15 and math_score >= 5):
        print("Bob is accepted.")
    elif math_score == 20 or english_score == 20:
        print("Bob is accepted.")
    elif math_score == 0 and english_score == 0:
        print("Bob is not accepted")
    else:
        print("Bob is not accepted")