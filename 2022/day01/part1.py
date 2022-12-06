'''
Part 1
Loop through list
    sum ints until new line
    set sum as highest if > than highest
Output highest
'''

def main():
    with open('1.txt') as f:
        highest = 0
        sum = 0
        for line in f:
            if line == '\n':
                highest = sum if sum > highest else highest
                sum = 0
                continue
            sum += int(line)
        return print(highest)


if __name__ == "__main__":
    main()
