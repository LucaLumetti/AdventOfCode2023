import sys
import re

rx = re.compile(r'\d+')

x = sys.stdin.read().strip().split('\n')
x = [list(k) for k in x]

empty_cols = []
empty_rows = []

for row in range(len(x)):
    if '#' not in x[row]:
        empty_rows.append(row)

for col in range(len(x[0])):
    emp = True
    for row in range(len(x)):
        if x[row][col] == '#':
            emp = False
    if emp:
        empty_cols.append(col)


idx = 1
gal_idxs = []
for row in range(len(x)):
    for col in range(len(x[0])):
        if x[row][col] == '#':
            gal_idxs.append((row, col))
            x[row][col] = f'{idx}'
            idx += 1

p1_total = 0
p2_total = 0
for i,a in enumerate(gal_idxs):
    for j,b in enumerate(gal_idxs):
        if i >= j:
            continue
        dist = 0
        for r in empty_rows:
            if a[0] < r < b[0] or b[0] < r < a[0]:
                dist+= 1
        for c in empty_cols:
            if a[1] < c < b[1] or b[1] < c < a[1]:
                dist += 1

        man_dist = abs(a[0]-b[0]) + abs(a[1]-b[1])
        p1_total+=man_dist+dist
        p2_total+=man_dist+dist*999999

print(p1_total)
print(p2_total)
