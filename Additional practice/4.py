# Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

a=[value for key, value in my_dict.items()]
a.sort(reverse=True)
finished_dict={}

for i in a:
    for key, value in my_dict.items():
        if i == value:
            finished_dict[key]=i

print(finished_dict)
