# Напишите программу, которая выводит чётные числа
# из заданного списка и останавливается, если встречает число 237.

a = [1, 6, 3, 7, 2, 77, 55, 22, 568, 324, 256, 114, 237, 11, 56]

for i in a:
    if i == 237:
        break
    else:
        if not i % 2:
            print(i)
