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

AR = {'A':0, 'R':0}
for p in P:
    for pp in p:
        exec(pp)
    curr = WF['in']
    found_end = False
    while True:
        for c in curr:
            if len(c) == 1:
                out = c[0]
                if out in 'AR':
                    AR[out] += (m+s+a+x)
                    found_end=True
                    break
                curr = WF[out]
                break
            if len(c) == 2:
                cond = c[0]
                out = c[1]
                res =eval(cond)
                if res:
                    if out in 'AR':
                        AR[out] += (m+s+a+x)
                        found_end=True
                        break
                    curr = WF[out]
                    break
                else:
                    continue
        if found_end: break

print(AR['A'])


