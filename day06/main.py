def get_input(filename):
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            return [int(x) for x in line.split(",")]


def map_fish(fish):
    fishes = {x: 0 for x in range(0, 9)}
    for f in fish:
        fishes[f] += 1
    return fishes


def run_days(fishes, days):
    for day in range(0, days):
        temp6 = fishes[6]
        temp8 = fishes[8]
        for x in range(0, 9):
            if x == 0:
                fishes[6] = fishes[0]
                fishes[8] = fishes[0]
            elif x == 6:
                fishes[5] = temp6
            elif x == 7:
                fishes[6] += fishes[7]
            elif x == 8:
                fishes[7] = temp8
            else:
                fishes[x-1] = fishes[x]
    return sum(fishes.values())


def main():
    fish = get_input("input")
    fishes = map_fish(fish)
    count = run_days(fishes, 80)
    print("Part 1:")
    print(count)
    print()

    fishes = map_fish(fish)
    count = run_days(fishes, 256)
    print("Part 2:")
    print(count)


if __name__ == "__main__":
    main()
