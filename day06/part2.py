import sys
import re

rx = re.compile(r'\d+')

x = sys.stdin.read().split('\n')
x = [rx.findall(l) for l in x]
time = int(''.join(x[0]))
distance = int(''.join(x[1]))

beat = 0
for h in range(time):
    speed = h
    rt = time-h
    td = h*rt
    beat += td > distance
print(beat)

