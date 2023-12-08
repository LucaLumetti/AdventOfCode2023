import math
import sys

x = sys.stdin.read().strip().split('\n')
direc = list(x[0])
graph = {}

for j in range(2, len(x)):
    source = x[j][:3]
    left = x[j][7:10]
    right = x[j][12:15]
    graph[source] = (left, right)

currs = [n for n in graph.keys() if n[-1] == 'A']
steps = [0 for _ in currs]
choices = {'L':0,'R':1}

for idx in range(len(currs)):
    while currs[idx][-1] != 'Z':
        choice = direc[steps[idx]%len(direc)]
        dir = choices[choice]
        currs[idx] = graph[currs[idx]][dir]
        steps[idx]+= 1

print(math.lcm(*steps))
