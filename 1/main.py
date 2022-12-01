
# Part 1
def get_most_calories():
    file = open("input.txt")
    current_calories = 0
    max_calories = 0
    for line in file:
        line = line.strip()
        if not line:
            max_calories = max(max_calories, current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    file.close()
    return max_calories
# Part 2            
from heapq import *
def get_top_3_most_calories():
    file = open("input.txt")
    current_calories = 0
    heap = []
    for line in file:
        line = line.strip()
        if not line:
            heappush(heap, current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    file.close()
    return sum(nlargest(3, heap))

print(get_most_calories())
print(get_top_3_most_calories())