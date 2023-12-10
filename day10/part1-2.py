import sys

UP = 0-1j
DOWN = 0+1j
RIGHT = 1
LEFT = -1

x = sys.stdin.read().strip().split('\n')
x = [list(k) for k in x]

def find_start():
    for r in range(len(x)):
        for c in range(len(x[0])):
            if x[r][c] == 'S':
                return c+r*1j
    assert False

def get_com(a, com):
    x = int(com.real)
    y = int(com.imag)
    h = len(a)
    w = len(a[0])
    if x < 0 or x > w: return '.'
    if y < 0 or y > h: return '.'
    return a[y][x]

def get_trbl(x, pos):
    tt = get_com(x, pos+UP)
    rr = get_com(x, pos+RIGHT)
    bb = get_com(x, pos+DOWN)
    ll = get_com(x, pos+LEFT)
    return tt,rr,bb,ll


s = find_start()

t, r, b, l = get_trbl(x, s)
dir = 0

if t in '|F7':
    dir = -1j
elif r in '-J7':
    dir = 1
elif b in '|JL':
    dir = 1j
elif l in '-FL':
    dir = -1

steps = 0
prev = 'S'
actual = get_com(x, s)
visit = {s}

while actual != 'S' or steps == 0:
    s += dir
    visit.add(s)
    steps += 1
    actual = get_com(x, s)
    assert actual != '.'

    if dir == RIGHT and actual == '7': dir = DOWN
    if dir == RIGHT and actual == 'J': dir = UP
    if dir == DOWN and actual == 'J': dir = LEFT
    if dir == DOWN and actual == 'L': dir = RIGHT
    if dir == LEFT and actual == 'L': dir = UP
    if dir == LEFT and actual == 'F': dir = DOWN
    if dir == UP and actual == 'F': dir = RIGHT
    if dir == UP and actual == '7': dir = LEFT
    prev = actual

print(steps//2)

for r in range(len(x)):
    for c in range(len(x[0])):
        if (c+r*1j) not in visit:
            x[r][c] = '.'

double_x = [[' ']*(len(x[0])*2) for _ in range(len(x)*2)]
for r in range(len(x)):
    for c in range(len(x[0])):
        d = x[r][c]
        if d == '|':
            double_x[r*2][c*2] = '|'
            double_x[r*2+1][c*2] = '|'
            double_x[r*2][c*2+1] = ' '
            double_x[r*2+1][c*2+1] = ' '
        if d == '.':
            double_x[r*2][c*2] = ' '
            double_x[r*2][c*2+1] = ' '
            double_x[r*2+1][c*2+1] = '.'
            double_x[r*2+1][c*2] = ' '
        if d == '-':
            double_x[r*2][c*2] = '-'
            double_x[r*2][c*2+1] = '-'
            double_x[r*2+1][c*2+1] = ' '
            double_x[r*2+1][c*2] = ' '
        if d == '7':
            double_x[r*2][c*2] = '7'
            double_x[r*2+1][c*2] = '|'
            double_x[r*2][c*2+1] = ' '
            double_x[r*2+1][c*2+1] = ' '
        if d == 'F':
            double_x[r*2][c*2] = 'F'
            double_x[r*2][c*2+1] = '-'
            double_x[r*2+1][c*2] = '|'
            double_x[r*2+1][c*2+1] = ' '
        if d == 'L':
            double_x[r*2][c*2] = 'L'
            double_x[r*2][c*2+1] = '-'
            double_x[r*2+1][c*2] = ' '
            double_x[r*2+1][c*2+1] = ' '
        if d == 'J':
            double_x[r*2][c*2] = 'J'
            double_x[r*2][c*2+1] = ' '
            double_x[r*2+1][c*2] = ' '
            double_x[r*2+1][c*2+1] = ' '
        if d == 'S':
            double_x[r*2][c*2] = 'S'
            double_x[r*2][c*2+1] = ' '
            double_x[r*2+1][c*2] = ' '
            double_x[r*2+1][c*2+1] = '|'

cnt = 0
for r in range(len(double_x)):
    inside = False
    for c in range(len(double_x[0])):
        if double_x[r][c] == '|': inside = not inside
        if double_x[r][c] == '.':
            double_x[r][c] = 'I' if inside else 'O'
            cnt += inside


# print('\n'.join([''.join(k) for k in double_x]))
print(cnt)
