# Variables are just symbols with a value
# They can be various data types

x = 100
num = 1
print(num + x) # Prints 101

# Variables are static!! They can change and are not constantly set!
# Variables can be assigned to other variables and reassigned again at any time
# You can also assign different variables to different values at the same time
num1, num2, num3 = 1, 2, 3

# NAMING RESTRICTIONS
# - Variables must start with a letter or underscore
# - The rest of the name must consist of letters, numbers, or underscores
# - Names are case-sensitive
# Most variables should be snake_case... e.g.
first_num_variable = 10 #This is snake case, different from camel case
# If the letters are capitalized, then they refer to a constant variable (e.g. PI = 3.14)

# UpperCamelCase usually refers to a class
# Variables that start and end with 2 underscore, __, are called dunder and are private and, or, meant to be left alone
__no_touch__ = "No touch"

# DATA TYPES
# There are multiple data types used in python, the most common are:
# - bool: True or False values
# - int: an integer
# - str: (string) a sequence of Unicode characters, e.g. "Patrick"
# - list: an ordered sequence of values of other data types, e.g. [1, 2, 3] or ["a", "b", "c"]
# - dict: a collection of key and value pairs, e.g {"first_name": "Patrick", "last_name": "Apgar"}

# DYNAMIC TYPING
# Python is very flexible about reassigning variables to different types
# Languages like C++ are statically typed and variables are stuck with their originally-assigned type
# Python is different, Python uses dynamic typing in which variables can changes types easily

var = True
print(var)

var = "I'm a string now"
print(var)

var = 22 // 7
print(var)

# There's also a value called None. None is basically the equivalent of null that you see in other languages
variable = None
