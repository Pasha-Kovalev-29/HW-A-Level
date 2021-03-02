print("Give it to me!")      #Выводит строку
number = int(input())        #Вводим число

if (number>=100):
    print ("Thanks, man!")            #Если введенное число больше или равно 100 - выводит "Thanks, man!"
elif ((number>10) and (number<100)):
    print("OK :(")                    #Если введенное число больше 10 и меньше 100 - выводит "OK :("
else:
    print("WHAAAAT???")               #Если введенное число меньше или равно 10 - выводит "WHAAAAT???"

if (number > 1000):
    print("!!!!WOOOOWWWW!!!")         #Если введенное число больше 1000 - выводит "!!!!WOOOOWWWW!!!"