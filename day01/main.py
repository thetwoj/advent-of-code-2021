def get_input(filename):
    data = []
    with open(filename, 'r') as i:
        for x in i.readlines():
            data.append(int(x))
    return data


def count_increases(measurements):
    previous = measurements[0]
    increases = 0
    for measurement in measurements[1:]:
        if measurement > previous:
            increases += 1
        previous = measurement
    return increases


def sliding_window_increases(meansurements, window_size):
    previous = sum(meansurements[0:window_size])
    increases = 0
    for x in range(1, len(meansurements)):
        current = sum(meansurements[x:x+window_size])
        if current > previous:
            increases += 1
        previous = current
    return increases


def main():
    measurements = get_input("input")
    print("Part 1:")
    print(count_increases(measurements))
    print()
    print("Part 2:")
    print(sliding_window_increases(measurements, 3))


if __name__ == "__main__":
    main()
