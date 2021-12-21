from tqdm import tqdm
from collections import defaultdict


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
        for x in range(len(polymer) - 1):
            current_pair = polymer[x:x+2]
            if x == len(polymer)-2:
                next_polymer += current_pair[0] + rules[current_pair] + current_pair[1]
            else:
                next_polymer += current_pair[0] + rules[current_pair]
        polymer = next_polymer
        step_count += 1
    return polymer


def create_shortcuts(rules):
    shortcuts = {}
    for polymer in tqdm(rules):
        shortcuts[polymer] = evaluate_rules(polymer, rules, 20)
    return shortcuts


def run_steps_via_shortcuts(polymer, shortcuts, steps=2):
    step_count = 0
    letter_counts = defaultdict(int)
    cached_letter_counts = {}
    while steps > step_count:
        next_polymer = ""
        for x in tqdm(range(len(polymer) - 1)):
            current_pair = polymer[x:x + 2]
            if step_count > 0:
                if current_pair not in cached_letter_counts:
                    cached_letter_counts[current_pair] = count_letters(shortcuts[current_pair])
                letter_counts = combine_counts(letter_counts, cached_letter_counts[current_pair])
                if x != len(polymer) - 2:
                    letter_counts[shortcuts[current_pair][-1:]] -= 1
            else:
                if x == len(polymer) - 2:
                    next_polymer += shortcuts[current_pair]
                else:
                    next_polymer += shortcuts[current_pair][:-1]
        polymer = next_polymer
        step_count += 1
    return find_high_low(letter_counts)


def combine_counts(letter_counts, letter_counts2):
    for key, value in letter_counts2.items():
        letter_counts[key] += value
    return letter_counts


def count_letters(polymer):
    letter_counts = defaultdict(int)
    for x in polymer:
        letter_counts[x] += 1
    return letter_counts


def find_high_low(letter_counts):
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
    letter_counts = count_letters(polymer)
    high, low = find_high_low(letter_counts)
    print("Part 1:")
    print(f"diff between most and least frequent is {high - low}")
    print()

    polymer, rules = get_input("input")
    shortcuts = create_shortcuts(rules)
    high, low = run_steps_via_shortcuts(polymer, shortcuts)
    print("Part 2:")
    print(f"diff between most and least frequent is {high - low}")
    print()


if __name__ == "__main__":
    main()
