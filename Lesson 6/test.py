# Написать функцию перевода размеров женского белья из международного во все остальные.
# Внeтри функции нужно просто обращаться к правильно составленному словарю.

def converter(a, b):
    """
    input: country and international size
    a: country
    b: international size
    return: size for country
    """
    MIN = {'Russia': 42, 'Gernamia': 36, 'USA': 8, 'France': 38, 'Great_Britain': 24}
    step = {'XXS' : 0, 'XS': 2, 'S': 4, 'M': 6, 'L': 8, 'XL': 10, 'XXL': 12, 'XXXL': 14}
    R = MIN[a] + step[b]
    print('Size ' + str(b) + ' from ' + a + ': ' + str(R))


converter('USA', 'L')

# Size XXS from USA: 16