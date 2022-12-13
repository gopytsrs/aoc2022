import json
from collections import *
from functools import *

def parse_input():
    pairs = defaultdict(list)
    index = 1
    file = open("input.txt")
    for line in file:
        line = line.strip()
        if not line:
            index += 1
            continue
        pairs[index].append(json.loads(line))
    return pairs

    
def check(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        return 0 if left == right else -1
    if isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            res = check(left[i], right[i])
            if res in [-1, 1]:
                return res
            i += 1
        if i == len(left):
            return 1
        return -1 if i == len(right) else 0
    elif isinstance(left, int) and isinstance(right, list):
        return check([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return check(left, [right])

def right_pairs_indices_sum():
    pairs = parse_input()
    indices_sum = 0
    for i, pair in pairs.items():
        left, right = pair
        if check(left, right) == 1:
            indices_sum += i
    return indices_sum

def get_decoder_key():
    pairs = parse_input()
    packets = [[[2]], [[6]]]
    for pair in pairs.values():
        packets.extend(pair)
    
    decoder_key = 1
    packets.sort(key=cmp_to_key(check), reverse=True)
    for i, packet in enumerate(packets):
        if packet in ([[2]], [[6]]):
            decoder_key *= (i+1)
    return decoder_key
print(right_pairs_indices_sum())
print(get_decoder_key())