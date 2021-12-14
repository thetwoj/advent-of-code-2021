import math


def get_input(filename):
    with open(filename, "r") as f:
        lines = []
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
        return lines


def print_error(line, history, char):
    expected = history[-1]
    # print(f"{line} - Expected closure for {expected}, got {char} instead")


def get_line_scores(lines):
    incomplete_line_scores = []
    corrupt_score = 0
    for line in lines:
        history = []
        for index, char in enumerate(line):
            if char in ["(", "[", "{", "<"]:
                history.append(char)
            elif char == ")":
                if history[-1] == "(":
                    history.pop()
                else:
                    print_error(line, history, ")")
                    corrupt_score += 3
                    break
            elif char == "]":
                if history[-1] == "[":
                    history.pop()
                else:
                    print_error(line, history, "]")
                    corrupt_score += 57
                    break
            elif char == "}":
                if history[-1] == "{":
                    history.pop()
                else:
                    print_error(line, history, "}")
                    corrupt_score += 1197
                    break
            elif char == ">":
                if history[-1] == "<":
                    history.pop()
                else:
                    print_error(line, history, ">")
                    corrupt_score += 25137
                    break
            if index == len(line) - 1:
                incomplete_line_score = 0
                while len(history) > 0:
                    current_char = history.pop()
                    incomplete_line_score = incomplete_line_score * 5
                    if current_char == "(":
                        incomplete_line_score += 1
                    elif current_char == "[":
                        incomplete_line_score += 2
                    elif current_char == "{":
                        incomplete_line_score += 3
                    elif current_char == "<":
                        incomplete_line_score += 4
                incomplete_line_scores.append(incomplete_line_score)

    incomplete_line_scores.sort()
    middle = math.ceil(len(incomplete_line_scores)/2) - 1
    return corrupt_score, incomplete_line_scores[middle]


def main():
    lines = get_input("input")
    corrupt_score, incomplete_score = get_line_scores(lines)
    print("Part 1:")
    print(f"corrupt lines score is: {corrupt_score}")
    print()

    print("Part 2:")
    print(f"middle incomplete score is: {incomplete_score}")
    print()


if __name__ == "__main__":
    main()
