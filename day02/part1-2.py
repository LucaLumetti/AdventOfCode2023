import sys
import re


x = sys.stdin.read().strip().split('\n')
x = [re.findall(r'(\d+) (blue|red|green)', k) for k in x]
p1_sol = 0
p2_sol = 1
for i, g in enumerate(x, 1):
    valid = True
    found = {'red':0, 'green':0, 'blue':0}
    for q, c in g:
        q = int(q)
        found[c] = max(found[c], q)
    valid &= found['red'] <= 12
    valid &= found['green'] <= 13
    valid &= found['blue'] <= 14
    p1_sol += i*valid
    p2_sol += found['red']*found['green']*found['blue']
print(p1_sol)
print(p2_sol)


