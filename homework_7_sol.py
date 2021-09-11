"""
Homework 7
Deadline: 30 AUG, 20:00
"""

"""
Problem 1

Write a function that will multiply all the list items.
"""
# list_of_numbers_2 = [3, 5, 15, 2, 9, 11, 10]
#
# prod = 1
# for i in list_of_numbers_2:
#     prod *= i
# print(prod)

"""
Problem 2

Write a program that removes duplicates from a list. DO NOT use set().
"""
# list_with_duplicates = ['a', 'b', 'ab', 'a', 'c', 'ab', 'd', 'hh', 'k', 'hh']
#
# without_dupl = []
# for i in list_with_duplicates:
#     if i not in without_dupl:
#         without_dupl.append(i)
#
# print(without_dupl)

"""
Problem 3

Write a program that will find the second smallest number of the list.
"""
# ls = [3, 5, 88, -1, 0, -1, 3, -7, -10, 3, 3, -7, 5, -10, 1]
#
# sorted_ls = list(set(ls))
# print(sorted_ls)
# sorted_ls.sort()
# print(sorted_ls)
# print(sorted_ls[1])


"""
Problem 4

Write a program that will add the string 'AAA' before every item of the list.
"""
the_list = ['chrome', 'opera', 'mozilla', 'explorer']

"""
Problem 5

Try to divide a number by 0. Use try, except as a backup. 
"""

# num1 = int(input('input the first number: '))
# num2 = int(input('input the second number: '))
#
# try:
#     print(num1 / num2)
# except:
#     print("You can't divide by zero.")

"""
Problem 6

Make a list and then try to access an index that doesn't exist. Use try and except. 
"""
the_list = ['chrome', 'opera', 'mozilla', 'explorer']

# try:
#     print(the_list[9])
# except IndexError:
#     print("No value for that index.")
# except:
#     print("something else is wrong")


"""
Problem 7 (OPTIONAL)

1. You have a list of lists. You need to flatten the list. (Make 1 list of all the items in all lists.)
2. Do the same thing with list comprehension.
"""

list_of_list = [['anna', 'bob'], ['john', 'peter'], ['sarah', 'jess', 'ben'], ['ross']]

# # 1
# flat_list = []
# for ls in list_of_list:
#     for item in ls:
#         flat_list.append(item)
#
# print(flat_list)
#
# 2
# flat_list_1 = [item for ls in list_of_list for item in ls]
# print(flat_list_1)
