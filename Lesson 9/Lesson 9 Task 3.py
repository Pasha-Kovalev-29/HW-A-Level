a = open('file.py', 'r')

for line in a:
    b = list(line.split(';'))
    c = list(map(int, list(b[0].split())))
    e = list(map(int, list(b[1].split())))
    d = int(sum(c) / (len(c)))
    d1 = int(sum(c) % len(c))

    if d == e[0]:
        if d1 == e[1]:
            print(True, line)
        else:
            print(False, line)
    else:
        print(False, line)

