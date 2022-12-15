import string

def checkSack(setOfSacks):
    di=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters ]))
    sumPriority = 0
    found = []

    for i in setOfSacks[0]:
        if i in found:
            continue
        if setOfSacks[1].find(i) != -1 and setOfSacks[2].find(i) != -1:
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

    for i in range(0, len(inputValues), 3):
        firstSack = inputValues[i]
        secondSack = inputValues[i+1]
        thirdSack = inputValues[i+2]

        setOfSacks = [firstSack, secondSack, thirdSack]
        sum += checkSack(setOfSacks)

    print(sum)

if __name__ == "__main__":
    main()
