#-------------- EXERSISE 1 -----------------
# Try writing a Python program that takes an integer input from the user and prints "You are an adult" 
# if the age is 18 or older, and "You are a minor" otherwise.
# Here's a hint: you can use the int() function to convert the input to an integer,
#  and an if-else statement to make the decision."""

age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# #--------------- EXERSISE 2 ---------------
"""Python program that takes a string input from the user and prints "Hello, <name>!" 
    if the input is not empty, and "Please enter your name" otherwise."""

name = input("Enter your name ").strip()

if name != "":
    print("Hello, "+name) 
else:
    print("Please enter your name")


#------------- EXERSISE 3 --------------
# Try writing a Python program that takes two integer inputs from the user
# and prints "The numbers are equal" if they are equal, and "The numbers are not equal" otherwise.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a == b :
    print("The numbers are equal")
else:
    print("The numbers are not equal")