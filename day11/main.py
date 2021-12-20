class Octopus:
    def __init__(self, x, y, value):
        self.flashed = False
        self.value = value
        self.x = x
        self.y = y


def get_input(filename):
    with open(filename, "r") as f:
        octo_map = []
        for y, line in enumerate(f.readlines()):
            line = line.strip()
            octo_map.append([Octopus(x, y, int(value)) for x, value in enumerate(line)])
        return octo_map


def run_steps(octo_map, steps, run_until_all_flash=False):
    octopus_count = len(octo_map) * len(octo_map[0])
    step_count = 0
    flashes = 0
    while step_count < steps:
        to_flash = []
        # increment all octopus values by 1 and record flashers
        for row in octo_map:
            for octopus in row:
                octopus.value += 1
                if octopus.value > 9:
                    to_flash.append(octopus)

        has_flashed = []
        while to_flash:
            octopus = to_flash.pop()
            if octopus.flashed:
                continue

            x = octopus.x
            y = octopus.y
            if x > 0:
                octo_map[y][x-1].value += 1
                if octo_map[y][x-1].value > 9:
                    to_flash.append(octo_map[y][x-1])
                if y > 0:
                    octo_map[y-1][x-1].value += 1
                    if octo_map[y-1][x-1].value > 9:
                        to_flash.append(octo_map[y-1][x-1])
            if y > 0:
                octo_map[y-1][x].value += 1
                if octo_map[y-1][x].value > 9:
                    to_flash.append(octo_map[y-1][x])
                if x < len(octo_map[0]) - 1:
                    octo_map[y-1][x+1].value += 1
                    if octo_map[y-1][x+1].value > 9:
                        to_flash.append(octo_map[y-1][x+1])
            if x < len(octo_map[0]) - 1:
                octo_map[y][x+1].value += 1
                if octo_map[y][x+1].value > 9:
                    to_flash.append(octo_map[y][x+1])
                if y < len(octo_map) - 1:
                    octo_map[y+1][x+1].value += 1
                    if octo_map[y+1][x+1].value > 9:
                        to_flash.append(octo_map[y+1][x+1])
            if y < len(octo_map) - 1:
                octo_map[y+1][x].value += 1
                if octo_map[y+1][x].value > 9:
                    to_flash.append(octo_map[y+1][x])
                if x > 0:
                    octo_map[y+1][x-1].value += 1
                    if octo_map[y+1][x-1].value > 9:
                        to_flash.append(octo_map[y+1][x-1])

            octopus.flashed = True
            has_flashed.append(octopus)

        step_count += 1
        # return the step count if we're just waiting
        # for them all to flash, and they did
        if run_until_all_flash and len(has_flashed) == octopus_count:
            return step_count

        flashes += len(has_flashed)
        for octopus in has_flashed:
            octopus.flashed = False
            octopus.value = 0

    return flashes


def main():
    octo_map = get_input("input")
    flashes = run_steps(octo_map, 100)
    print("Part 1:")
    print(f"there were {flashes} in 100 steps")
    print()

    octo_map = get_input("input")
    all_flash_step = run_steps(octo_map, 99999, True)
    print("Part 2:")
    print(f"all flashed on step {all_flash_step}")
    print()


if __name__ == "__main__":
    main()
