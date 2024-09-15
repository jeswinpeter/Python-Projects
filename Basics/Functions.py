# Exercise 1: Hello, World!
# Write a function that takes no arguments and prints "Hello, World!" to the console.

def Hello_world():
    print("---- Hello World ----")

Hello_world()

# Exercise 2: Add Two Numbers
# Write a function that takes two arguments, a and b, and returns their sum.

# def add(a = 5, b = 10):
#     print(a + b)

# add()
# add(3,2)

# Exercise 3: Greet a Person
# Write a function that takes a single argument, name, and 
# prints a personalized greeting message to the console.

# def greetings(name):
#     print("---- Greetings ", name, "----")
#     print("Have a nice day")

# name = input("Enter your name -> ")
# greetings(name)

# Exercise 4: Calculate the Area of a Rectangle
# Write a function that takes two arguments, length and width, 
# and returns the area of a rectangle with those dimensions.

def rectangle(l, b):
    print("The Area of the Rectangle =", l * b)
    return l * b

length = int(input("Enter Length of the Rectangle -> "))
width = int(input("Enter width of the Rectangle -> "))

area = rectangle(length, width)
# print(area)