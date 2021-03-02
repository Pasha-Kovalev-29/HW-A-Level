# Банкомат выдает сумму максимально возможными купюрами

o = sum = int(input('Please enter an amount equivalent to UAH 5: '))  # 1885
thousand = 0
five_hundred = 0
two_hundred = 0
one_hundred = 0
fifty = 0
twenty = 0
ten = 0
five = 0

if sum % 5 == 0:
    print('I give the following bills:')
    while o > 0:
        if o >= 1000:
            thousand = o // 1000
            o %= 1000
            print('Face value 1000 UAH: ' + str(thousand))
        elif o >= 500:
            five_hundred = o // 500
            o %= 500
            print('Face value 500 UAH: ' + str(five_hundred))
        elif o >= 200:
            two_hundred = o // 200
            o %= 200
            print('Face value 200 UAH: ' + str(two_hundred))
        elif o >= 100:
            one_hundred = o // 100
            o %= 100
            print('Face value 100 UAH: ' + str(one_hundred))
        elif o >= 50:
            fifty = o // 50
            o %= 50
            print('Face value 50 UAH: ' + str(fifty))
        elif o >= 20:
            twenty = o // 20
            o %= 20
            print('Face value 20 UAH: ' + str(twenty))
        elif o >= 10:
            ten = o // 10
            o %= 10
            print('Face value 10 UAH: ' + str(ten))
        elif o >= 5:
            five = o // 5
            o %= 5
            print('Face value 5 UAH: ' + str(five))
else:
    print('Error! Please enter an amount equivalent to UAH 5')

# I give the following bills:
# Face value 1000 UAH: 1
# Face value 500 UAH: 1
# Face value 200 UAH: 1
# Face value 100 UAH: 1
# Face value 50 UAH: 1
# Face value 20 UAH: 1
# Face value 10 UAH: 1
# Face value 5 UAH: 1
