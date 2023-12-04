import sys
import re

original = sys.stdin.read().split('\n')
x = [k.split(':')[-1] for k in original]
x = [k.split(' | ') for k in x]
x = x[:-1]
for k in x:
    k[0] = [int(j) for j in k[0].strip().split(' ') if j != '']
    k[1] = [int(j) for j in k[1].strip().split(' ') if j != '']

x = [len(set(k[0]) & set(k[1])) for k in x]
sol=[]

card_count = [1]*(len(original)-1)
total_p1 = 0
for i,k in enumerate(x):
    total_p1 += int(2**(int(k)-1))
    for _ in range(card_count[i]):
        for j in range(i+1, i+k+1):
            card_count[j] += 1

print(total_p1)
print(sum(card_count))
