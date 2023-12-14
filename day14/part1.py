import sys

def T(g):
    return list(map(list, zip(*g)))

x = sys.stdin.read().strip().split('\n')
g = [list(k) for k in x]

g = T(g)

rows = len(g)
cols = len(g[0])
moved = True
while moved:
    moved = False
    for row in range(rows):
        for col in range(cols):
            if g[row][col] != 'O': continue
            if col-1 >= 0 and g[row][col-1] == '.':
                g[row][col-1], g[row][col] = g[row][col], g[row][col-1]
                moved = True

g = T(g)
total = 0
for row in range(rows):
    for col in range(cols):
        if g[row][col] == 'O':
            total += rows-row

print(total)
