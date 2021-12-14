class Display:
    def __init__(self):
        self.signals_to_letters = {
            0: {"a", "b", "c", "d", "e", "f", "g"},
            1: {"a", "b", "c", "d", "e", "f", "g"},
            2: {"a", "b", "c", "d", "e", "f", "g"},
            3: {"a", "b", "c", "d", "e", "f", "g"},
            4: {"a", "b", "c", "d", "e", "f", "g"},
            5: {"a", "b", "c", "d", "e", "f", "g"},
            6: {"a", "b", "c", "d", "e", "f", "g"},
        }
        self.letters_to_signals = {
            'a': {0, 1, 2, 3, 4, 5, 6},
            'b': {0, 1, 2, 3, 4, 5, 6},
            'c': {0, 1, 2, 3, 4, 5, 6},
            'd': {0, 1, 2, 3, 4, 5, 6},
            'e': {0, 1, 2, 3, 4, 5, 6},
            'f': {0, 1, 2, 3, 4, 5, 6},
            'g': {0, 1, 2, 3, 4, 5, 6},
        }


def get_input(filename):
    with open(filename, "r") as f:
        entries = []
        for line in f.readlines():
            line = line.strip()
            sentences = line.split("|")
            entries.append({
                "signal": sentences[0].rstrip(),
                "output": sentences[1].lstrip()
            })
        return entries


def unique_output_digits(entries):
    unique_digits = 0
    for entry in entries:
        for word in entry["output"].split(" "):
            if len(word) in [2, 3, 4, 7]:
                unique_digits += 1
    return unique_digits


def decode_signals(entries):
    sum = 0
    for entry in entries:
        display = Display()
        for word in entry["signal"].split(" "):
            for letter in word:
                if len(display.letters_to_signals[letter]) > 1:
                    if len(word) == 2:
                        limit_matches_by_signal(display, letter, [2, 5])
                    elif len(word) == 3:
                        limit_matches_by_signal(display, letter, [0, 2, 5])
                    elif len(word) == 4:
                        limit_matches_by_signal(display, letter, [1, 2, 3, 5])

        for _ in range(7):  # this is silly
            for l, s in display.letters_to_signals.items():
                if len(s) == 1:
                    signal = s.pop()
                    limit_matches_by_letter(display, signal, [l])
                    s.add(signal)

                for l2, s2, in display.letters_to_signals.items():
                    if l == l2:
                        continue
                    if len(s) == 2 and s == s2:
                        for signal in s:
                            limit_matches_by_letter(display, signal, [l, l2])

        for word in entry["signal"].split(" "):
            if len(word) == 6:
                # zero
                middle = display.signals_to_letters[3].copy()
                for letter in middle:
                    if letter not in word:
                        limit_matches_by_signal(display, letter, [3])
                # six
                top_right_letters = display.signals_to_letters[2].copy()
                for letter in top_right_letters:
                    if letter not in word:
                        limit_matches_by_signal(display, letter, [2])
                # nine
                bottom_left_letters = display.signals_to_letters[4].copy()
                for letter in bottom_left_letters:
                    if letter not in word:
                        limit_matches_by_signal(display, letter, [4])

        for l, s in display.letters_to_signals.items():
            if len(s) == 1:
                signal = s.pop()
                limit_matches_by_letter(display, signal, [l])
                s.add(signal)

        output = ""
        for word in entry["output"].split(" "):
            if len(word) == 2:
                output += "1"
            elif len(word) == 3:
                output += "7"
            elif len(word) == 4:
                output += "4"
            elif len(word) == 5:
                top_left = display.signals_to_letters[1].pop()
                display.signals_to_letters[1].add(top_left)
                bottom_left = display.signals_to_letters[4].pop()
                display.signals_to_letters[4].add(bottom_left)
                if top_left not in word and bottom_left not in word:
                    output += "3"
                    continue
                top_right = display.signals_to_letters[2].pop()
                display.signals_to_letters[2].add(top_right)
                if top_right not in word and bottom_left not in word:
                    output += "5"
                    continue
                bottom_right = display.signals_to_letters[5].pop()
                display.signals_to_letters[5].add(bottom_right)
                if top_left not in word and bottom_right not in word:
                    output += "2"
                    continue
            elif len(word) == 6:
                middle = display.signals_to_letters[3].pop()
                display.signals_to_letters[3].add(middle)
                if middle not in word:
                    output += "0"
                    continue
                top_right = display.signals_to_letters[2].pop()
                display.signals_to_letters[2].add(top_right)
                if top_right not in word:
                    output += "6"
                    continue
                bottom_left = display.signals_to_letters[4].pop()
                display.signals_to_letters[4].add(bottom_left)
                if bottom_left not in word:
                    output += "9"
                    continue
            elif len(word) == 7:
                output += "8"

        sum += int(output)
    return sum


def limit_matches_by_signal(display, letter, limit_to_signals):
    letters_removed = []
    for signal in display.letters_to_signals[letter]:
        if signal not in limit_to_signals:
            letters_removed.append(signal)
            display.signals_to_letters[signal].remove(letter)
    for signal in letters_removed:
        display.letters_to_signals[letter].remove(signal)


def limit_matches_by_letter(display, signal, limit_to_letters):
    letters_removed = []
    for letter in display.signals_to_letters[signal]:
        if letter not in limit_to_letters:
            letters_removed.append(letter)
            display.letters_to_signals[letter].remove(signal)
    for letter in letters_removed:
        display.signals_to_letters[signal].remove(letter)


def main():
    entries = get_input("input")
    unique_digits = unique_output_digits(entries)
    print("Part 1:")
    print(f"unique digit count: {unique_digits}")
    print()

    total = decode_signals(entries)
    print("Part 2:")
    print(f"total of all output values is {total}")
    print()


if __name__ == "__main__":
    main()
