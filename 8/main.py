def parse_input():
    file = open("input.txt")
    grid = []
    for line in file:
        row = list(map(int, line.strip()))
        grid.append(row)
    return grid

from collections import *
def get_visible_trees():
    grid = parse_input()
    ROWS, COLS = len(grid), len(grid[0])
    
    top_max, left_max = defaultdict(lambda:-1), defaultdict(lambda:-1)
    visible_trees = set()
    for r in range(ROWS):
        for c in range(COLS):
            if top_max[c] < grid[r][c]:
                visible_trees.add((r, c))
                top_max[c] = grid[r][c]
            if left_max[r] < grid[r][c]:
                visible_trees.add((r, c))
                left_max[r] = grid[r][c]
                
    bottom_max, right_max = defaultdict(lambda:-1), defaultdict(lambda:-1)
    for r in range(ROWS-1, -1, -1):
        for c in range(COLS-1, -1, -1):
            if bottom_max[c] < grid[r][c]:
                visible_trees.add((r, c))
                bottom_max[c] = grid[r][c]
            if right_max[r] < grid[r][c]:
                visible_trees.add((r, c))
                right_max[r] = grid[r][c]
    return len(visible_trees)

def get_max_scenic_score():
    grid = parse_input()
    ROWS, COLS = len(grid), len(grid[0])
    max_scenic_score = 0
    
    for row in range(ROWS):
        for col in range(COLS):
            # Ignore Edges
            if row in [0, ROWS-1] or col in [0, COLS-1]:
                continue
            
            height = grid[row][col]
            left = right = top = bottom = 0
            # Find viewing distance at each direction
            for r in range(row+1, ROWS):
                bottom += 1
                if grid[r][col] >= height:
                    break
            for r in range(row-1, -1, -1):
                top += 1
                if grid[r][col] >= height:
                    break
            for c in range(col+1, COLS):
                right += 1
                if grid[row][c] >= height:
                    break
            for c in range(col-1, -1, -1):
                left += 1
                if grid[row][c] >= height:
                    break
            max_scenic_score = max(max_scenic_score, left*right*top*bottom)
    return max_scenic_score
                

    
    
print(get_visible_trees())
print(get_max_scenic_score())