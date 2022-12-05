#  Input handling
with open(r'C:\Users\Joey\OneDrive\Scripts\adventOfCode\2021\03.in') as fin:
    data = [i for i in fin.read().strip().split('\n')]


def binary_to_int(binaryStr):
    return int(binaryStr, 2)


def part1():  # Part 1 - Finding Power consumption
    gammaRate = []
    epsilonRate = []

    for column in range(0, len(data[0])):
        zeros = 0
        ones = 0

        for bitString in data:
            if bitString[column] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gammaRate.append('0')
            epsilonRate.append('1')
        elif ones > zeros:
            gammaRate.append('1')
            epsilonRate.append('0')

    gammaRate = ''.join(gammaRate)
    epsilonRate = ''.join(epsilonRate)

    print(binary_to_int(gammaRate))
    print(binary_to_int(epsilonRate))
    powerConsumption = binary_to_int(gammaRate) * binary_to_int(epsilonRate)
    return powerConsumption


def part2():  # Part 2 - Finding Life support rating
    # Copy dataset
    oxyData = data.copy()

    # Find Oxygen Rating
    i = 0
    while len(oxyData) > 1:
        zeros = 0
        ones = 0
        # Counter
        for bitString in oxyData:
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            oxyData = [
                bitString for bitString in oxyData if bitString[i] == '0']
        else:
            oxyData = [
                bitString for bitString in oxyData if bitString[i] == '1']

        i += 1

    oxygenRating = ''.join(oxyData)

    # Finding  c02 Scrubber rating
    c02Data = data.copy()
    i = 0
    while len(c02Data) > 1:
        zeros = 0
        ones = 0
        # Counter
        for bitString in c02Data:
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            c02Data = [
                bitString for bitString in c02Data if bitString[i] == '1']
        else:
            c02Data = [
                bitString for bitString in c02Data if bitString[i] == '0']

        i += 1

    c02Rating = ''.join(c02Data)

    lifeSupportRating = binary_to_int(oxygenRating) * binary_to_int(c02Rating)
    return lifeSupportRating


print('Answer to part 1: ', part1())
print('Answer to part 2: ', part2())
