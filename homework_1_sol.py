"""
Homework 1
Deadline: 16 AUG, 20:00
"""

"""
Problem 1.

Give examples of integer, string and float values.
Then use type() function to prove it. 
"""
example_of_integer = 44
example_of_string = "a text message"
example_of_float = 5.5

print(type(example_of_integer))
print(type(example_of_string))
print(type(example_of_float))

"""
Problem 2.

Create variables movie1 and movie2, assign your 2 favourite movies to those variables.
Put the variables in the text "My 2 favourite movies are ____, ____." and print it. 
"""
movie1 = "Star Wars"
movie2 = "The Proposal"
print("My 2 favourite movies are ", movie1, movie2)

"""
Problem 3.

Calculate your age using the value of the year you were born and the value of current year.
"""
current_year = 2021
year_i_was_born = 1997
my_age = current_year - year_i_was_born
print("I am " + str(my_age) + " years old.")

"""
Problem 4.

What is wrong with this variable name? Correct it.
"""
my_first_name = "Poghos"

"""
Problem 5.

Petros is 20 years old.
Print "Petros is younger than me." if his age is smaller than yours.
Print "Petros is older than me." if his age is greater than yours.
Print "Petros is my age" if his age equals yours.
"""
petros_age = 20

if petros_age < my_age:
    print("Petros is younger than me.")
if petros_age > my_age:
    print("Petros is older than me.")
if petros_age == my_age:
    print("Petros is my age")


"""
Problem 6.

Create a string variable.
Transform it into integer.
"""
var = '47567'
print(float(var))
