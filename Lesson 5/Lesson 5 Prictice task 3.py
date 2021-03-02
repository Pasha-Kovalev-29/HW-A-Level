# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк.
# Считаем частоту встретившихся слов в файле, но через функции и map, без единого цикла!

from collections import Counter

file = open('text_for_ practice_task_3.py', 'r')


def lower(a):
    return a.lower()


def counter(f):
    list_split = list(map(str, f.split()))
    list_split = map(lower, list_split)
    counter = Counter(list_split)
    return counter


print(list(map(counter, file)))

file.close()
