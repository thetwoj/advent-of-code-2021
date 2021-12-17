def get_input(filename):
    with open(filename, "r") as f:
        height_map = []
        for line in f.readlines():
            line = line.strip()
            height_map.append([int(x) for x in line])
        return height_map


def low_point_risk(height_map):
    low_points = []
    for y, row in enumerate(height_map):
        for x, height in enumerate(row):
            neighbors = get_neighbors(height_map, y, x)
            neighbors.append(height)
            # check if current height is both the min and unique
            if min(neighbors) == height and len([x for x in neighbors if x == height]) == 1:
                low_points.append(height)
    risk_total = sum([x + 1 for x in low_points])
    return risk_total


def get_neighbors(height_map, y, x):
    neighbors = []
    if y > 0:
        neighbors.append(height_map[y-1][x])
        if x > 0:
            neighbors.append(height_map[y-1][x-1])
        if x < len(height_map[y]) - 1:
            neighbors.append(height_map[y-1][x+1])
    if x > 0:
        neighbors.append(height_map[y][x-1])
    if y < len(height_map) - 1:
        neighbors.append(height_map[y+1][x])
        if x > 0:
            neighbors.append(height_map[y+1][x-1])
        if x < len(height_map[y]) - 1:
            neighbors.append(height_map[y+1][x+1])
    if x < len(height_map[y]) - 1:
        neighbors.append(height_map[y][x+1])
    return neighbors


def main():
    height_map = get_input("input")
    risk_total = low_point_risk(height_map)
    print("Part 1:")
    print(f"sum of risk levels is {risk_total}")
    print()


if __name__ == "__main__":
    main()
