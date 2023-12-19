import sys
import re

workflows,parts = sys.stdin.read().strip().split('\n\n')

WF = {}
tx = re.compile(r'(\w+){(.*)}')
for line in workflows.split('\n'):
    name,process = re.findall(r'(\w+){(.*)}', line)[0]
    process = process.split(',')
    process = [k.split(':') for k in process]
    WF[name]=process

P = []
for line in parts.split('\n'):
    line = line[1:-1].split(',')
    P.append(line)


def update_range(op, qty, rng):
    s, e = rng
    if '>' in op:
        s = max(s, qty+('=' not in op))
    elif '<' in op:
        e = min(e, qty-('=' not in op))
    return (s,e)

AR = {'A':0, 'R':0}

ranges = [('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000))]


while len(ranges) > 0:
    key, x, m, a, s = ranges.pop()
    if key in 'AR':
        v = [k[1]-k[0]+1 for k in [x,m,a,s]]
        vprod = 1
        for vv in v:
            vprod*=vv
        AR[key] += vprod
        continue

    wf = WF[key]

    for step in wf:
        if len(step) == 2:
            cond, next = step
        else:
            cond, next = None, step[0]

        if len(step) == 1:
            ranges.append((next, x, m, a, s))
            break

        assert cond != None

        var = cond[0]
        op = cond[1]
        qty = int(cond[2:])

        if var == 'x':
            ranges.append((next, update_range(op, qty, x), m, a, s))
        if var == 'm':
            ranges.append((next, x, update_range(op, qty, m), a, s))
        if var == 'a':
            ranges.append((next, x, m, update_range(op, qty, a), s))
        if var == 's':
            ranges.append((next, x, m, a, update_range(op, qty, s)))

        op = '>=' if op == '<' else '<='

        if var == 'x':
            x = update_range(op, qty, x)
        if var == 'm':
            m = update_range(op, qty, m)
        if var == 'a':
            a = update_range(op, qty, a)
        if var == 's':
            s = update_range(op, qty, s)

print(AR['A'])
