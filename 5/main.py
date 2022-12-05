from collections import *
def parse_input():
    file = open("input.txt")
    stacks = defaultdict(deque)
    for i, line in enumerate(file):
        if not line.strip():
            break
        if i == 8:
            continue
        stack = [line[i:i+4].strip() for i in range(0, len(line), 4)]
        for i, ele in enumerate(stack):
            if ele: stacks[f"{i+1}"].appendleft(ele)
    
    # Continues reading after the blank line separation
    procedures = []
    for i, line in enumerate(file):
        parts = line.strip().split()
        # amount to move, from stack, to stack
        procedures.append([int(parts[1]), parts[3], parts[5]])
    return [stacks, procedures]

# Part 1
def get_crates_at_top():
    stacks, procedures = parse_input()
    for amt, fr, to in procedures:
        for _ in range(amt):
            stacks[to].append(stacks[fr].pop())
    
    pairs = [[s, q[-1]] for s, q in stacks.items()]
    return "".join([p[1][1] for p in sorted(pairs, key=lambda x:x[0])])

# Part 2
def get_crates_at_top_9001():
    stacks, procedures = parse_input()
    for amt, fr, to in procedures:
        to_move = []
        for _ in range(amt):
            to_move.append(stacks[fr].pop())
        stacks[to].extend(to_move[::-1])
    pairs = [[s, q[-1]] for s, q in stacks.items()]
    return "".join([p[1][1] for p in sorted(pairs, key=lambda x:x[0])])            

print(get_crates_at_top())
print(get_crates_at_top_9001())
        