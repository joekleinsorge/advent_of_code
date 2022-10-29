""" 
input data
format data as array
loop through array (skipping last 3)
   check the word

return position
 """


def sub_position():
    import re

    # Import data
    text_file = open(
        r"C:\Users\Joey\OneDrive\Scripts\adventOfCode\2021\02-input.txt", "r")
    data = [x.strip() for x in text_file.readlines()]
    # print(data)

    # Declare variables
    depth = 0
    horizontal = 0
    aim = 0

    # Move the sub
    for i in range(len(data)):
        # Pull out what to do
        x = data[i].split(" ")
        direction = x[0]
        amount = int(x[1])

        if "forward" in direction:
            horizontal += amount
            depth += aim * amount
        if "down" in direction:
            aim += amount
        if "up" in direction:
            aim -= amount

    print(horizontal)
    print(depth)
    position = horizontal * depth
    print(position)


sub_position()
