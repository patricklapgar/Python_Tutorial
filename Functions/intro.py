from random import random
# Functions are the building blocks of Python programs
# They're also pretty easy to build
# Officially, functions are a nice block of code that can be reused at any time
# The output depends on the input

# Functions allow you as the programmer to write DRY code
# - Don't
# - Repeat
# - Yourself

# #####################################
# FUNCTION STRUCTURE
# #####################################

# def name_of_function():
    # Block of code

def say_hi():
    print("Hi")

say_hi()

# #####################################
# THE RETURN KEYWORD
# #####################################

# Examples

def print_square_of_7():
    print(7**2)

print_square_of_7()

def square_of_7():
    # The return keyword is necessary in your function to give an output
    return 7**2

# A few things to know about the 'return' keyword
# - It exits the function
# - It outputs whatever value is placed after the return keyword
# - It pops the function off the call stack

# ################################################
# COIN TOSS EXAMPLE
# ################################################

def flip_coin():
    # generate random number 0-1
    r = random()
    if r > 0.75:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())

def generate_evens():
    print([num for num in range(1, 50) if num % 2 == 0])

generate_evens()