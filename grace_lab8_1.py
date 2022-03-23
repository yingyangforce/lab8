#+--------------------------+
#| lab8_1.py - Isaiah Grace |
#+--------------------------+

# Task 1 - Print only employee names from data file

textdata = open("lab8_data.txt")

for line in textdata:
    members = line.split()
    print(members[1])
