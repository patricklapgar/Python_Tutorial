# How to convert one data type to another
# It's actually pretty straightforward
# In string interpolation, data types are converted into string form, so that's a form of data type conversion

# You can also use built-in functions to convert variables
decimal = 12.563
integer = int(decimal) # returns 12
string = str(decimal) # returns '12'
print(integer)
print(string)

my_list = [1, 2, 3]
my_list_as_a_string = str(my_list)
print(my_list_as_a_string)