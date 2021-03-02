# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.

a=input("Please enter sequence of numbers separated \",\" : ")
list_numbers=list(map(int, a.split(",")))
print(list_numbers)
set_numbers=set(map(int, a.split(",")))
print(set_numbers)