
def parse_input():
    file = open("input.txt")
    LCM = 1
    monkeys = {}
    curr_monkey = None
    line_i = 0
    for line in file:
        line = line.strip()
        if not line:
            line_i = 0
            continue
        if line_i == 0:
            _, monkey = line[:-1].split()
            curr_monkey = int(monkey)
            monkeys[curr_monkey] = {}
        elif line_i == 1:
            _, items = line.split(":")
            items = list(map(int, items.strip().split(",")))
            monkeys[curr_monkey]['items'] = items
        elif line_i == 2:
            parts = line.split("old ")
            parts = parts[-1].split()
            op, val = parts[0], parts[1]
            if op == '*':
                if val == "old":
                    monkeys[curr_monkey]['operation'] = lambda x: x * x
                else:
                    monkeys[curr_monkey]['operation'] = lambda x, val=int(val): x * val
            elif op == '+':
                monkeys[curr_monkey]['operation'] = lambda x, val=int(val): x + val
        elif line_i == 3:
            parts = line.split()
            val = int(parts[-1])
            LCM *= val
            monkeys[curr_monkey]['test'] = lambda x, val=int(val): x % val == 0
        elif line_i == 4:
            parts = line.split()
            pass_throw = int(parts[-1])
            monkeys[curr_monkey]['pass'] = pass_throw
        elif line_i == 5:
            parts = line.split()
            fail_throw = int(parts[-1])
            monkeys[curr_monkey]['fail'] = fail_throw
        line_i += 1
    return monkeys, LCM

def get_monkey_business(rounds, use_LCM):
    monkeys, LCM = parse_input()
    inspect_times = [0 for _ in range(len(monkeys))]
    
    for _ in range(rounds):
        for m in monkeys:
            if not monkeys[m]['items']:
                continue
            while monkeys[m]['items']:
                inspect_times[m] += 1
                worry_level = monkeys[m]['items'].pop(0)
                worry_level = monkeys[m]['operation'](worry_level)
                worry_level = worry_level % LCM if use_LCM else worry_level // 3
                test_result = monkeys[m]['test'](worry_level)
                if test_result:
                    monkeys[monkeys[m]['pass']]['items'].append(worry_level)
                else:
                    monkeys[monkeys[m]['fail']]['items'].append(worry_level)
    prod = 1
    for it in sorted(inspect_times, reverse=True)[:2]:
        prod *= it
    return prod
print(get_monkey_business(20, False))
print(get_monkey_business(10000, True))
