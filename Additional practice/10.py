# Напишите программу, которая принимает два списка
# и выводит все элементы первого, которых нет во втором.

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [6, 7, 8, 9, 10, 11]


def difference(list1, list2):
    result = set(list1) - set(list2)
    print(list(result))


difference(a, b)
