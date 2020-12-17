# There are dictionary comprehensions just like with lists
# The syntax is similar, but also different
# 
# These two areas are for
# key-value pairs
#   |   |
#   V   V
# {___:___for___in___}

# Dict comprehensions will iterate over keys by default
# But you can also iterate over kays and values using the .items() method

# Example
numbers = dict(first=1, second=2, third=3)
# This is a dict comprehension
# The key stays the same, but the value is changed
squared_numbers = {key: value ** 2 for key,value in numbers.items()}

# Another example
# This one squares each value in the array 
{num: num**2 for num in [1, 2, 3, 4, 5]}

# Another example
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo) # Returns {'A': '1', 'B': '2', 'C': '3'}

# #####################################################
# Dictionary comprehensions witih conditional logic
# #####################################################

# Example
num_list = [1, 2, 3, 4]
# Remember this is the 
# key                   And this is the value
# |                     |
# V                     V
{ num:("even" if num % 2 == 0 else "odd") for num in num_list }

# Another example
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# Here's a great example of using a dictionary comprehension
def multiple_letter_count(string):
    """
    A simple function that returns a dictionary containing the number of times a letter appears in a phrase.
    """
    return {letter.lower(): string.count(letter.lower()) for letter in string}

print(multiple_letter_count("awesome")) # Returns {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}