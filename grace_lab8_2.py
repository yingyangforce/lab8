#+--------------------------+
#| lab8_2.py - Isaiah Grace |
#+--------------------------+

# Task 2 - Print sum of all salaries

datasum = 0

datafile = open("lab8_data.txt")

for lines in datafile:
    members = lines.split()
    datasum += int(members[2])

print(f"Salary sum: ${datasum}.")