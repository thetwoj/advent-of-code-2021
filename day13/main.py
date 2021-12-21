def get_input(filename):
    max_x = 0
    max_y = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                break
            x, y = line.split(",")
            x = int(x)
            y = int(y)
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    reading_folds = False
    folds = []
    paper = [["." for x in range(max_x + 1)] for _ in range(max_y + 1)]
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                reading_folds = True
                continue
            if not reading_folds:
                x, y = line.split(",")
                paper[int(y)][int(x)] = "#"
            else:
                folds.append(line.split(" ")[-1])
    return paper, folds


def do_folds(paper, folds, fold_count=None):
    count = 0
    for fold in folds:
        axis = fold[0]
        loc = int(fold.split("=")[-1])
        if axis == "y":
            for y in range(loc + 1, len(paper)):
                for x in range(len(paper[0])):
                    if paper[y][x] == "#":
                        paper[y][x] = "."
                        offset = (y - loc) * 2
                        paper[y-offset][x] = "#"
            paper = paper[:loc]
        elif axis == "x":
            for y in range(len(paper)):
                for x in range(loc + 1, len(paper[0])):
                    if paper[y][x] == "#":
                        paper[y][x] = "."
                        offset = (x - loc) * 2
                        paper[y][x-offset] = "#"
            for y in range(len(paper)):
                paper[y] = paper[y][:loc]

        count += 1
        if fold_count and count == fold_count:
            return paper
    return paper


def count_dots(paper):
    dots = 0
    for y in range(len(paper)):
        for x in range(len(paper[0])):
            if paper[y][x] == "#":
                dots += 1
    return dots


def main():
    paper, folds = get_input("input")
    paper = do_folds(paper, folds, 1)
    dots = count_dots(paper)
    print("Part 1:")
    print(f"{dots} dots are visible after one fold")
    print()

    paper, folds = get_input("input")
    paper = do_folds(paper, folds)
    print("Part 2:")
    # this makes it more visible on my terminal
    for y in range(len(paper)):
        for x in range(len(paper[0])):
            if paper[y][x] == "#":
                print(" X ", end="")
            else:
                print("   ", end="")
        print()


if __name__ == "__main__":
    main()
