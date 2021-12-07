length = float (input('enter the length of the room in mts :'))
width =float(input('enter the width of the room in mts: '))
area = length * width
print ('the area of the room :',area,'sq.mts')


def areaoftheroom(length,width):
    area = length *width
    print("area of the rectangle is:%.2f sq.mts"%area)
    length = float(input('enter the length of the room in mts :'))
    width = float(input('enter the width of the room in mts: '))
    areaoftheroom(length, width)