import sys
import heapq

D = {
    'r': (1, 0),
    'l': (-1,0),
    'u': (0, -1),
    'd': (0, +1),
}

def solve(grid, start):
    rows, cols = len(grid), len(grid[0])
    distances = {(y, x, mid, d): float('infinity') for y in range(rows) for x in range(cols) for mid in range(4) for d in 'rlud'}
    distances[(0, 0, 0, 'q')] = 0
    visited = set()
    priority_queue = [(0, start, 0, 'q')]

    while priority_queue:
        current_distance, (y, x), move_in_dir, last_dir = heapq.heappop(priority_queue)

        if (y, x, move_in_dir, last_dir) in visited:
            continue

        visited.add((y, x, move_in_dir, last_dir))

        for dir in D.keys():
            if dir == last_dir and move_in_dir == 3: continue
            if last_dir == 'u' and dir == 'd': continue
            if last_dir == 'd' and dir == 'u': continue
            if last_dir == 'l' and dir == 'r': continue
            if last_dir == 'r' and dir == 'l': continue

            dx, dy = D[dir]

            new_y, new_x = y + dy, x + dx
            if not(0 <= new_y < rows and 0 <= new_x < cols): continue

            distance = current_distance + grid[new_y][new_x]

            new_move_in_dir = move_in_dir + 1 if dir == last_dir else 1

            if 0 <= new_y < rows and 0 <= new_x < cols:
                if distance < distances[(new_y, new_x, new_move_in_dir, dir)]:
                    distances[(new_y, new_x, new_move_in_dir, dir)] = distance
                    heapq.heappush(priority_queue, (distance, (new_y, new_x), new_move_in_dir, dir))

    return distances

grid = sys.stdin.read().strip().split('\n')
grid = [[int(k) for k in a] for a in grid]
rows = len(grid)
cols = len(grid[0])

start_cell = (0, 0)
result = solve(grid, start_cell)

dists = [[0 for _ in range(cols)] for _ in range(rows)]

min_distances = {(y, x): float('infinity') for y in range(rows) for x in range(cols)}

for (y, x, _, _), distance in result.items():
    min_distances[(y, x)] = min(min_distances[(y, x)], distance)

print(min_distances[(rows-1, cols-1)])

