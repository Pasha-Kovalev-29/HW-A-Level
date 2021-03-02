from itertools import zip_longest

s = [1, 2, 3, 4]
u = ['q', 'w', 'e', 'r', 't']
y = [5, 6, 7, 8]


def zip_func(a, b, c):
    """
    input: three random lists
    combines three lists (including different lengths)
    return: one list
    """
    return list(zip_longest(a, b, c))


print(zip_func(s, u, y))
