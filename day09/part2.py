import sys
import re

def all_zeros(a):
    for k in a:
        if k != 0:return False
    return True

rx = re.compile(r'\d+')

x = sys.stdin.read().strip().split('\n')
x = [[int(a) for a in k.split()] for k in x]

total=0

for seq in x:
    subseq = [seq]
    while not all_zeros(subseq[-1]):
        subseq.append([])
        for idx in range(1,len(subseq[-2])):
            subseq[-1].append(subseq[-2][idx]-subseq[-2][idx-1])
    next_val = 0
    n = len(subseq)
    for s in list(range(n))[::-1]:
        subseq[s] = [next_val] + subseq[s]
        actual_s = subseq[s]
        prev_s = subseq[s-1]
        next_val = prev_s[0]-actual_s[0]
    total += subseq[0][0]
print(total)




