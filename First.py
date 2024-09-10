# --- Basic Printing, data types 
print("---- Learning Python Basics -----")
    
name: str = "Hydra"
age: int = 100

name2 = "Tom"

#Trying out Multi line Printing
comment = """HI there
    Starting to learn Python"""

#Formated printing with Multi line printing
mail = """
Hail {},
My name is {}
hail {}
"""

print(mail.format(name,name2,name))

check = True
PI = 3.14

print(type(PI))
print(type(check))
print("Name -" ,name , "Age -" ,age)
print(comment)


