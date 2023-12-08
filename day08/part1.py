import sys

x = sys.stdin.read().strip().split('\n')
direc = list(x[0])
graph = {}

for j in range(2, len(x)):
    source = x[j][:3]
    left = x[j][7:10]
    right = x[j][12:15]
    graph[source] = (left, right)

steps = 0
choices = {'L':0,'R':1}
curr = 'AAA'
while curr != 'ZZZ':
    choice = direc[steps%len(direc)]
    dir = choices[choice]
    curr = graph[curr][dir]
    steps += 1

print(steps)

