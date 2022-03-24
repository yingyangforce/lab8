#+------------------------------+
#| lab8_rev_3.py - Isaiah Grace |
#+------------------------------+

# Task 3 - Make deep copy, L3, of L1

import copy

L1 = [
    ['A','B','C'],
    ['D','E','F','G'],
    ['H','I','J','K','L'],
    ['M','N','O'],
    ['P','Q','R','S'],
    ['T']
]

L3 = copy.copy(L1)

L3[2] = ['A', 'A']

print(L1)
print(L3)