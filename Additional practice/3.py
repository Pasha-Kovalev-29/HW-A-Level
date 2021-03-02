# Отсортируйте словарь по значению в порядке возрастания и убывания.

a = {1: 8, 2: 10, 3: 1, 4: 5, 5: 6}



def sort_increase(dict1):
    b = []
    dic={}
    for i in dict1.values():
        b.append(i)
    b.sort()
    for u in b:
        for key, value in dict1.items():
            if u==value:
                dic[key]=value
    return dic


def sort_increase_revers(dict1):
    b = []
    dic={}
    for i in dict1.values():
        b.append(i)
    b.sort(reverse=True)
    for u in b:
        for key, value in dict1.items():
            if u==value:
                dic[key]=value
    return dic


print(sort_increase(a))
print(sort_increase_revers(a))
