fizz=int(input("Please, enter fizz: "))
buzz= int(input("Please, enter buzz: "))
value3=int(input("Please, enter a value of three: "))

for i in range(1, value3+1):
    if (i%fizz==0) and (i%buzz==0):
        print('FB', end=' ')
    elif i%fizz==0:
        print ('F', end=' ')
    elif i%buzz==0:
        print('B', end=' ')
    else:
        print(i, end=' ')
