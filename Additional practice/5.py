# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

def convert(sec):
    second=sec
    minute=int(sec/60)
    hour=int(minute/60)
    day=int(hour/24)
    print('Days: ' + str(day) + ', Hour:' +str(hour) + ', Minute: '+ str(minute) + ', Second: ' + str(second))

s=int(input('Please enter seconds: '))
convert(s)