import sys
import re
import numpy as np
import cv2 as cv

rx = re.compile(r'([RLDU]) (\d+) \(\#([A-Za-z0-9]+)\)')

D = {
    'R': (1, 0),
    'L': (-1,0),
    'U': (0, -1),
    'D': (0, +1),
}

x = sys.stdin.read().strip().split('\n')
vertex = [[0, 0]]

for i, r in enumerate(x):
    m = rx.findall(r)
    m = m[0]

    c = m[2]
    dir = 'RDLU'[int(c[-1])]
    
    n = int(c[-7:-1], 16)

    dx, dy = D[dir]
    dx *= n
    dy *= n
    x, y = vertex[-1]
    vertex.append([x+dx, y+dy])

vertex = np.array(vertex)
vertex = vertex.reshape((-1, 1, 2))
area = cv.contourArea(vertex)
perimeter = cv.arcLength(vertex, closed=True)
print(int(area+perimeter//2+1))
