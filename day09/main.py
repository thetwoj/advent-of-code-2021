import math


class Area:
    def __init__(self, height):
        self.height = height
        self.visited = False
        self.neighbors = []
        self.x = 0
        self.y = 0

    def __repr__(self):
        return f"({self.x}, {self.y})"


def get_input(filename):
    with open(filename, "r") as f:
        height_map = []
        for line in f.readlines():
            line = line.strip()
            height_map.append([Area(int(x)) for x in line])
        return height_map


def find_low_points(height_map):
    low_points = []
    for y, row in enumerate(height_map):
        for x, area in enumerate(row):
            area.x = x
            area.y = y
            area.neighbors = get_neighbors(height_map, y, x)
            if min([n.height for n in area.neighbors]) > area.height:
                low_points.append(area)
    return low_points


def get_neighbors(height_map, y, x):
    neighbors = []
    if y > 0:
        neighbors.append(height_map[y-1][x])
    if x > 0:
        neighbors.append(height_map[y][x-1])
    if y < len(height_map) - 1:
        neighbors.append(height_map[y+1][x])
    if x < len(height_map[y]) - 1:
        neighbors.append(height_map[y][x+1])
    return neighbors


def find_basin_sizes(height_map):
    low_points = find_low_points(height_map)
    basin_sizes = []
    for low_point in low_points:
        basin_sizes.append(visit_neighbors(low_point, 0))
    return basin_sizes


def visit_neighbors(area, basin_size):
    if area.height == 9 or area.visited:
        return basin_size
    basin_size += 1
    area.visited = True
    for neighbor in area.neighbors:
        basin_size = visit_neighbors(neighbor, basin_size)
    return basin_size


def main():
    height_map = get_input("input")
    low_points = find_low_points(height_map)
    risk_total = sum([a.height + 1 for a in low_points])
    print("Part 1:")
    print(f"sum of risk levels is {risk_total}")
    print()

    basin_sizes = find_basin_sizes(height_map)
    basin_sizes.sort(reverse=True)
    three_largest = basin_sizes[:3]
    total = math.prod(three_largest)
    print("Part 2:")
    print(f"product of 3 largest basins is {total}")


if __name__ == "__main__":
    main()
