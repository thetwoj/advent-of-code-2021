def get_input(filename):
    data = []
    with open(filename, 'r') as i:
        for x in i.readlines():
            data.append(x.strip())
    return data


def find_gamma_epsilon(report):
    digit_counts = {}
    binary_gamma = ""
    for line in report:
        for index, letter in enumerate(line):
            if index in digit_counts:
                digit_counts[index][letter] += 1
            else:
                digit_counts[index] = {"0": 0, "1": 0}
                digit_counts[index][letter] += 1

    for key in digit_counts:
        if digit_counts[key]["0"] > digit_counts[key]["1"]:
            binary_gamma += "0"
        else:
            binary_gamma += "1"

    binary_epsilon = ""
    for digit in binary_gamma:
        if digit == "0":
            binary_epsilon += "1"
        else:
            binary_epsilon += "0"

    gamma = int(binary_gamma, 2)
    epsilon = int(binary_epsilon, 2)
    return gamma, epsilon


def find_oxygen(report):
    for x in range(len(report[0])):
        tracker = {"0": [], "1": []}
        for line in report:
            tracker[line[x]].append(line)
        if len(tracker["0"]) > len(tracker["1"]):
            report = tracker["0"]
        else:
            report = tracker["1"]
        if len(report) == 1:
            return int(report[0], 2)


def find_co2(report):
    for x in range(len(report[0])):
        tracker = {"0": [], "1": []}
        for line in report:
            tracker[line[x]].append(line)
        if len(tracker["0"]) <= len(tracker["1"]):
            report = tracker["0"]
        else:
            report = tracker["1"]
        if len(report) == 1:
            return int(report[0], 2)


def main():
    report = get_input("input")
    print("Part 1:")
    gamma, epsilon = find_gamma_epsilon(report)
    print(gamma * epsilon)
    print()
    print("Part 2:")
    oxygen = find_oxygen(report)
    co2 = find_co2(report)
    print(oxygen * co2)


if __name__ == "__main__":
    main()
