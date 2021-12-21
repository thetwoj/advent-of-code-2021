class Cave:
    def __init__(self, name, neighbors):
        self.name = name
        self.size = "lg" if name.isupper() else "sm"
        self.neighbors = neighbors

    def __repr__(self):
        return f"{self.name} - {self.neighbors}"


def get_input(filename):
    caves = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            cave1_name, cave2_name = line.split("-")
            if cave1_name in caves:
                caves[cave1_name].neighbors.append(cave2_name)
            else:
                caves[cave1_name] = Cave(cave1_name, [cave2_name])
            if cave2_name in caves:
                caves[cave2_name].neighbors.append(cave1_name)
            else:
                caves[cave2_name] = Cave(cave2_name, [cave1_name])
        return caves


def find_routes(caves, current_cave_name="start", visited=None, valid_paths=None, single_small_twice=False, double_visited=False):
    current_cave = caves[current_cave_name]
    if current_cave_name == "end":
        visited.append("end")
        return visited

    # if it's lowercase and we've been here before figure out what to do
    if (
            current_cave_name != "start"
            and current_cave_name in visited
            and current_cave_name.islower()
    ):
        # if it's illegal, bail
        if not single_small_twice or double_visited:
            return
        # if it's okay but only this one, make sure we don't do it again
        if single_small_twice and not double_visited:
            double_visited = True

    if visited:
        visited.append(current_cave.name)
    else:
        visited = ["start"]
    for next_cave_name in current_cave.neighbors:
        next_cave = caves[next_cave_name]
        if next_cave.name == "start":
            continue
        path = find_routes(caves, next_cave.name, visited.copy(), valid_paths, single_small_twice, double_visited)
        if path is not None:
            valid_paths.append(path)


def main():
    caves = get_input("input")
    valid_paths = []
    find_routes(caves, valid_paths=valid_paths)
    # for path in valid_paths:
    #     print(path)
    print("Part 1:")
    print(f"found {len(valid_paths)} valid paths")
    print()

    caves = get_input("input")
    valid_paths = []
    find_routes(caves, valid_paths=valid_paths, single_small_twice=True)
    print("Part 2:")
    print(f"found {len(valid_paths)} valid paths")
    print()


if __name__ == "__main__":
    main()
