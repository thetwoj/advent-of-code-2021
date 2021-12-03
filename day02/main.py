def get_input(filename):
    data = []
    with open(filename, 'r') as i:
        for x in i.readlines():
            data.append(x)
    return data


def interpret_commands(commands):
    horizontal = 0
    depth = 0
    for command in commands:
        words = command.split()
        direction = words[0]
        distance = int(words[1])
        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            if distance > depth:
                depth = 0
            else:
                depth -= distance
    return horizontal, depth


def interpret_commands_with_aim(commands):
    aim = 0
    horizontal = 0
    depth = 0
    for command in commands:
        words = command.split()
        direction = words[0]
        distance = int(words[1])
        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    return horizontal, depth


def main():
    commands = get_input("input")
    print("Part 1:")
    horizontal, depth = interpret_commands(commands)
    product = horizontal * depth
    print(product)
    print()
    print("Part 2:")
    horizontal, depth = interpret_commands_with_aim(commands)
    product = horizontal * depth
    print(product)


if __name__ == "__main__":
    main()
