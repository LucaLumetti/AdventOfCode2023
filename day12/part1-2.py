import sys
import re

_cache = {}
def rec(cond, i, count, j, seq):
    key = (str(cond), i, str(count), j, seq)
    if key in _cache: return _cache[key]

    if i == len(cond):
        end_a = j == len(count) - 1 and count[j] == seq
        end_b = j == len(count) and seq == 0
        return end_a or end_b

    sol = 0
    if cond[i] in '#?':
        sol += rec(cond, i+1, count, j, seq+1)
    if cond[i] in '.?' and seq > 0 and j < len(count) and count[j] == seq:
        sol += rec(cond, i+1, count, j+1, 0)
    if cond[i] in '.?' and seq == 0:
        sol += rec(cond, i+1, count, j, 0)
    _cache[key] = sol
    return sol

x = sys.stdin.read().strip().split('\n')

total=0
for l in x:
    cond, count = l.split(' ')
    cond = ''.join([cond])
    count = [int(i) for i in count.split(',')]
    sol = rec(cond, 0, count, 0, 0)
    total += sol
print(total)

total = 0
for l in x:
    cond, count = l.split(' ')
    cond = (''.join([cond + '?']*5))[:-1]
    count = [int(i) for i in count.split(',')]*5
    sol = rec(cond, 0, count, 0, 0)
    total += sol
print(total)
