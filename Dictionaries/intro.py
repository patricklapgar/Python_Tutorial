# #########################################
# LISTS VS DICTIONARIES
# #########################################

# Lists are very good for storing values of the same data type
# With dictionaries, you can store more information and describe it with more detail
# At its core, a dictionary consists of key value pairs
# You use keys to describe the data, and values to represent the data

first_dictionary = {
#    Key    Value
    # |       |
    # V       V
    "name": "Patrick",
    "is_human": True,
    "native_language": "English",
    "age": 20
}

# Another way to create a dictionary is to use the dict function. 
# You assign values to keys by passing in keys and values separated by =
another_dictionary = dict(key = "Patrick", age = 21, native_language = "English")

# ########################################
# ACCESSING DICTIONARY VALUES
# ########################################
# You can access values in a dictionary the same way you can access values within a list

insctructor = {
    "name": "Patrick",
    "age": 20,
    "is_human": True,
    "favorite_food": "tacos",
    "owns_pet": True
}

# Unlike lists, you use the key to find its corresponding value in a dictionary
print(insctructor["name"]) # Returns "Patrick"

# #######################################
# ITERATING OVER DICTIONARIES
# #######################################

# You can retrieve all values of a dictionary through the proecss of iteration
# You can use a for loop! 
# There's a very important method to use with dictionaries that will retrieve the values! 
# It's called .values() and you use it like so

insctructor = {
    "name": "Patrick",
    "age": 20,
    "is_human": True,
    "favorite_food": "tacos",
    "owns_pet": True
}

for value in insctructor.values():
    print(value)

# You can also do the same thing but with the keys instead
for key in insctructor.keys():
    print(key)

# Sometimes, you'll also wanna access both the keys and the values. To do so, use the .items() method
# Because you now have 2 pieces of data, use 2 separate variables in your for loop
for key, value in insctructor.items():
    print(f"key is {key} and value is {value}")

# QUICK NOTE
# There's a way to check if a value exists within a dictionary or not
# Just like with lists, you can use the 'in' keyword to see if a value exists within a dictionary

insctructor = {
    "name": "Patrick",
    "age": 20,
    "is_human": True,
    "favorite_food": "tacos",
    "owns_pet": True
}

# This is how you can test it with keys
"name" in insctructor # Returns True
"favorite_color" in insctructor # Returns False

# If you want to know if a certain value exists, you can use the .values() method again
"Patrick" in insctructor.values() # Returns True
"Apgar" in insctructor.values() # Returns False

