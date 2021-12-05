from collections import defaultdict


class Board:
    def __init__(self):
        # 2d array of Spaces
        self.rows = []
        self.won = False

    def __repr__(self, show_called=False):
        response = ""
        for row in self.rows:
            for space in row:
                if show_called:
                    if space.called:
                        response += "X"
                    else:
                        response += "_"
                else:
                    response += space.__repr__().rjust(2)
                response += " "
            response += "\n"
        return response

    def print_called(self):
        print(self.__repr__(True))


class Space:
    def __init__(self, number):
        self.called = False
        self.number = number

    def __repr__(self):
        return str(self.number)


def get_input(filename):
    boards = []
    calls = []
    current_board = Board()
    spaces_distribution = defaultdict(list)
    with open(filename, 'r') as i:
        for index, line in enumerate(i.readlines()):
            line = line.strip()
            if index == 0:
                calls = line.split(",")
                continue
            if line == "":
                if len(current_board.rows) > 0:
                    boards.append(current_board)
                current_board = Board()
                continue
            split_line = line.split(" ")
            spaces = [Space(x) for x in split_line if x != ""]
            current_board.rows.append(spaces)
            for space in spaces:
                spaces_distribution[space.number].append(space)
    boards.append(current_board)
    return calls, boards, spaces_distribution


def has_won(board):
    # handles row wins
    for row in board.rows:
        if all([space.called for space in row]):
            return True

    # handles column wins
    for x in range(len(board.rows)):
        if all([row[x].called for row in board.rows]):
            return True
    return False


def first_winner(calls, boards, spaces_distribution):
    for call in calls:
        if call not in spaces_distribution:
            continue
        for space in spaces_distribution[call]:
            space.called = True

        for board in boards:
            board.won = has_won(board)
            if board.won:
                return int(call), board
    print("no winner")


def last_winner(calls, boards, spaces_distribution):
    for call in calls:
        if call not in spaces_distribution:
            continue
        for space in spaces_distribution[call]:
            space.called = True

        # skip boards that have already won
        boards_yet_to_win = [b for b in boards if not b.won]
        for board in boards_yet_to_win:
            board.won = has_won(board)
            if board.won and len(boards_yet_to_win) == 1:
                return int(call), board
    print("couldn't figure out last winner")


def main():
    calls, boards, spaces_distribution = get_input("input")
    winning_call, board = first_winner(calls, boards, spaces_distribution)
    sum_uncalled = 0
    for row in board.rows:
        sum_uncalled += sum([int(space.number) for space in row if not space.called])
    print("Part 1:")
    print(winning_call * sum_uncalled)
    print()

    winning_call, board = last_winner(calls, boards, spaces_distribution)
    sum_uncalled = 0
    for row in board.rows:
        sum_uncalled += sum([int(space.number) for space in row if not space.called])
    print("Part 2:")
    print(winning_call * sum_uncalled)


if __name__ == "__main__":
    main()
