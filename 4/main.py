def get_start_end(string):
    start, end = string.split("-")
    return [int(start), int(end)]

# Part 1
def get_fully_contained_pairs():
    file = open("input.txt")
    contained_pairs = 0
    for line in file:
        pair1, pair2 = line.split(",")
        start1, end1 = get_start_end(pair1)
        start2, end2 = get_start_end(pair2)
        if (start1 <= start2 and end2 <= end1) or (start2 <= start1 and end1 <= end2):
            contained_pairs += 1
    return contained_pairs    
    file.close()

# Part 2
def get_overlapping_pairs():
    file = open("input.txt")
    overlapping_pairs = 0
    for line in file:
        pair1, pair2 = line.split(",")
        interval1 = get_start_end(pair1)
        interval2 = get_start_end(pair2)
        # Sort by start interval
        if interval2[0] < interval1[0]:
            interval1, interval2 = interval2, interval1 
        if interval2[0] <= interval1[1]:
            overlapping_pairs += 1
    file.close()
    return overlapping_pairs

print(get_fully_contained_pairs())
print(get_overlapping_pairs())