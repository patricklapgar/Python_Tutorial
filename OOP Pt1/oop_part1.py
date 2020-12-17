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

