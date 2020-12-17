# Object Oriented Programming (OOP) is a way of thinking how to write/organize code
# It's really not as hard as it seems

# Two key terms you MUST know of are classes and objects
# OOP is way to programmatically recreate anything you can think of (i.e. a dog, car, even computer processors, and etc)
# You do this using classes and objects.

# A class is like a blueprint for objects. They can contain methods (aka functions) and different properties (aka attributes)
# Additionally, an object is also known as an 'instance' of a class.
# Now, the term 'instance' can sound confusing for some, but really what it is a variable that uses the class we create

# Firstly, an example of a class is shown below

class Dog:
    def __init__(self):
        pass

    def bark(self):
        print("Bark")

# Next, is an object (or 'instance') of the class 'Dog'
pitbull = Dog() # <-- This is an object. See, it's a variable that uses the class we make
pitbull.bark() # Prints "Bark"

### ABSTRACTION AND ENCAPSULATION (Big Topics!!)
# Remember: The reason why OOP is used is because it makes writing simpler and more organized

# With object oriented programming, the end goal is to build your code
# in a logical, organized manner. You do this by putting your classes into hierarchical groups

# Now on to the good stuff! Encapsulation is basically when both public and 'private' methods 
# are grouped together into one single class. 
# I mentioned both public and 'private' methods. By that, I mean private methods are methods that are 
# intended only for the class you build. They won't and shouldn't be accessed by you, the programmer.
# Encapsulation is very useful in that it allows for abstraction

# Now, abstraction is when you build a class, but you expose the relevant functions for the programmer to use and you hide the private methods.
# You would only hide private methods

# Here's an example of everything I've just talked about!
# Example: User class

class User:
#   This is the __init__ function.
#
#       |   |   |
#       V   V   V
    def __init__(self, username, password):
        pass

user1 = User()
