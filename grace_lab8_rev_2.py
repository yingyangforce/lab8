#+------------------------------+
#| lab8_rev_2.py - Isaiah Grace |
#+------------------------------+

# Review Task 2 - Make 4 x 5 list from L1

L1 = [
    ['A','B','C'],
    ['D','E','F','G'],
    ['H','I','J','K','L'],
    ['M','N','O'],
    ['P','Q','R','S'],
    ['T']
]

L2 = []
L3 = []

for sublists in L1:
    L3 += (char for char in sublists)

for i in range(0, len(L3), 5):
    L2.append(L3[i:i+5])

print(L2)