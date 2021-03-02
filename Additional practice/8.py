# При заданном целом числе n посчитайте n + nn + nnn.

a = str(input('Please enter integer: '))

a2 = a * 2
a3 = a * 3

result = int(a) + int(a2) + int(a3)
print(result)
