n = int(input('enter no.of bottles:'))
l=[]
for i in range (0,n):
    l.append(float(input('enter the volume in litres:')))
r = 0
for j in l:
    if(j<=1):
        r =r+0.1
    else:
        r=r+0.25
print('total refund will be{}'.format(r))