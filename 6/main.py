def parse_input():
    file = open("input.txt")
    string = []
    for line in file:
        string.append(line.strip())
    return "".join(string)

from collections import *
def min_chars_processed(length):
    S = parse_input()
    left = 0
    chars_count = defaultdict(int)
    for right in range(len(S)):
        chars_count[S[right]] += 1
        if right-left+1 == length:
            if len(chars_count) == length:
                return right+1
            chars_count[S[left]] -= 1
            if chars_count[S[left]] == 0:
                chars_count.pop(S[left])
            left += 1
            
print(min_chars_processed(4))
print(min_chars_processed(14))