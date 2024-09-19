# #--- Excerside 1 - ZeroDivisionError ---#

try:
    x = 10/0
except ZeroDivisionError:
    print("Cannot devide 10 by 0!!")
#--------------------------------------------


# #---- Excersise 2 - TypeError ----#

word = "Exception"
x = 10

try:
    print(word + x)
except TypeError:
    print("Cannot concatenate an int value with a string")
#---------------------------------------------


#---- Exercise 3: Catching a ValueError ----#

try:
    w = int(input("Enter value to convert -> "))
    print(f"{w} is a valid input")
except ValueError:
    print("Cannot convert string to an int")
#---------------------------------------------