# Here, you'll learn about the * and ** operators and how to use them as parameters both inside and outside of a function

# ################################################
# *args
# ################################################

# *args are a special type of operator that you can pass to functions
# It gathers remaining arguments as a tuple

# Example
#           Here, the *args parameter basically can take all other parameters that
#           would be in the function call.
#           It returns a tuple containing all of the arguments you pass into the function call
#                   |
#                   V
def sum_all_nums(*args):
    # Because *args is a tuple, you must iterate through it to use its values
    total = 0
    for num in args:
        total += num

    return total

print(sum_all_nums(4, 6, 8, 7, 9))

# Another example but with strings
def contains_purple(*args):
    if "purple" in args:
        return True
    return False

contains_purple("purple", False, 21) # Returns True
contains_purple(True, 20, "hello world") # False

# ###################################################
# **kwargs
# ###################################################
# The full name is called keyword args 
# Instead of collecting all forms of arguments, it will only collect the keyword arguments
# and store the values in a dictionary

# Example
def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")

fav_colors(patrick="green", alexandra="red")

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting david"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who this is"

# Another example
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return f"{kwargs['prefix']} {word}"
    elif "suffix" in kwargs:
        return f"{word} {kwargs['suffix']}"
    else:
        return word

combine_words("patrick", prefix="Mr.") # Returns Mr. Patrick

# ###################################################################
# Parameter Ordering
# ###################################################################
# 
# There's a certain ordering of parameters in functions that you MUST follow
# otherwise you'll run into bugs and errors much more frequently 
# 
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

# #########################################################
# Tuple Unpacking
# #########################################################

# Instead of using * as a parameter for args and kwargs, you can also use * to 'unpack' arguments
# The term 'unpack' means to retrieve all values within the *args parameter

# Example
#          Remember that the *args parameter returns a tuple
#                    |  
#                    V
def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

# Below, there's a list of numbers that is going to passed into the function
# However, passing in the list normally will return an error
nums = (1, 2, 3, 4, 5, 6)

# The * operator 'unpacks' each individual value and passes them as 
# individual arguments in the function
sum_all_values(*nums) # Returns 21

# Another example
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

result1 = count_sevens(1, 4, 7)

result2 = count_sevens(*nums)

# #################################################################
# Dictionary Unpacking
# #################################################################

# Now you can also use ** to unpack dictionaries into keyword arguments
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}
print(display_names(**names))

def dipslay_info(id, name, info, **kwargs):
    return f"Id: {id}, Name of User: {name}, User Info: {info}, Other: {kwargs}"

info = {
    "id": 123,
    "name": "Patrick",
    "info": ["blue", "5'11", 20, "Bachelor's Degree"]
}

print(dipslay_info(**info, marital_status='married'))

    