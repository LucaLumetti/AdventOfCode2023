import sys
import re
import time

rx = re.compile(r'\d+')

def T(g):
    return list(map(list, zip(*g)))

grid = sys.stdin.read().strip().split('\n')
grid = [list(g) for g in grid]
rows = len(grid)
cols = len(grid[0])

D = {
    'r': (1, 0),
    'l': (-1,0),
    'u': (0, -1),
    'd': (0, +1)
}


def solve(beams):
    energ = [[0 for _ in range(cols)] for _ in range(rows)]

    _cache = set()
    while len(beams) > 0:
        x, y, d = beams.pop()
        if (x, y, d) in _cache: continue
        _cache.add((x, y, d))

        if y >= rows or x >= cols: continue
        if y < 0 or x < 0: continue

        # cgrid = [c.copy() for c in grid]
        # cgrid[y][x] = 'O'
        # print('\n'.join([''.join([str(a) for a in e]) for e in cgrid]))
        # print(x, y, d, len(beams))
        # print()
        # time.sleep(.5)

        elem = grid[y][x]
        energ[y][x] = 1

        dx, dy = D[d]

        if elem == '.':
            d = d

        elif elem == '/' and d == 'u':
            d = 'r'
        elif elem == '/' and d == 'd':
            d = 'l'
        elif elem == '/' and d == 'l':
            d = 'd'
        elif elem == '/' and d == 'r':
            d = 'u'

        elif elem == '\\' and d == 'u':
            d = 'l'
        elif elem == '\\' and d == 'l':
            d = 'u'
        elif elem == '\\' and d == 'd':
            d = 'r'
        elif elem == '\\' and d == 'r':
            d = 'd'

        elif elem == '-' and d in ['l','r']:
            d = d
        elif elem == '|' and d in ['u', 'd']:
            d = d

        elif elem == '-' and d in ['u', 'd']:
            dx, dy = D['l']
            beams.append((x+dx, y+dy, 'l'))
            dx, dy = D['r']
            beams.append((x+dx, y+dy, 'r'))
            continue

        elif elem == '|' and d in ['l', 'r']:
            dx, dy = D['u']
            beams.append((x+dx, y+dy, 'u'))
            dx, dy = D['d']
            beams.append((x+dx, y+dy, 'd'))
            continue

        dx, dy = D[d]
        beams.append((x+dx, y+dy, d))

    total = 0
    for r in energ:
        for c in r:
            total += c
    return total

print(solve([(0, 0, 'r')]))
total = 0
for y in range(rows):
    total = max(total, solve([(0, y, 'r')]))
    total = max(total, solve([(cols-1, y, 'l')]))
for x in range(cols):
    total = max(total, solve([(x, 0, 'd')]))
    total = max(total, solve([(x, rows-1, 'u')]))
print(total)
