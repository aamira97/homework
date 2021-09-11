"""
Homework 8
Deadline: 1 SEP, 20:00
"""

"""
Problem 1

Create 3 dictionaries for your favourite top 3 cars. Dict should contain information like brand, model, year, and color.
Add all those dicts in one dict and print items. 
"""

# car1 = {
#     "brand": "ford",
#     "model": "escape",
#     "year": "2020",
#     "color": "white"
# }
#
# car2 = {
#     "brand": "lambo",
#     "model": "urus",
#     "year": "2019",
#     "color": "gray"
# }
# car3 = {
#     "brand": "tesla",
#     "model": "x",
#     "year": "2020",
#     "color": "anything"
# }
# cars = {}
# cars.update({'car1': car1,
#              "car2": car2,
#              "car3": car3})
# print(cars.items())

"""
Problem 2

You have a list of lists. Each list in the list contains a key and a value. Transform it into a list of dictionaries. 
Use loops.
"""

# ls = [['Bob', 45], ['Anna', 4], ['Luiza', 24], ['Martin', 14]]
#
# dt = {}
#
# for i in ls:
#     dt.update({i[0]: i[1]})
#
# print(dt)

"""
Problem 3

Check if value 1000 exists in the dict values. If yes delete all other items except that one.
"""
# dt = {'hundred': 100, 'million': 1000000, 'thousand': 1000, 'ten': 10}
#
# if 1000 in dt.values():
#     for k, v in dt.items():
#         if v == 1000:
#             dt.clear()
#             dt.update({k: v})
#             print(dt)
#             break
# else:
#     print(dt)

"""
Problem 4

Change Narine's salary to 10000
"""
# sampleDict = {
#     'employee1': {'name': 'Marine', 'salary': 7500},
#     'employee2': {'name': 'Karine', 'salary': 8000},
#     'employee3': {'name': 'Narine', 'salary': 6500}
# }
#
# for i in sampleDict.values():
#     if i.get('name') == 'Narine':
#         i.update({'salary': 10000})
# print(sampleDict)

"""
Problem 5

Write a function that will get a dict of employees and their salaries. It will return a new dict with 
the same keys (employees) and all values will be the average of their salaries. 
example:  dict1 = {'ann': 3000, 'bob': 4000, 'lily': 5000}
          dict2 = {'ann': 4000, 'bob': 4000, 'lily': 4000}
"""
dict1 = {'ann': 3000, 'bob': 4000, 'lily': 5000, 'molly': 5500, 'some_intern': 500}


# def func(dt):
#     dt_len = len(dt)
#     sum_salary = 0
#     for i in dt.values():
#         sum_salary += i
#     avg = sum_salary / dt_len
#     for j in dt:
#         dt.update({j: avg})
#     return dt
# #
# #
# print(func(dict1))

"""
Homework 7 Problem 4

Write a program that will add the string 'AAA' as an item before every item of the list.
"""

# the_list = ['chrome', 'opera', 'mozilla', 'explorer']
# ls = []
# for i in the_list:
#     for j in ["AAA", i]:
#         ls.append(j)
# print(ls)
