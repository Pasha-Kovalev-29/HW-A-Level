# Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.
# После чего с помощью map применить ваши функции к списку строк.
# Отдельно каждую функцию к отдельному списку строк!

text1 = 'lowercase text'
text2 = 'UPPERCASE TEXT'
text3 = ['apple', 'pen', 'applepen']
text4 = ['PINEAPPLE', 'PEN', 'PINEAPPLEPEN']


def upper(a):
    return a.upper()


def lower(a):
    return a.lower()

print(upper(text1))
print(lower(text2))
print(list(map(upper, text3)))
print(list(map(lower, text4)))

# LOWERCASE TEXT
# uppercase text
# ['APPLE', 'PEN', 'APPLEPEN']
# ['pineapple', 'pen', 'pinapplepen']
