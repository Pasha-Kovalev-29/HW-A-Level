# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры

o = sum = int(input('Please enter an amount equivalent to UAH 10: '))  # 18790

thousand = 0
five_hundred = 0
two_hundred = 0
one_hundred = 0
fifty = 0
twenty = 0
ten = 0

if sum % 10 == 0:
    print('I give the following bills:')
    while o > 0:
        if o >= 8800:
            thousand = ((o - 8800) // 1000) + 1
            o = o - (thousand * 1000)
        elif (o < 8800) and (o >= 3800):
            five_hundred = ((o - 3800) // 500) + 1
            o -= (five_hundred * 500)
        elif (o < 3800) and (o >= 1800):
            two_hundred = ((o - 1800) // 200) + 1
            o -= (two_hundred * 200)
        elif (o < 1800) and (o >= 800):
            one_hundred = ((o - 800) // 100) + 1
            o -= (one_hundred * 100)
        elif (o < 800) and (o >= 300):
            fifty = ((o - 300) // 50) + 1
            o -= (fifty * 50)
        elif (o < 300) and (o >= 100):
            twenty = ((o - 100) // 20) + 1
            o -= (twenty * 20)
        elif o < 100:
            ten = o // 10
            o %= 10

    print('Face value 1000 UAH: ' + str(thousand))
    print('Face value 500 UAH: ' + str(five_hundred))
    print('Face value 200 UAH: ' + str(two_hundred))
    print('Face value 100 UAH: ' + str(one_hundred))
    print('Face value 50 UAH: ' + str(fifty))
    print('Face value 20 UAH: ' + str(twenty))
    print('Face value 10 UAH: ' + str(ten))

else:
    print('Error! Please enter an amount equivalent to UAH 10')

# I give the following bills:
# Face value 1000 UAH: 10
# Face value 500 UAH: 10
# Face value 200 UAH: 10
# Face value 100 UAH: 10
# Face value 50 UAH: 10
# Face value 20 UAH: 10
# Face value 10 UAH: 9
