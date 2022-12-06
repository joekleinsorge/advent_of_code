'''
Part 1
Loop through list
    calculate score for each line
    add score to total
Output total
Part 2

'''

wining_moves = {
    'A': 'Y', # Paper beats rock
    'B': 'Z', # Scissors beats paper
    'C': 'X'  # Rock beats scissors
}

shape_score = {
    'X': 1, # Rock is worth 1 point
    'Y': 2, # Paper is worth 2 points
    'Z': 3  # Scissors is worth 3 points
}


def calculate_score(line):
    left_char = line[0].upper()
    right_char = line[2].upper()

    if left_char == right_char:
        print(f'draw: {left_char} vs {right_char}')
        return 3 + shape_score[right_char] # 3 points for a draw + shape score
    if wining_moves[left_char] == right_char:
        print(f'you win: {left_char} vs {right_char}')
        return 6 + shape_score[right_char] # 6 points for a win + shape score
    print(f'you lose: {left_char} vs {right_char}')
    return 0 + shape_score[right_char] # 0 points for a loss + shape score


def part1():
    with open('2.txt') as f:
        total = 0
        for line in f:
            total += calculate_score(line)
        return print(total)

def part2():
    return

if __name__ == "__main__":
    part1()