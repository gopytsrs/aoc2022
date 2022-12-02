# Part 1
def strategy_guide1():
    file = open("input.txt")
    #A B C => X Y Z => Rock Paper Scissors
    score_map = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6 }
    total_score = 0
    for line in file:
        total_score += score_map["".join(line.split())]
    file.close()
    return total_score

# Part 2
def strategy_guide2():
    file = open("input.txt")
    # A B C => Rock Paper Scissors, X Y Z => Lose Draw Win
    score_map = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7 }
    total_score = 0
    for line in file:
        total_score += score_map["".join(line.split())]
    file.close()
    return total_score


print(strategy_guide1())
print(strategy_guide2())