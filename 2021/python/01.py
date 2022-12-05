def counter() -> int:

    with open(r"C:\Users\Josep\OneDrive\Scripts\adventOfCode\2021\01-input.txt") as data:
        lines = [x.strip() for x in data.readlines()]

    count = 0

    lst = []
    for i in lines:
        lst.append(int(i))

    for i, j in enumerate(lst[:-1]):
        if j < lst[i+1]:
            count += 1

    print(count)


counter()
