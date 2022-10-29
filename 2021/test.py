data = ['00100', '11110', '10110', '10111', '10101', '01111',
        '00111', '11100', '10000', '11001', '00010', '01010']


def most_frequent(data, index):
    counter = 0
    num = data[0][0]

    for i in data:
        curr_frequency = data.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


def opposite_bit(i):
    if i == 0:
        return 1
    if i == 1:
        return 0


print(most_frequent(data, 0))
