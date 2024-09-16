# Opening and Reading from a file

# file = open('D:/Text_file.txt', 'r')

# comment = file.read()
# print(comment)

# file.close()

# trying out write mode

with open('D:/Text_file.txt', 'w') as file:
    file.write('Checking write mode')

# -- Trying append mode -- #

with open('D:/Text_file.txt', 'r') as file:
    content = file.read()
    print(content)
print("------------------------------")

with open('D:/Text_file.txt', 'a') as file:
    file.write("\nTesting Append Mode")

with open('D:/Text_file.txt', 'r') as file:
    content = file.read()
    print(content)
