def get_input(filename):
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            return [int(x) for x in line.split(",")]


def map_crabs(crab_positions):
    crabs = {x: 0 for x in range(min(crab_positions), max(crab_positions) + 1)}
    for cp in crab_positions:
        crabs[cp] += 1
    return crabs


def least_required_fuel(crabs, additive_cost_per_move=0):
    fuel_from_left = []
    fuel_from_right = []
    total_moves = []

    current_fuel_from_left = 0
    left_crab_fuel_costs = []  # (crab count, fuel cost)
    for index in range(min(crabs), len(crabs)):
        fuel_from_left.append(current_fuel_from_left)
        for crab_data in left_crab_fuel_costs:
            crab_data["cost"] += additive_cost_per_move
            current_fuel_from_left += crab_data["count"] * crab_data["cost"]
        left_crab_fuel_costs.append({"count": crabs[index], "cost": 1})
        current_fuel_from_left += crabs[index]


    current_fuel_from_right = 0
    right_crab_fuel_costs = []
    for index in range(len(crabs) - 1, min(crabs) - 1, -1):
        fuel_from_right.append(current_fuel_from_right)
        for crab_data in right_crab_fuel_costs:
            crab_data["cost"] += additive_cost_per_move
            current_fuel_from_right += crab_data["count"] * crab_data["cost"]
        right_crab_fuel_costs.append({"count": crabs[index], "cost": 1})
        current_fuel_from_right += crabs[index]
    fuel_from_right.reverse()

    for index in range(0, len(crabs)):
        total_moves.append(fuel_from_left[index] + fuel_from_right[index])

    least_moves = min(total_moves)
    least_moves_index = total_moves.index(least_moves) + min(crabs)

    return least_moves, least_moves_index


def main():
    crab_positions = get_input("input")
    crabs = map_crabs(crab_positions)
    least_fuel, least_fuel_index = least_required_fuel(crabs)
    print("Part 1:")
    print(f"least fuel is {least_fuel} at position {least_fuel_index}")
    print()

    least_fuel, least_fuel_index = least_required_fuel(crabs, additive_cost_per_move=1)
    print("Part 2:")
    print(f"least fuel is {least_fuel} at position {least_fuel_index}")
    print()


if __name__ == "__main__":
    main()
