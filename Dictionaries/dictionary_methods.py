# ################################
# DICTIONARY METHODS
# ################################

# Just like with lists, there are some built-in methods to use with dictionaries
# The first one is clear()
# It's very straightforward. All it does is clear a dictionary of its values and keys leaving behind an empty object
d = dict(a=1, b=2, c=3)
d.clear()
print(d) # Returns {}

# The copy() method makes a copy of a dictionary
d = dict(a=1, b=2, c=3)
c = d.copy()
print(c)
c is d # Returns False

# The next method is called fromkeys()
# What it does is crate key-value pairs from comma separated values:
# For example:
# We're calling this from an empty object, but we can also use the dict keyword to initialize an empty dictionary
# |
# V
{}.fromkeys("a", "b") # {'a', 'b'}
{}.fromkeys("a", [1, 2, 3, 4, 5, 6]) # A dictionary of lists 
# This is a special case where if the key is a list, the fromkeys() method 
# will iterate through the list giving each iterable a value of 'unknown'
{}.fromkeys(["email", "username", "password"], "unknown")

# Another method is the get() method. Again, it's pretty straightforward and it retrieves a key in and object but returns None instead of an error if that key doesn't exist
d = dict(a=1, b=2, c=3)
d.get('a') # 1
d.get('d') # None

# #######################################
# MORE METHODS
# #######################################
# There are 3 other important methods to know for Python development

# The next one is the pop() method. Just like how you use the pop method for a list to remove a single element
# You can use this method to remove values from a dictionary
# However, this method takes a single argument that corresponds with a key
# and it removes the key-value pair from the dictionary. The pop method returns the value that was removed
# Example:

d = dict(a=1, b=2, c=3)
d.pop('a') # Returns 1
print(d) # Returns {'c': 3, 'b': 2}

# Now if you want to remove a random key in a dictionary, use the popitem() method

d = dict(a=1, b=2, c=3, d=4, e=5)
# Quick note: popitem() takes no arguments
d.popitem() # Removes a randome key-value pair

# Lastly, there's the update() method which updates keys and values in a dictionary with another key-value pair
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}
# Using the update method will override all key-values that you've already written in the dictionary
second.update(first)
print(second) # Returns {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# You can overwrite existing keys
second['a'] = "HELLO"
