import sys
import re

rx = re.compile(r'\d+')

x = sys.stdin.read().split('\n')
x = [rx.findall(l) for l in x]
times = [int(a) for a in x[0]]
distances = [int(a) for a in x[1]]
print(times)
print(distances)

total = 1
for r in range(len(times)):
    beat = 0
    for h in range(times[r]):
        speed = h
        rt = times[r]-h
        td = h*rt
        beat += td > distances[r]
        print(f'{h=} {td=}')
    total *= beat
    print(beat)
print(total)

