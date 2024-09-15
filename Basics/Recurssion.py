# ---- Exercise 1: Recursive Sum ----
#
# Write a recursive function recursive_sum that takes a list of integers as 
# input and returns the sum of all elements in the list.

#sum = 0

def rec_sum(n, array):
    if n == 0:
        return 0
    else:
        return array[n-1] + rec_sum(n - 1, array)

test = []
size = int(input("Enter no elements in the list -> "))

print("Enter Elements to the list :")
for i in range(0,size):
    test.append(int(input(f"Num {i + 1} -> ")))

result = rec_sum(size, test)
print(f"The sum of elements of the list = {result}")