#+--------------------------+
#| lab8_3.py - Isaiah Grace |
#+--------------------------+

# Task 3 - read data into list, give 10% raise
#          write all to new file, "lab8_updated".

lab_data = open("lab8_data.txt")
updated = open("lab8_updated.txt", 'a')

for lines in lab_data:
    lines = lines.split()
    lines[2] = str(int(lines[2]) + (int(lines[2]) * .10))
    updated.write(" ".join(lines) + '\n')
