# Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!

f = open('test.py', 'r')
res = open('result.py', 'w')  # если файла не существует, создается новый

for line in f:
    fizz, buzz, value3 = map(int, line.split())
    print(' ')

    for i in range(1, value3 + 1):
        if (not i % fizz) and (not i % buzz):
            res.write('FB ')
        elif not i % fizz:
            res.write('F ')
        elif not i % buzz:
            res.write('B ')
        else:
            res.write(str(i) + ' ')
    res.write('\n')
f.close()
res.close()
print('Everything is recorded in result.py')
