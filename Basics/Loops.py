# Create a list called numbers that contains the following elements: 1, 2, 3, 4, and 5. 
# Then, use a for loop to iterate over the list and print the square of each number.

# Hint: You can use the ** operator to calculate the square of a number.

numbers = [1,2,3,4,5]

for square in numbers:
    print(square*square)

#------------- Exersise 2 --------------
# Exercise: Write a Python program to print the sum of all even numbers in a given list.
# List: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Task: Use a for loop to iterate over the list and print the sum of all even numbers.
# Hint: You can use the modulo operator (%) to check if a number is even.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for num in numbers:
    if (num % 2) == 0:
        sum = sum + num

print("Sum of the even numbers = ",sum)

#-------------- Exersise 3 --------------
#==== Infinite while loop ====
#Exercise 1: Infinite Loop Write a Python program that uses an infinite 
#loop to print the numbers from 1 to 10 repeatedly.

i = 1

while True:
    if i == 11:
        break
    
    print(i)
    i += 1

#-------------- Exersise 4 -------------
#Exercise 2: Loop Control Statement Write a Python program that 
# uses a for loop to iterate over the numbers 
# from 1 to 10, but skips the number 5 using a continue statement.

for j in range(1,11):
    if j == 5:
        continue

    print(j)

#------------- Exersise 5 ---------------
# Exercise 3: Real-World Example Write a Python program that uses a while 
# loop to prompt the user to enter their favorite color. If the user enters 
# anything other than "red", "green", or "blue", the program should ask again. 
# Once the user enters a valid color, the program should 
# print a message indicating that the color has been accepted.

while True:
    color = input("Enter your favorite color: ").strip().lower()

    if color == "red" or color == "green" or color == "blue":
        print("$$ Your color has been accepted $$")
        break