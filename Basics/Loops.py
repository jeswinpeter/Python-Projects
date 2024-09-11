# Create a list called numbers that contains the following elements: 1, 2, 3, 4, and 5. 
# Then, use a for loop to iterate over the list and print the square of each number.

# Hint: You can use the ** operator to calculate the square of a number.

numbers = [1,2,3,4,5]

for square in numbers:
    print(square*square)

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