# Create a list called colors that contains the 
# following elements: 'red', 'green', 'blue', and 'yellow'. 
# Then, perform the following operations:
#   Print the entire list.
#   Access and print the second element of the list.
#   Append the element 'purple' to the end of the list.
#   Insert the element 'orange' at the second position of the list.
#   Remove the first occurrence of the element 'green' from the list.
#   Print the length of the list.

colors = ["red", "green", "blue", "yellow"]
print(colors)
print(colors[1])
colors.append("purple")
colors.insert(1, "orange")
colors.remove("green")
print(len(colors))