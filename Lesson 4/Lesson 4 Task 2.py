# Заканчиваем прошлые задачи, украшаем работу физбазов работой со строками, списками,
# пробуем генераторы списков и прочие новые красоты, которые выучили. Доводим код до идеала!

f = open('test_unsorted.py', 'r')
res = open('result.py', 'w')  # если файла не существует, создается новый

all_result_list = []

for line in f:
    b = line.split()
    for i in range(len(b)):
        b[i] = int(b[i])
    b.sort()  # добавил метод сортировки, на случай, если вводные данные написаны в случайном порядке, как данные с test_unsorted.py

    fizz = int(b[0])
    buzz = int(b[1])
    value3 = int(b[2])
    print(' ')

    for i in range(1, value3 + 1):
        if (i % fizz == 0) and (i % buzz == 0):
            res.write('FB ')
        elif i % fizz == 0:
            res.write('F ')
        elif i % buzz == 0:
            res.write('B ')
        else:
            all_result_list.append(str(i))
            res.write(str(i) + ' ')
    res.write('\n')
f.close()
res.close()
print('Everything is recorded in result.py and append in list')

# выше создали список, в который добавили только числа

all_result_list = list(map(int, all_result_list))  # конвертируем каждый елемент списка с str в int

all_result_list.sort()  # сортируем по порядке
all_result_list.reverse()  # сортируем в обратном порядке
print(all_result_list)

# создаем генератор списка, который умножает все данные списка all_result_list
test_list = [i * 2 for i in all_result_list]
print(test_list)

# Вывод:
# [59, 58, 57, 56, 55, 54, 54, 53, 53, 52, 51, 51, 50, 49, 49, 49, 48, 47, 47, 47, 46, 46, 46, 45, 45, 45, 44, 43, 43, 43, 43, 43, 42, 42, 42, 42, 41....
# [118, 116, 114, 112, 110, 108, 108, 106, 106, 104, 102, 102, 100, 98, 98, 98, 96, 94, 94, 94, 92, 92, 92, 90, 90, 90, 88, 86, 86, 86, 86, 86, 84, 84, 84, 84.....
