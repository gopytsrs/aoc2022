def parse_input():
    file = open("input.txt")
    grid = []
    S, E = None, None
    A = []
    for line in file:
        row = []
        heights = list(line.strip())
        for h in heights:
            if h == "S":
                S = (len(grid), len(row))
                row.append(ord("a"))
            elif h == "E":
                E = (len(grid), len(row))
                row.append(ord("z"))
            else:
                if h == "a":
                    A.append((len(grid), len(row)))
                row.append(ord(h))
        grid.append(row)
    return grid, S, E, A

from collections import deque
grid, S, E, A = parse_input()
ROWS, COLS = len(grid), len(grid[0])
directions = lambda r, c: [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

def fewest_steps(starting):
    visited = {s for s in starting}
    queue = deque([s for s in starting])
    steps = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) == E:
                return steps
            for nr, nc in directions(r, c):
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or (nr, nc) in visited or grid[nr][nc] > grid[r][c] + 1:
                    continue
                visited.add((nr, nc))
                queue.append((nr, nc))
        steps += 1
    

print(fewest_steps([S]))
print(fewest_steps(A))