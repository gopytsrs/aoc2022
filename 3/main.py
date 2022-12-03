# Part 1
from string import *
def priority_sum1():
    file = open("input.txt")
    priorities = {c:i+1 for i, c in enumerate(ascii_letters)}
    common_items = []
    for line in file:
        part1, part2 = set(line[:len(line)//2]), set(line[len(line)//2:])
        common_items.append(*part1.intersection(part2))
    file.close()
    return sum([priorities[x] for x in common_items])

# Part 2
def priority_sum2():
    file = open("input.txt")
    priorities = {c:i+1 for i, c in enumerate(ascii_letters)}
    total = 0
    badges = []
    for line in file:
        badges.append(set(line.strip()))
        if len(badges) == 3:
            badge = badges[0].intersection(badges[1], badges[2])
            total += priorities[badge.pop()]
            badges = []
    file.close()
    return total

print(priority_sum1())
print(priority_sum2())