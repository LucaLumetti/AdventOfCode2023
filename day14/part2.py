import sys
import re

N = 1000000000

def T(g):
    return list(map(list, zip(*g)))

def R(g):
    return [l[::-1] for l in g]

rx = re.compile(r'\d+')

x = sys.stdin.read().strip().split('\n')
g = [list(k) for k in x]

def better_better_move_stone(g):
    rows = len(g)
    for row in range(rows):
        gr = ''.join(g[row])
        while '.O' in gr:
            gr = re.sub(r"(\.+)(O+)",r"\2\1", gr)
        g[row] = gr
    return g

def better_move_stone(g):
    rows = len(g)
    cols = len(g[0])
    for row in range(rows):
        for _ in range(cols):
            g[row]=''.join(g[row]).replace('.O', 'O.')
    return g

def move_stone(g):
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
    return g

states = {}
n = 0
while n < N:
    key = ''.join([''.join(k) for k in g])
    if key in states:
        cycle_length = n-states[key]
        n += ((N-n)//cycle_length)*cycle_length
    states[key] = n

    g = T(g)
    g = better_better_move_stone(g)
    g = T(g)
    g = better_better_move_stone(g)
    g = R(T(g))
    g = better_better_move_stone(g)
    g = R(T(R(g)))
    g = better_better_move_stone(g)
    g = R(g)
    n += 1

rows = len(g)
cols = len(g[0])

total = 0
for row in range(rows):
    for col in range(cols):
        if g[row][col] == 'O':
            total += rows-row

print(total)
