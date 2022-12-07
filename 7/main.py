from collections import *
def parse_input():
    directories = Counter()
    file = open("input.txt")
    curr_dir = []
    # directories will contains => key: size, key is always a directory, not a file.
    for line in file:
        line = line.strip()
        if line.startswith("$ cd"):
            _, _, d  = line.split()
            if d == "/":
                curr_dir = []
            elif d == "..":
                curr_dir.pop()
            else:
                curr_dir.append(d)
        elif line.startswith("$ ls"):
            continue
        else:
            a, _ = line.split()
            if a.isnumeric():
                for i in range(len(curr_dir)+1):
                    directories["/".join(curr_dir[:i])] += int(a)
    return directories

def total_size_of_directories():
    directories = parse_input()
    total_size = 0
    for size in directories.values():
        if size <= 100000:
            total_size += size
    return total_size

def smallest_directory_to_delete():
    directories = parse_input()
    min_size = float('inf')
    required = 30000000 - (70000000 - directories[""])
    for size in directories.values():
        if size >= required:
            min_size = min(min_size, size)
    return min_size

print(total_size_of_directories())
print(smallest_directory_to_delete())