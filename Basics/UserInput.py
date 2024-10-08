# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

# avl_cars = [ 'Toyota', 'Tata', 'Renault', 'Chevorlet', 'Benz' ]

# rent = input("What kind of a car would you like to rent: ")

# if rent in avl_cars:
#     print(f"Your {rent} car is ready for pick up sir")
# else:
#     print(f"Sorry a {rent} is not available right now")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.

prompt = "Hello, greetings to you!\nCould you please tell me how many people are"
prompt += "\nin your dinner group: "

group_size = int(input(prompt))

if group_size > 8:
    print("Sorry for the inconvinience you will have to wait")
else:
    print(f"Your table for {group_size} is ready")