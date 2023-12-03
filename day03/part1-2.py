import sys
import re

rx = re.compile(r'\d+')

x = sys.stdin.read().split('\n')
sol = 0
from collections import defaultdict
sym_num = defaultdict(list)

for i, r in enumerate(x):
    for m in rx.finditer(r):
        n = int(m.group())
        s = m.start()
        e = m.end()
        c = []
        for k in range(s-1, e+1):
            c.append((i-1,k))
            c.append((i+1,k))
        c.append((i,s-1))
        c.append((i,e))

        sym = False
        for rr, cc in c:
            try:
                if x[rr][cc] != '.' and not x[rr][cc].isnumeric():
                    sym = True
                    sym_num[f'{rr}-{cc}'].append(n)
            except: pass
        sol += n*sym
print(sol)

sol=0
for v in sym_num.values():
    if len(v) != 2: continue
    sol += (v[0]*v[1])
print(sol)
