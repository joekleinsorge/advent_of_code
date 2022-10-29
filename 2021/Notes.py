string = "abc"
print(len(string))  # 3
print(string[0:2])  # ab
print(string[::-1])  # cba

var = [1, 2, 3, 4, 5, 6]
for var in range(4):
    print(var)  # 0/n 1 /n 2 /n 3

s = "abcdefgh"
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")


def is_even(i):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    return i % 2 == 0


print(is_even(4))  # True
