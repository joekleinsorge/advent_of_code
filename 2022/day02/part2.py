'''
Part 1
Loop through list
    calculate score for each line
    add score to total
Output total
'''

outcome = {
    'x': 0, # Lose
    'y': 3, # Draw
    'z': 6  # Win
}

wining_moves = {
    'A': 'Y', # Paper beats rock
    'B': 'Z', # Scissors beats paper
    'C': 'X'  # Rock beats scissors
}

tie_moves = {
    'A': 'X', # Paper ties paper
    'B': 'Y', # Scissors ties scissors
    'C': 'Z'  # Rock ties rock
}

shape_score = {
    'X': 1, # Rock is worth 1 point
    'Y': 2, # Paper is worth 2 points
    'Z': 3  # Scissors is worth 3 points
}


def calculate_score(line):
    split_line = line.split(" ")
    opp = split_line[0]
    outcome = split_line[1]    

    if tie_moves[opp] == response:
        return 3 + shape_score[response] # 3 points for a draw + shape score
    if wining_moves[opp] == response:
        return 6 + shape_score[response] # 6 points for a win + shape score
    return 0 + shape_score[response] # 0 points for a loss + shape score


def main():
    inputFile = open("input.txt", "r")
    inputValues = inputFile.read().split("\n")
    total = 0
    for line in inputValues:
        total += calculate_score(line)
    return print(total)


if __name__ == "__main__":
    main()
