import sys
import re


x = sys.stdin.read().strip().split('\n\n')

def T(g):
    return list(map(list, zip(*g)))

def p2(g):
    g = [list(x) for x in g.split('\n')]
    s = 0
    row = mirr(g)
    if row != -1:
        return 100*row
    g = T(g)
    col = mirr(g)
    if col != -1:
        return col

def mirr(g):
    rows = len(g)
    cols = len(g[0])
    g = [''.join(x) for x in g]
    for i in range(len(g)-1):
        diffs = 0
        for j in range(len(g)):
            spec = i+1+i-j
            if spec not in range(rows):
                continue
            if g[j] != g[spec]:
                for k in range(cols):
                    if g[j][k] != g[spec][k]:
                        diffs+=1
        if diffs == 2:
            return i+1
    return -1


print(sum([p2(g) for g in x]))
