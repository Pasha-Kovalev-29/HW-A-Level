value=int(input("Please, enter a value: "))

d=len(str(value)) #Находит кол-во цифр в числе

#Выводит разряды
i=0
r=1
while i<d:
    s=value//10
    b=value%10
    i+=1
    value=s
    print (str(r) + '*' + str(b))
    r*=10


