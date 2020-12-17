# In Python there are also "escape characters", which are interpreted by Python to do something special
# e.g. \n is an escap sequence that creates a new line
new_line = "Hello\nWorld"
print(new_line)

# Some other escape sequences are:
# \b - backspace
# \r - carriage return
# \t - horizontal tab
# \v - vertical tab
# \' - single quote
# \" - double quote

# STRING CONCATENATIONS
str_one = "your"
str_two = "face"
str_three = str_one + " " + str_two # Returns 'your face'
# You CANNOT concatenate variables of different data types, you can only concatenate strings together

# FORMATTING STRINGS
# In Python, there are several ways to format strings to interpolate variables
# The new way is to use something called F-Strings
# e.g.
x = 10
# This is string interpolation, see how it easily allows you to concatenate numbers to a string
formatted = f"I've told you {x} times already!"
# You can even do some math in the brackets if you want to
print(formatted)

# Another example
guess = 8
name = "Patrick"
message = f"nice try {name}, but your guess of {guess} is incorrect"
print(message)

# There's also an alternative way to format strings and it's by using the format method
# e.g.

message2 = "I am {} years old".format(20)
# Another example
fruit = "banana"
ripeness = "unripe"
print("The {} is {}".format(fruit, ripeness))