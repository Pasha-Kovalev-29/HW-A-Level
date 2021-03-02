# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.

f = open('test.py')

for line in f:
    b=list(map(int, line.split()))

    fizz = int(b[0])
    buzz = int(b[1])
    value3 = int(b[2])
    print(' ')

    for i in range(1, value3 + 1):
        if (i % fizz == 0) and (i % buzz == 0):
            print('FB', end=' ')
        elif i % fizz == 0:
            print('F', end=' ')
        elif i % buzz == 0:
            print('B', end=' ')
        else:
            print(i, end=' ')
f.close()
