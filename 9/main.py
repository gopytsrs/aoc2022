
def parse_input():
    file = open("input.txt")
    moves = []
    for line in file:
        parts = line.strip().split()
        moves.append((parts[0], int(parts[1])))
    return moves

X, Y = 0, 1
dirs = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

def follow_head(head, tail):
    xd = head[X] - tail[X]
    yd = head[Y] - tail[Y]
    tx, ty = tail
    hx, hy = head
    
    if abs(xd) == 2 and abs(yd) == 2:
        tx = (tx+hx)//2
        ty = (ty+hy)//2
    elif abs(xd) == 2:
        tx = (tx+hx)//2
        ty = hy
    elif abs(yd) == 2:
        ty = (ty+hy)//2
        tx = hx
    return (tx, ty)
        
        

def get_tail_positions():
    moves = parse_input()
    head = [0, 0]
    tail = [0, 0]
    visited = {(0, 0)}
    for d, steps in moves:
        for _ in range(steps):
            head = [head[X]+dirs[d][X], head[Y]+dirs[d][Y]]
            tail = follow_head(head, tail)
            visited.add(tail)
    return len(visited)

def get_elongated_tail_positions():
    moves = parse_input()
    head = [0, 0]
    tails = [[0, 0] for _ in range(9)]
    visited = {(0, 0)}
    for d, steps in moves:
        for _ in range(steps):
            head = [head[X]+dirs[d][X], head[Y]+dirs[d][Y]]
            tails[0] = follow_head(head, tails[0])
            for i in range(1, 9):
                tails[i] = follow_head(tails[i-1], tails[i])
            visited.add(tails[8])
    return len(visited)
        
print(get_tail_positions())
print(get_elongated_tail_positions())