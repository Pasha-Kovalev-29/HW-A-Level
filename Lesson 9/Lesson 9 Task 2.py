a = int(input("Please enter number: "))
b = '*'

if (a > 0) and (a % 2):
    for m in range(1, a + 1, 2):
        print((b * m).center(a))
    for m in range(a - 2, 0, -2):
        print((b * m).center(a))


else:
    print("Error")
