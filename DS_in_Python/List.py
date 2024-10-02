# List is ordered and mutable data structure
# Any data types are allowed
# duplicate elements are allowed

data = ["jan","feb","mar"]
print(f"initial: {data}") 

# first = data[0]
# sec = data[1]
# third = data[2]

# print(f"{first}, {sec}, {third}")

# print(len(data))

data.append("may")
print(f"After append: {data}") 

data.insert(3, "apr")
print(f"After append: {data}") 

# data.remove("jan")
# print(f"after rem: {data}")

#---- List of Methods on List ----#
# pop -> removes from end {item = data.pop()}
# .remove -> remove specific item {data.remove("element")}
# .clear -> Removes all elements
# .reverse -> guess what, it reverses the list
# .sort -> suffles the list "jk"


# ------ Tricks ------ #
# data = [1] * 5 ==>> [1,1,1,1,1] 
# use " + " to conccatenate

# ==== Slicing a List ===== #
new = data[1:3]                 #(Second value is not inclusive)
print(f"After Slicing: {new}")
## note => data[::2] -> starts at begning ends at end jumps of 2 steps
## note => data[::-1] -> reverses the list


num = [1, 2, 3, 4]
sqr = [i * i for i in num]
print(f"Numbers: {num}")
print(f"Squres: {sqr}")