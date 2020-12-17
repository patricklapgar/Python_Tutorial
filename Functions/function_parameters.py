# Parameters, aka arguments, are very simple to understand. They are the input of functions 
# that return a certain output

def square(num):
    return num**2

print(square(4))

# You can use multiple parameters in a function that can be used for different purposes
def sum(a, b):
    return a + b

# When you name parameters, it's best practice to be as specific as possible in regards to what the argument is and 
# what it'll do

# Not a good example
def print_full_name(string1, string2):
    return(f"Your name is {string1} {string2}")

# A better example
def print_full_name(first_name, last_name):
    return(f"Your full name is {first_name} {last_name}")

# There's actually a technical difference between parameters and arguments:
# - A parameter is a variable in a method definition
# - But when a method is called, the arguments are the data you pass into the method's parameters
# - In other words, a parameter is a variable in the declaration of the function
# - And an argument is the actual value of this variable that gets passed to function

# ###############################################
# DEFAULT PARAMETERS
# ###############################################
# A default parameter is basically a standard parameter that will always have a default value but will be
# overridden if another value is present

#               This is a default parameter
#                       |
#                       V
def exponent(num, power=2):
    return num ** power

print(exponent(2, 3))
# So now if a power argument isn't specified, the default value will always be 2
print(exponent(2))

# Default parameters can be anything really, including other functions!
def add(a, b):
    return a + b

# This is how functions are used in default parameters
# Quick note, it is best practice to put all functions at the END of each statement
def math(a,b, fn=add):
    # Call the function parameter here
    return fn(a, b)


def subtract(a, b):
    return a - b

math(2, 2) # Returns 4
math(2, 2, subtract) # Returns 0

def speak(animal="dog"):
    noises = {"dog":"woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    return noises.get(animal, '?')

speak("dog")

# ############################################
# KEYWORD ARGUMENTS
# ############################################

# Keyword arguments are similar to default parameters in syntax, but you
# can specify function arguments directly in the function call. 
# This makes them different from default parameters

def full_name(first, last):
    return f"Your name is {first} {last}"

full_name(first='Patrick', last='Apgar')

# Keyword arguments are actually very useful when passing in dictionaries into functions and unpacking its values
# They are also really flexible

# ############################################
# SCOPE
# ############################################
# Scope is an area of code where certain variables and parameters can be used
# When you write a function that holds a parameter, that parameter variable is only available inside of that function
# Variables that are written outside of classes, functions, and so forth have global scope

# Example
total = 0

def increment():
    total += 1
    return total

increment()

# The code above won't work because the function is looking for a variable that has a local scope
# So far, the total variable has a global scope. Usually the use of global variables should be minimized, but if you want to use global variables
# you must use the 'global' keyword

total = 0
def increment():
    # The global variable is referenced here. You must initialize it first before anything else
    global total 
    total+=1
    return total

increment()

# Then there's another keyword called 'nonlocal' and what it does is that 
# it lets you modify a parent's variables in a child (or nested) function
# Example

def outer():
    count = 0
    def inner():
        # See, now you have access to the count variable
        nonlocal count
        count += 1
        return count
    return inner()

# ####################################################
# DOCUMENTING FUNCTIONS
# ####################################################
# Python has a special syntax when you have to document complex functions
# Essentially, use triple double quotes to write your comments """..."""

def say_hello():
    """ A simple function that returns the string hello """
    return "Hello!"

# You can also use more special syntax to return the documentation within a function
# The .__doc__ keyword property retrieves all coments in a function
print(say_hello.__doc__) # Returns  'A simple function that returns the string hello' 

# Example
def return_day(day=1):
    days_in_week = {
        1: "Sunday", 
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    if day > 7 or day < 1:
        return None
    else:
        return days_in_week.get(day)

print(return_day(3))