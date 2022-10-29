""" 
input data
format data as array
loop through array (skipping last 3)
    get sum of current number plus next two
    get sum of next number plus next two
    compare sums
        if next set is greate add to count
return count
 """


def sum_triplets():
    # Import data
    with open(r"C:\Users\Josep\OneDrive\Scripts\adventOfCode\2021\01-input.txt") as data:
        data = [x.strip() for x in data.readlines()]

    #  Format data
    lst = []
    for i in data:
        lst.append(int(i))

    # Declare variables
    count = 0

    # Loop through data
    for i in range(len(lst)):
        currentSet = sum(lst[i:i+3])
        nextSet = sum(lst[i+1:i+4])
        if currentSet < nextSet:
            count += 1

    print(count)
    return count


sum_triplets()
