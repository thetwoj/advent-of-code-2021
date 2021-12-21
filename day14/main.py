def get_input(filename):
    with open(filename, "r") as f:
        polymer = ""
        rules = {}
        for line in f.readlines():
            line = line.strip()
            if not polymer:
                polymer = line
                continue
            if line == "":
                continue
            ingredients, results = line.split(" -> ")
            rules[ingredients] = results
        return polymer, rules


def evaluate_rules(polymer, rules, steps):
    step_count = 0
    while steps > step_count:
        next_polymer = ""
        for x in range(len(polymer)-1):
            current_pair = polymer[x:x+2]
            if x == len(polymer)-2:
                next_polymer += current_pair[0] + rules[current_pair] + current_pair[1]
            else:
                next_polymer += current_pair[0] + rules[current_pair]
        polymer = next_polymer
        step_count += 1
    return polymer


def count_letters(polymer):
    letter_counts = {}
    for x in polymer:
        if x in letter_counts:
            letter_counts[x] += 1
        else:
            letter_counts[x] = 1

    lowest = None
    highest = None
    for v in letter_counts.values():
        if lowest is None or v < lowest:
            lowest = v
        if highest is None or v > highest:
            highest = v
    return highest, lowest


def main():
    polymer, rules = get_input("input")
    polymer = evaluate_rules(polymer, rules, 10)
    high, low = count_letters(polymer)
    print("Part 1:")
    print(f"diff between most and least frequent is {high - low}")
    print()

    # this takes so long that it hasn't actually ever finished...
    polymer, rules = get_input("input")
    polymer = evaluate_rules(polymer, rules, 40)
    high, low = count_letters(polymer)
    print("Part 2:")
    print(f"diff between most and least frequent is {high - low}")
    print()


if __name__ == "__main__":
    main()
