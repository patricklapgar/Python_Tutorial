from random import randint
# CONDITIONAL STATEMENTS
# if statements represent different paths a program can take based on some type of comparison of input

# if some condition is True:
#   do something
# elif some other condition is True:
#   do something
# else:
#   do something

# ex:
name = "Patrick"

# In Python, spacing matters a lot. You have to indent after the : of each conditional statement. Otherwise, you'll receive an error
if name == "Alexandra":
    print("Hey honey!")
elif name == "Patrick":
    print("That's me!")
else:
    print("What's your name")

# Another example
num = randint(1, 1000)

if num % 2 != 0:
    print("odd")
else:
    print("even")

# In python, all conditional checks resolve to True or False
# 'is' is another special keyword in python that works similarly to the == operator
# x = 1
# x is 1 // True
# x is 0 // False

# Values that will resolve to True can be known as "truthy", or values that will resolve to False can be known as "falsy"
#  Other things that are naturally falsy are:
# - Empty objects
# - Empty strings
# - The keyword 'None'
# - The number 0

# example
animal = input("Enter your favorite animal\n")

# Any string that isn't empty is truthy! However, if the string is empty, then the string is falsy
if animal:
    print(animal + " is my favorite too!")
else :
    print("You didn't say anything!!")

######################################
# COMPARISON OPERATORS
######################################
# Examples of some comparison operators
# == - Equality operator
# != - The NOT operator
# >, < - greater than / less than operators
# >=, <= - greater than or equal / less than or equal operators

if 1 > 0:
    print("1 is greater than 0")

# LOGICAL OPERATORS
# Logical operators in Python are keywords instead of actual symbols like you would use in C or Java
# and - AND operator
# or  - OR operator
# not - NOT operator

# EXAMPLE
# if a and b:
#     print(c)

# if am_tired or is_bedtime:
#     print("Go to sleep")

# if not is_weekend:
#     print("go to work!")

# You can also use comparison operators and connect them via logical operators
state = input("Which state do you live in?\n")
city = input("Where do you live?\n")
if state == "texas":
    if city == "dallas" or city == "houston":
        print("Howdy! You're a Texan living in " + city)
    elif city == "san antonio":
        print("You in san antonio!")
    elif city == "austin":
        print("WOW! You live in the state capital!")
else:
    print("well... you're not a Texan, but you're still cool!")

# is vs. "=="
# The 'is' keyword tests for equality
# In Python, "==" and "is" are similar but not the same
# == checks if the values are the same
# Meanwhile, the "is" keyword checks if the values are stored in the same memory location
# a = [1, 2, 3]
# b = [1, 2, 3]
# a == b # True
# a is b # False, because the two lists are stored in different memory locations