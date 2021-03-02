s = [1, 3, 5, 7, 'l']
y = [2, 4, 6, 'l', 6, 'a']
u = ['aa', 'bb', 'cc', 'ee', 'zz']


def zip_func(a, b, c):
    """
    input: three random lists
    combines three lists (including different lengths)
    return: one list
    """
    lr = min(len(a), len(b), len(c))
    zip = []
    for i in range(0, lr):
        zr = a[i], b[i], c[i]
        zip.append(zr)
    return zip


print(zip_func(s, y, u))
