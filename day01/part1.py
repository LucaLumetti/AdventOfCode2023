import re

with open('input', 'r') as f:
    x = f.read().strip().split('\n')
    x = [re.sub(r'\D', '', k) for k in x]
    print(sum([int(f'{k[0]}{k[-1]}') for k in x]))
