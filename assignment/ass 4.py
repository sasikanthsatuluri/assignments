length = int(input('length of the field in feet :'))
width = int(input('width of the field in feet :'))
area = (length*width)/43560
print('the area of the field is : ',area,'acres')

def areaofthefield(length,width):
    area = (length * width)/43560
    print("area of the field  is:%.2f acres" % area)
    length = int(input('enter the length of the field in feet :'))
    width = int(input('enter the width of the field in feet: '))
    areaofthefield(length, width)