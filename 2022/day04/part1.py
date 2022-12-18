

def checkSec(line):
    '''
    spilts the line into two parts, one for each elf
    Create list of elfs sections
    checks if one elf contains the other elf
    if so, return 1
    '''
    elf1 = line.split(",")[0]
    range1 = range(int(elf1.split("-")[0]), int(elf1.split("-")[1]))
    elf2 = line.split(",")[1]
    range2 = range(int(elf2.split("-")[0]), int(elf2.split("-")[1]))
    print(range1, range2)
    if range1.start in range2 and range1[-1] in range2:
        return 1
    if range2.start in range1 and range2[-1] in range1:
        return 1    
    else: 
        return 0


def main():
    inputFile = open("input.txt", "r")
    inputValues = inputFile.read().split("\n")
    sum = 0
    for line in inputValues:
        sum += checkSec(line)
    print(sum)

if __name__ == "__main__":
    main()
