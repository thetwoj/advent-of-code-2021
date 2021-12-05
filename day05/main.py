def get_input(filename):
    vent_lines = []
    max_x = 0
    max_y = 0
    with open(filename, 'r') as i:
        for line in i.readlines():
            line = line.strip()
            start, end = line.split(" -> ")
            x1, y1 = start.split(",")
            x2, y2 = end.split(",")
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)
            vent_lines.append(
                {
                    "start": {
                        "x": x1,
                        "y": y1
                    },
                    "end": {
                        "x": x2,
                        "y": y2
                    }
                }
            )
    return vent_lines, max_x, max_y


def map_vents(vent_lines, max_x, max_y, diagonal=False):
    vent_overlap_count = 0
    vent_map = []
    for y in range(max_y + 1):
        vent_map.append([0 for x in range(max_x + 1)])

    for vent_line in vent_lines:
        x1 = vent_line["start"]["x"]
        y1 = vent_line["start"]["y"]
        x2 = vent_line["end"]["x"]
        y2 = vent_line["end"]["y"]

        # vertical lines
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                vent_map[y][x1] += 1
                if vent_map[y][x1] == 2:
                    vent_overlap_count += 1
        # horizontal lines
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                vent_map[y1][x] += 1
                if vent_map[y1][x] == 2:
                    vent_overlap_count += 1
        # diagonals
        elif diagonal:
            # preserving ordering of x1,y1 to x2,y2 is needed
            # for diagonals, have to figure out which way to
            # iterate the ranges to generate proper coords
            xdir = -1 if x1 > x2 else 1
            ydir = -1 if y1 > y2 else 1
            xs = [x for x in range(x1, x2 + xdir, xdir)]
            ys = [y for y in range(y1, y2 + ydir, ydir)]
            for index, x in enumerate(xs):
                vent_map[ys[index]][x] += 1
                if vent_map[ys[index]][x] == 2:
                    vent_overlap_count += 1

    return vent_overlap_count


def main():
    vent_lines, max_x, max_y = get_input("input")
    vent_overlap_count = map_vents(vent_lines, max_x, max_y)
    print("Part 1:")
    print(vent_overlap_count)
    print()

    vent_overlap_count = map_vents(vent_lines, max_x, max_y, diagonal=True)
    print("Part 2:")
    print(vent_overlap_count)


if __name__ == "__main__":
    main()
