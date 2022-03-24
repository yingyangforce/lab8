#+------------------------------+
#| lab8_rev_1.py - Isaiah Grace |
#+------------------------------+

# Review Task 1 - Print list contents w/o whitespace

L1 = [
    ['A','B','C'],
    ['D','E','F','G'],
    ['H','I','J','K','L'],
    ['M','N','O'],
    ['P','Q','R','S'],
    ['T']
]

for lists in L1:
    letters = "".join(char for char in lists)
    print(letters, end='')

print('\n')