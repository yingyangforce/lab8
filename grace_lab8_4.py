#+--------------------------+
#| lab8_4.py - Isaiah Grace |
#+--------------------------+

# Task 4 - Append data to lab8_data.

newemps = [
    (304, "Yulia", 91000),
    (305, "Ruben", 88000)
]

datafile = open("lab8_data.txt", 'a')

datafile.write('\n')

for tuples in newemps:
    newline = " ".join(str(member) for member in tuples)
    datafile.write(newline + '\n')