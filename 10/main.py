def parse_input():
    file = open("input.txt")
    instructions = []
    for line in file:
        line = line.strip()
        if line.startswith("noop"):
            instructions.append((1, 0))
        else:
            _, val = line.split()
            instructions.append((2, int(val)))
    return instructions

from collections import *

def get_signal_strength():
    x, clk = 1, 0
    instructions = parse_input()
    queue = deque()
    signal_strength = 0
    cycles = {20, 60, 100, 140, 180, 220}
    
    for inst, val in instructions:
        if inst == 2:
            clk += 1
            if clk in cycles:
                signal_strength += x * clk
        clk += 1
        if clk in cycles:
            signal_strength += x * clk
        x += val
    return signal_strength

def get_CRT_letters():
    instructions = parse_input()
    CRT = [[" "]*40 for _ in range(6)]
    clk = 0
    x = 1
    def draw():
        row, col = (clk-1)//40, (clk-1)%40
        col_diff = abs(x - col)
        if col_diff <= 1:
            CRT[row][col] = "#"
    
    for inst, val in instructions:
        if inst == 2:
            clk += 1
            draw()
        clk += 1
        draw()
        x += val
    return "\n".join("".join(row) for row in CRT)
    

print(get_signal_strength())
print(get_CRT_letters())