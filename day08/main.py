def get_input(filename):
    with open(filename, "r") as f:
        entries = []
        for line in f.readlines():
            line = line.strip()
            sentences = line.split("|")
            entries.append({
                "signal": sentences[0].rstrip(),
                "output": sentences[1].lstrip()
            })
        return entries


def map_crabs(crab_positions):
    crabs = {x: 0 for x in range(min(crab_positions), max(crab_positions) + 1)}
    for cp in crab_positions:
        crabs[cp] += 1
    return crabs


def unique_output_digits(entries):
    unique_digits = 0
    for entry in entries:
        for word in entry["output"].split(" "):
            if len(word) in [2, 3, 4, 7]:
                unique_digits += 1
    return unique_digits


def decode_signals(entries):
    for entry in entries:



def main():
    entries = get_input("input")
    unique_digits = unique_output_digits(entries)
    print("Part 1:")
    print(f"unique digit count: {unique_digits}")
    print()

    # least_fuel, least_fuel_index = least_required_fuel(crabs, additive_cost_per_move=1)
    # print("Part 2:")
    # print(f"least fuel is {least_fuel} at position {least_fuel_index}")
    # print()


if __name__ == "__main__":
    main()
