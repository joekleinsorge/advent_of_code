'''
Part 2
Loop through list
    sum ints until new line
    if sum > highest, set sum as highest
    elif sum > second highest, set sum as second highest
    elif sum > third highest, set sum as third highest
Output total of highest, second highest, third highest
'''

def main():
    with open('1.txt') as f:
        highest = 0
        second_highest = 0
        third_highest = 0
        sum = 0
        for line in f:
            if line == '\n':
                if sum > highest:
                    third_highest = second_highest
                    second_highest = highest
                    highest = sum
                elif sum > second_highest:
                    third_highest = second_highest
                    second_highest = sum
                elif sum > third_highest:
                    third_highest = sum
                sum = 0
                continue
            sum += int(line)
        return print(highest + second_highest + third_highest)
    

if __name__ == "__main__":
    main()
