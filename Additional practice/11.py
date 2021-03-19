a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def uniqueness(list):
    if len(list) == len(set(list)):
        print("Unique")
    else:
        print("Not unique")

uniqueness(a)