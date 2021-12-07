'''marks=[]
sub =[]
for i in range(6):
    sub.append(input('enter the sub'))
    marks.append(int(input('enter the marks')))

print(marks)

initial = 0

for i in marks:
    initial = initial + int(i)

print('initial',initial)

avg = (initial/6)

if avg>=75:
    print('average')
else:
    print('not good')

print(avg)'''

num = 10

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Neither pos. nor Neg.")

    
