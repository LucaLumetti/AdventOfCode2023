import sys
from collections import defaultdict
import re

rx = re.compile(r'\d+')

x = sys.stdin.read().strip().split('\n\n')

def rdko(input_list):
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

class Range:
    def __init__(self, start, *, length=None, end=None):
        self.start = start
        assert length is not None or end is not None
        if length is None:
            self.end = end
        else:
            self.end = start+length-1

    def __hash__(self,):
        return hash((self.start, self.end))

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def is_empty(self):
        return self.start > self.end

    def __truediv__(self, other):
        common = set()
        out = set()
        if self.start < other.start:
            out.add(Range(self.start, end=min(self.end, other.start-1)))
            common.add(Range(other.start, end=min(self.end, other.end)))

        if self.end > other.end:
            out.add(Range(max(other.end, self.start), end=self.end))
            common.add(Range(max(self.start, other.start), end=other.end))

        if self.start >= other.start and self.end <= other.end:
            common.add(self)

        return common, out

    def offset(self, off):
        self.start += off
        self.end += off
        return self

seeds = list(map(int, x[0].split()[1:]))
p1_seeds = [Range(x, length=1) for x in seeds]
p2_seeds = []
for i in range(len(seeds)//2):
    p2_seeds.append(Range(seeds[i*2], length=seeds[i*2+1]))

p1_seeds = set(p1_seeds)
p2_seeds = set(p2_seeds)
    
maps = defaultdict(list)
current_map_name = ''
for line in x[1:]:
    if '-' not in line:
        current_map_name = line[:-1]
        maps[current_map_name] = []
    else:
        map_line = line.split(':\n')[1].split('\n')
        current_map_name = line.split(':\n')[0]
        map_line = [[int(k) for k in l.split()] for l in map_line]
        maps[current_map_name] = map_line

def solve(maps, seeds):
    for k in maps.keys():
        mapping = {}

        for m in maps[k]:
            mapping[Range(m[1], length=m[2])] = m[0] - m[1]

        new_seed = set()
        for mapping_range in mapping.keys():
            out_seed = set()
            for seed in seeds:
                common, out = seed / mapping_range
                common = {c.offset(mapping[mapping_range]) for c in common}
                out_seed |= out
                new_seed |= common
            new_seed = {ns for ns in new_seed if not ns.is_empty()}
            seeds = {os for os in out_seed if not os.is_empty()}
        seeds = new_seed | seeds
    return seeds


p1_seeds = solve(maps, p1_seeds)
p2_seeds = solve(maps, p2_seeds)
print(min([s.start for s in p1_seeds]))
print(min([s.start for s in p2_seeds]))
