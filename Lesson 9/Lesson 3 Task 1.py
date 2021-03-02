import math


def find_flat(flat_number, flats_per_floor, floors_count):
    flats_per_entrance = flats_per_floor * floors_count #кол-во кварти в подъезде (кв на этаж*кол-во этажей)
    entrance_number = math.ceil(flat_number / flats_per_entrance) #подъезд (квартира / кол-во кв в подъезде)
    floor_number = math.ceil((flat_number - flats_per_entrance * (entrance_number - 1)) / flats_per_floor)
    return entrance_number, floor_number


a = int(input('Apartment number: '))
b = int(input('Apartments per floor : '))
c = int(input('Floor:'))
entrance, floor = find_flat(a, b, c)
print("Entrance to the house :", entrance, "Floor:", floor)