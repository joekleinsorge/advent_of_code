import string

def checkSack(line):
    length = int(len(line) / 2)
    firstComp = line[:length]
    secondComp = line[length:]
    di=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters ]))
    sumPriority = 0
    found = []

    for i in firstComp:
        if i in found:
            continue
        if secondComp.find(i) != -1:
            found.append(i)
            if i.islower():
                sumPriority += di[i]
            else:
                sumPriority += di[i] + 26
    return sumPriority


def main():
    inputFile = open("input.txt", "r")
    inputValues = inputFile.read().split("\n")
    sum = 0
    for line in inputValues:
        sum += checkSack(line)
    print(sum)

if __name__ == "__main__":
    main()
