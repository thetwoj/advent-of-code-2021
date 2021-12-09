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


def least_required_moves(crabs):
    moves_from_left = []
    moves_from_right = []
    total_moves = []

    current_moves_from_left = 0
    current_crabs_from_left = 0
    for index in range(min(crabs), len(crabs)):
        moves_from_left.append(current_moves_from_left)
        current_crabs_from_left += crabs[index]
        current_moves_from_left += current_crabs_from_left

    current_moves_from_right = 0
    current_crabs_from_right = 0
    for index in range(len(crabs) - 1, min(crabs) - 1, -1):
        moves_from_right.append(current_moves_from_right)
        current_crabs_from_right += crabs[index]
        current_moves_from_right += current_crabs_from_right
    moves_from_right.reverse()

    for index in range(0, len(crabs)):
        total_moves.append(moves_from_left[index] + moves_from_right[index])

    least_moves = min(total_moves)
    least_moves_index = total_moves.index(least_moves) + min(crabs)

    return least_moves, least_moves_index


def main():
    crab_positions = get_input("input")
    crabs = map_crabs(crab_positions)
    least_moves, least_moves_index = least_required_moves(crabs)
    print("Part 1:")
    print(f"least moves is {least_moves} at position {least_moves_index}")
    print()


if __name__ == "__main__":
    main()
