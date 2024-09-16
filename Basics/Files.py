# Opening and Reading from a file

file = open('D:/Text_file.txt', 'r')

comment = file.read()
print(comment)

file.close()

# trying out write mode

with open('D:/Text_file.txt', 'w') as file:
    file.write('Checking write mode')

# with open('D:/Text_file.txt', 'a') as file:
#     file.append