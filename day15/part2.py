import sys
import re

x = sys.stdin.read().strip().replace('\n','').split(',')

def hash(s):
    current_value = 0

    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256

    return current_value


# x = sum([hash(s) for s in x])
# print(x)

from collections import defaultdict
boxes = defaultdict(list)
for a in x:
    label = re.match(r'\w+', a)
    op = a[label.end()]
    val = a[label.end()+1:]
    b = int(hash(label[0]))

    if op == '=':
        c = False
        for idx,bb in enumerate(boxes[b]):
            if bb[0] != label[0]: continue
            boxes[b][idx] = (label[0], int(val))
            c = True
        if not c:
            boxes[b].append((label[0], int(val)))
    if op == '-':
        for bb in boxes[b]:
            if bb[0] != label[0]: continue
            boxes[b].remove(bb)
            break

total = 0
for box in boxes:
    for slot,bb in enumerate(boxes[box]):
        total += (box+1)*(slot+1)*int(bb[-1])

print(total)
