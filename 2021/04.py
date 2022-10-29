#  Input handling
from os import X_OK


with open(r'C:\Users\Joey\OneDrive\Scripts\adventOfCode\2021\04.in') as fin:
    numbers, *boards = fin.read().split('\n\n')
    numbers = [int(i) for i in numbers.split(',')]
    allBoards = [[[int(col) for col in row.split()]
                  for row in board.split('\n')] for board in boards]


def mark_board(number, board):  # Replace called number with x

    for row in board:
        for col in range(0, len(row)):
            if row[col] == number:
                row[col] = 'x'


def sum_board(board):  # Return sum of all non-marked numbers

    sum = 0
    for row in board:
        for num in row:
            if num != 'x':
                sum += num
    return sum


def check_for_winner(board):  # Check for a winning board
    winner = False

    # check Rows
    for row in board:
        winner = all(elem in ['x'] for elem in row)

        if winner:
            return winner
    # check columns
    for col in range(0, 5):
        winner = all(elem in ['x'] for elem in [row[col] for row in board])

        if winner:
            return winner
    return winner


def part1():  # Part 1 - Find the first winning Bingo Card's sum
    boards = allBoards

    for number in numbers:
        for board in boards:
            mark_board(number, board)

            if check_for_winner(board):
                return sum_board(board) * number


#  Results
print('Answer to part 1: ', part1())
