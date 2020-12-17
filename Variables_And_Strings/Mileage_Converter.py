print("How many kilometers did you run today?")

# input() is a function that accepts user input in the command line
kilometers = float(input())
conversion_variable = 1.60934
miles = kilometers / conversion_variable

# The round() function is a function that rounds a certain number by a different number of decimal places
# round(thing to round, how many decimal points to round to)
miles = round(miles, 2)

print(f"Your {kilometers} km ride is equal to {miles} mi")