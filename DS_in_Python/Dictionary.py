# team_A = {'Score' : 0}
# team_B = {'Score' : 0}

# team_A['Score'] = input("Enter sore achived by team A: ")
# team_B['Score'] = input("Enter sore achived by team B: ")

# print(f"Team A has scored {team_A['Score']} points")
# print(f"Team B has scored {team_B['Score']} points")

# if team_A['Score'] > team_B['Score'] :
#     team_A['Position'] = '1st'
#     team_B['Position'] = '2nd'
#     print(f"Team A has secured {team_A['Position']} position")
# else:
#     team_B['Position'] = '1st'
#     team_A['Position'] = '2nd'
#     print(f"Team B has secured {team_B['Position']} position")

# LOOPING through the Dictionary
fav_subject = {}

i = 0

while i < 4:
    name_1 = input("Enter Name: ")
    fav_subject[name_1] = input("Enter favorite Subject: ")
    i += 1

# Printing dictionary using a loop
for key, value in fav_subject.items(): 
    print(f"\nKey: {key}")
    print(f"Value: : {value}")

for k in fav_subject.keys():
    print(k.title())